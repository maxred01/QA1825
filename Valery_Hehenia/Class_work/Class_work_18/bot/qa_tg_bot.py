import os
import zipfile
import time
import asyncio
from pathlib import Path
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

UI_TESTS = Path("./tests/UI")
API_TESTS = Path("./tests/API")
RESULTS_DIR = Path("./allure-results")
REPORT_DIR = Path("./allure-report")

def clean_results():
    RESULTS_DIR.mkdir(exist_ok=True)
    for f in RESULTS_DIR.glob("*"):
        if f.is_file():
            f.unlink()


async def execute_command(cmd: str, update: Update, timeout: int = 300) -> str:
    """Выполняет shell-команду с таймаутом и возвращает результат"""
    try:
        proc = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout)
        output = f"STDOUT:\n{stdout.decode().strip()}" if stdout else ""
        output += f"\nSTDERR:\n{stderr.decode().strip()}" if stderr else ""
        return output.strip()
    except asyncio.TimeoutError:
        return f"❌ Таймаут ({timeout} сек)"
    except Exception as e:
        return f"⚠️ Ошибка: {str(e)}"


async def run_tests(update: Update, context: ContextTypes.DEFAULT_TYPE, test_path: Path):
    await update.message.reply_text(f"🔍 Запускаю тесты: {test_path.name}")
    clean_results()
    cmd = f'pytest -s -v "{test_path}" --alluredir="{RESULTS_DIR}"'
    stdout = await execute_command(cmd, update)
    short_result = "\n".join([line for line in stdout.split("\n") if "FAILED" in line or "ERROR" in line])
    if short_result:
        await update.message.reply_text(f"📊 Результаты тестов:\n{short_result[:3000]}")
    else:
        await update.message.reply_text("✅ Все тесты прошли успешно!")

async def run_tests_ui(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await run_tests(update, context, UI_TESTS)

async def run_tests_api(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await run_tests(update, context, API_TESTS)

async def run_tests_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Все тесты по очереди без создания подкаталогов
    await run_tests(update, context, UI_TESTS)
    await run_tests(update, context, API_TESTS)




async def generate_allure_report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Генерация Allure отчета из всех существующих папок в results"""
    results_dir = Path("./results")
    report_dir = Path("./allure-report")
    report_dir.mkdir(exist_ok=True)

    # Находим все подкаталоги с результатами тестов
    test_dirs = [p for p in results_dir.iterdir() if p.is_dir() and any(p.iterdir())]
    if not test_dirs:
        await update.message.reply_text("❌ Нет данных для отчета: папка results пуста")
        return

    await update.message.reply_text(f"📈 Генерирую Allure-отчет из: {', '.join(p.name for p in test_dirs)}")

    for test_dir in test_dirs:
        cmd = f'allure generate "{test_dir}" --clean -o "{report_dir}"'
        result = await execute_command(cmd, update)
        await update.message.reply_text(result)

    report_index = report_dir / "index.html"
    if not report_index.exists():
        await update.message.reply_text("❌ Ошибка генерации: index.html не найден")
        return

    await update.message.reply_text("✅ Allure Report успешно сгенерирован!")
async def open_allure_report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Генерация и открытие интерактивного Allure отчета из всех существующих папок в results"""
    results_dir = Path("./results")
    report_dir = Path("./allure-report")
    report_dir.mkdir(exist_ok=True)

    # Находим все подкаталоги с результатами тестов
    test_dirs = [p for p in results_dir.iterdir() if p.is_dir() and any(p.iterdir())]
    if not test_dirs:
        await update.message.reply_text("❌ Нет данных для отчета: папка results пуста")
        return

    await update.message.reply_text(f"📈 Генерирую Allure-отчет из: {', '.join(p.name for p in test_dirs)}")

    # Генерация отчета из каждой папки, объединяя результаты
    combined_results = Path("./results/combined")
    combined_results.mkdir(exist_ok=True)
    # Копируем все файлы из существующих папок в combined_results
    for test_dir in test_dirs:
        for file in test_dir.iterdir():
            target = combined_results / file.name
            if file.is_file():
                target.write_bytes(file.read_bytes())
            elif file.is_dir():
                # Простое копирование содержимого директорий
                for subfile in file.rglob("*"):
                    rel_path = subfile.relative_to(file)
                    dest = combined_results / rel_path
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    if subfile.is_file():
                        dest.write_bytes(subfile.read_bytes())

    # Генерация отчета в report_dir
    cmd = f'allure generate "{combined_results}" --clean -o "{report_dir}"'
    result = await execute_command(cmd, update)
    await update.message.reply_text(result)

    report_index = report_dir / "index.html"
    if not report_index.exists():
        await update.message.reply_text("❌ Ошибка генерации: index.html не найден")
        return

    await update.message.reply_text("✅ Allure Report успешно сгенерирован! 🔹 Открываю интерактивно...")

    # Открываем интерактивно
    os.system(f'start cmd /k allure serve "{combined_results}"')


async def full_cycle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Полный цикл: тесты + отчет"""
    await run_tests(update, context)
    await generate_allure_report(update, context)


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Информация о боте"""
    about_text = """
🤖 *Allure Report Bot*
Версия: 2.1
Автор: Ваша команда
Функционал:
- Запуск тестов (/runtests)
- Генерация отчета (/allurereport)
- Полный цикл (/fullreport)
    """
    await update.message.reply_text(
        about_text.strip(),
        parse_mode='MarkdownV2',
        disable_web_page_preview=True
    )


def main():
    application = Application.builder().token("8289688062:AAFZevVUE_dWH5U4VQAtCc3W3VUAcoqXchY").build()

    handlers = [
        CommandHandler("runtests_ui", run_tests_ui),
        CommandHandler("runtests_api", run_tests_api),
        CommandHandler("runtests_all", run_tests_all),
        CommandHandler("allurereport", generate_allure_report),
        CommandHandler("openreport", open_allure_report),
        CommandHandler("fullreport", full_cycle),
        CommandHandler("about", about)
    ]

    for handler in handlers:
        application.add_handler(handler)

    print("🤖 Бот запущен, ждём команд...")
    application.run_polling()


if __name__ == "__main__":
    main()