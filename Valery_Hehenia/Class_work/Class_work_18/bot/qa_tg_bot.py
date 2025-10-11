import os
import time
import zipfile
import asyncio
import logging
from pathlib import Path
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ===== НАСТРОЙКИ =====
BASE_DIR = Path(__file__).resolve().parents[1]
TOKEN = "8289688062:AAFZevVUE_dWH5U4VQAtCc3W3VUAcoqXchY"
TESTS_DIR_UI = Path("tests/UI")
TESTS_DIR_API = Path("tests/API")

# ===== ЛОГИ =====
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")
logger = logging.getLogger("allure-report-bot")

# ===== УТИЛИТЫ =====
async def sh(cmd: str, timeout: int = 1000) -> str:
    try:
        proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout)
        out = ""
        if stdout: out += f"STDOUT:\n{stdout.decode(errors='replace').strip()}"
        if stderr: out += f"\nSTDERR:\n{stderr.decode(errors='replace').strip()}"
        return out.strip() or "(пусто)"
    except asyncio.TimeoutError:
        return f"❌ Таймаут выполнения команды ({timeout} сек)"
    except Exception as e:
        logger.exception("Ошибка команды")
        return f"⚠️ Ошибка: {e}"

def truncate(msg: str, limit: int = 3800) -> str:
    return (msg[:limit] + "\n… (обрезано)") if len(msg) > limit else msg

def clean_dir(p: Path):
    p.mkdir(exist_ok=True, parents=True)
    for root, dirs, files in os.walk(p, topdown=False):
        for f in files: Path(root, f).unlink(missing_ok=True)
        for d in dirs: Path(root, d).rmdir()

# ===== ЯДРО =====
async def run_pytest(kind: str, update: Update) -> tuple[str, Path]:
    """
    kind: 'ui' | 'api' | 'all'
    Возвращает (вывод pytest, путь к allure-results-*)
    """
    results_dir = BASE_DIR / f"allure-results-{kind}"
    # подчистим предыдущие результаты
    if results_dir.exists():
        for root, dirs, files in os.walk(results_dir, topdown=False):
            for f in files: Path(root, f).unlink(missing_ok=True)
            for d in dirs: Path(root, d).rmdir()
    else:
        results_dir.mkdir(parents=True, exist_ok=True)

    # уведомление пользователю об очистке
    await update.message.reply_text("♻️ Старые результаты Allure очищены перед запуском.")

    if kind == "ui":
        target = TESTS_DIR_UI
    elif kind == "api":
        target = TESTS_DIR_API
    else:  # all
        # запуск двух каталогов подряд
        target = f"\"{TESTS_DIR_UI}\" \"{TESTS_DIR_API}\""

    # Проверка наличия тестов (для ui/api отдельно)
    if kind in ("ui", "api"):
        if not target.exists():
            return f"❌ Каталог с тестами не найден: {target}", results_dir
        if not any(target.rglob("test_*.py")):
            return f"❌ В {target} не найдено файлов test_*.py", results_dir

    # Команда pytest. В all target — уже строка с двумя путями
    if kind in ("ui", "api"):
        cmd = f'pytest -s -v "{target}" --alluredir="{results_dir}"'
    else:
        cmd = f"pytest -s -v {target} --alluredir=\"{results_dir}\""

    return await sh(cmd), results_dir

async def gen_allure(kind: str, results_dir: Path):
    if not results_dir.exists() or not any(results_dir.iterdir()):
        return "❌ Нет данных: allure-results пуст. Сначала запусти тесты.", None

    report_dir = BASE_DIR / f"allure-report-{kind}"
    report_dir.mkdir(exist_ok=True)

    check = await sh("allure --version")
    if "not found" in check.lower() or "ошибка" in check.lower():
        return "❌ Allure CLI недоступен. Установи и добавь в PATH.", None

    _ = await sh(f'allure generate "{results_dir}" --clean -o "{report_dir}"')
    if not (report_dir / "index.html").exists():
        return "❌ Ошибка генерации: index.html не создан.", None

    return None, report_dir

async def zip_and_send(update: Update, context: ContextTypes.DEFAULT_TYPE, kind: str, report_dir: Path, results_dir: Path):
    ts = int(time.time())
    zip_name = f"allure_{kind}_{ts}.zip"
    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(report_dir):
            for f in files:
                fp = Path(root, f)
                z.write(fp, arcname=os.path.join(f"allure-report-{kind}", os.path.relpath(fp, report_dir)))
        for root, _, files in os.walk(results_dir):
            for f in files:
                fp = Path(root, f)
                z.write(fp, arcname=os.path.join(f"allure-results-{kind}", os.path.relpath(fp, results_dir)))

    await update.message.reply_text("📤 Отправляю архив...")
    with open(zip_name, "rb") as fh:
        await context.bot.send_document(
            chat_id=update.effective_chat.id,
            document=fh,
            filename=zip_name,
            caption=f"📊 Allure {kind.upper()} (отчёт + результаты)"
        )
    os.remove(zip_name)

# ===== ХЕНДЛЕРЫ =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Доступные команды:\n"
        "• /runtests_ui — запустить только UI тесты\n"
        "• /runtests_api — запустить только API тесты\n"
        "• /runtests_all — запустить все тесты\n"
        "• /allure_ui — отчёт по UI\n"
        "• /allure_api — отчёт по API\n"
        "• /allure_all — общий отчёт\n"
        "• /full_ui — UI: тесты → отчёт\n"
        "• /full_api — API: тесты → отчёт\n"
        "• /full_all — ALL: тесты → отчёт\n"
        "• /about — информация"
    )

from telegram.constants import ParseMode

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🤖 <b>Allure Report Bot</b>\n"
        "Версия: 2.2\n"
        "Автор: Группа QA-1825 Гегеня Валерий\n"
        "\n"
        "<b>Назначение:</b> Автоматизация сайта\n"
        "Автоматизирует запуск <b>UI</b> и <b>API</b> тестов, формирует Allure-отчёты и отправляет их прямо сюда, в Telegram.\n"
        "\n"
        "<b>Основные команды:</b>\n"
        "• <code>/runtests_ui</code> — запустить только UI-тесты\n"
        "• <code>/runtests_api</code> — запустить только API-тесты\n"
        "• <code>/runtests_all</code> — запустить всё подряд\n"
        "\n"
        "• <code>/allure_ui</code> — сгенерировать отчёт по UI\n"
        "• <code>/allure_api</code> — отчёт по API\n"
        "• <code>/allure_all</code> — общий отчёт\n"
        "\n"
        "• <code>/full_ui</code> — UI: тесты + отчёт\n"
        "• <code>/full_api</code> — API: тесты + отчёт\n"
        "• <code>/full_all</code> — полный цикл\n"
        "\n"
        "<b>Как открыть отчёт вручную:</b>\n"
        "1️⃣ Скачай ZIP, который прислал бот\n"
        "2️⃣ Распакуй архив\n"
        "3️⃣ Открой файл <code>allure-report-*/index.html</code> в браузере\n"
        "\n"
        "<b>Альтернатива (локально):</b>\n"
        "<code>allure serve allure-results-ui</code>\n"
        "или\n"
        "<code>allure open allure-report-ui</code>\n"
        "\n"
        "<b>♻️ Очистка:</b> перед каждым запуском тестов и генерацией отчёта бот автоматически удаляет старые результаты, чтобы отчёт был свежим."
    )

    await update.message.reply_text(
        text,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )




# ---- RUNTETS ----
async def runtests_kind(update: Update, context: ContextTypes.DEFAULT_TYPE, kind: str):
    await update.message.reply_text(f"🔍 Запускаю {kind.upper()} тесты…")
    result, results_dir = await run_pytest(kind, update)
    if result.startswith("❌"):
        await update.message.reply_text(result)
        return

    # краткая сводка
    lines = [ln for ln in result.splitlines() if "FAILED" in ln or "ERROR" in ln or ("passed" in ln and "==" in ln)]
    summary = "\n".join(lines) or "✅ Все тесты прошли успешно!"
    await update.message.reply_text(truncate(f"📊 {kind.upper()} результаты:\n{summary}"))

async def run_ui(update: Update, context: ContextTypes.DEFAULT_TYPE):  return await runtests_kind(update, context, "ui")
async def run_api(update: Update, context: ContextTypes.DEFAULT_TYPE): return await runtests_kind(update, context, "api")
async def run_all(update: Update, context: ContextTypes.DEFAULT_TYPE): return await runtests_kind(update, context, "all")

# ---- ALLURE ----
async def allure_kind(update: Update, context: ContextTypes.DEFAULT_TYPE, kind: str):
    await update.message.reply_text(f"📈 Генерирую Allure-отчёт для {kind.upper()}…")
    # уведомление про очистку репорта (используем --clean)
    await update.message.reply_text("🧹 Старый Allure-отчёт будет удалён (--clean) перед созданием нового.")
    results_dir = Path(f"./allure-results-{kind}")
    err, report_dir = await gen_allure(kind, results_dir)
    if err:
        await update.message.reply_text(err)
        return
    await zip_and_send(update, context, kind, report_dir, results_dir)
    await update.message.reply_text("✅ Готово!")

async def allure_ui(update: Update, context: ContextTypes.DEFAULT_TYPE):  return await allure_kind(update, context, "ui")
async def allure_api(update: Update, context: ContextTypes.DEFAULT_TYPE): return await allure_kind(update, context, "api")
async def allure_all(update: Update, context: ContextTypes.DEFAULT_TYPE): return await allure_kind(update, context, "all")

# ---- FULL ----
async def full_kind(update: Update, context: ContextTypes.DEFAULT_TYPE, kind: str):
    await runtests_kind(update, context, kind)
    await allure_kind(update, context, kind)

async def full_ui(update: Update, context: ContextTypes.DEFAULT_TYPE):  return await full_kind(update, context, "ui")
async def full_api(update: Update, context: ContextTypes.DEFAULT_TYPE): return await full_kind(update, context, "api")
async def full_all(update: Update, context: ContextTypes.DEFAULT_TYPE): return await full_kind(update, context, "all")

# ===== MAIN =====
def main():
    os.chdir(BASE_DIR)
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))

    app.add_handler(CommandHandler("runtests_ui", run_ui))
    app.add_handler(CommandHandler("runtests_api", run_api))
    app.add_handler(CommandHandler("runtests_all", run_all))

    app.add_handler(CommandHandler("allure_ui", allure_ui))
    app.add_handler(CommandHandler("allure_api", allure_api))
    app.add_handler(CommandHandler("allure_all", allure_all))

    app.add_handler(CommandHandler("full_ui", full_ui))
    app.add_handler(CommandHandler("full_api", full_api))
    app.add_handler(CommandHandler("full_all", full_all))

    logger.info("✅ Бот запущен")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
