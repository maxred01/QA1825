from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import zipfile
import time
import asyncio
from pathlib import Path

# ==== ПУТИ ПОД ТВОЙ ПРОЕКТ ====
TESTS_DIR = r"D:\Studies\QA\DZ\QA1825\Valery_Hehenia\Class_work\Class_work_18\tests\UI"
RESULTS_DIR = Path(r"D:\Studies\QA\DZ\QA1825\Valery_Hehenia\Class_work\Class_work_18\results")
REPORT_DIR = Path(r"D:\Studies\QA\DZ\QA1825\Valery_Hehenia\Class_work\Сlass_work_18\allure-report")

# ==== ТОКЕН БОТА ====
BOT_TOKEN = "8055190659:AAGeOUr8YNyCyUCSvJKcyCEFH18ow780O60"


# ==== Создание папок, если их нет ====
for path in [RESULTS_DIR, REPORT_DIR]:
    path.mkdir(parents=True, exist_ok=True)

async def execute_command(cmd: str, timeout: int = 300) -> str:
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


async def run_tests(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 Запускаю тесты...")

    RESULTS_DIR.mkdir(exist_ok=True)
    for file in RESULTS_DIR.glob("*"):
        file.unlink()

    cmd = f"pytest -s -v {TESTS_DIR} --alluredir={RESULTS_DIR}"
    result = await execute_command(cmd)

    if not any(RESULTS_DIR.iterdir()):
        await update.message.reply_text("⚠️ allure-results пуст. Возможно, тесты не запустились.")
        return

    short_result = "\n".join([line for line in result.split("\n") if "FAILED" in line or "ERROR" in line])
    await update.message.reply_text(
        f"📊 Результаты тестов:\n{short_result[:3000]}" if short_result else "✅ Все тесты прошли успешно!"
    )


async def generate_allure_report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if not RESULTS_DIR.exists() or not any(RESULTS_DIR.iterdir()):
            await update.message.reply_text("❌ Нет данных для отчета")
            return

        await update.message.reply_text("📈 Генерирую Allure-отчет...")
        REPORT_DIR.mkdir(exist_ok=True)

        cmd = f"allure generate {RESULTS_DIR} --clean -o {REPORT_DIR}"
        await execute_command(cmd)

        report_index = REPORT_DIR / "index.html"
        if not report_index.exists():
            await update.message.reply_text("❌ Ошибка генерации: index.html не найден")
            return

        await update.message.reply_text("📦 Создаю архив...")
        timestamp = int(time.time())
        zip_name = f"allure_report_{timestamp}.zip"

        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(REPORT_DIR):
                for file in files:
                    file_path = Path(root) / file
                    arcname = os.path.join("allure-report", os.path.relpath(file_path, REPORT_DIR))
                    zipf.write(file_path, arcname=arcname)

            for root, _, files in os.walk(RESULTS_DIR):
                for file in files:
                    file_path = Path(root) / file
                    arcname = os.path.join("allure-results", os.path.relpath(file_path, RESULTS_DIR))
                    zipf.write(file_path, arcname=arcname)

        await update.message.reply_text("📤 Отправляю архив...")
        with open(zip_name, 'rb') as zip_file:
            await context.bot.send_document(
                chat_id=update.effective_chat.id,
                document=zip_file,
                filename=zip_name,
                caption="📊 Allure Report (с исходными данными)"
            )

        os.remove(zip_name)
        await update.message.reply_text("✅ Отчет успешно отправлен!")

    except Exception as e:
        await update.message.reply_text(f"⚠️ Ошибка: {str(e)}")


async def full_cycle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await run_tests(update, context)
    await generate_allure_report(update, context)


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = """
🤖 *QA Allure Bot*
Функционал:
- /runtests – запуск тестов
- /allurereport – генерация отчета
- /fullreport – тесты + отчет
    """
    await update.message.reply_text(about_text.strip(), parse_mode='MarkdownV2')


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("runtests", run_tests))
    app.add_handler(CommandHandler("allurereport", generate_allure_report))
    app.add_handler(CommandHandler("fullreport", full_cycle))
    app.add_handler(CommandHandler("about", about))

    print("✅ Бот запущен и ждёт команды...")
    app.run_polling()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Приветствие при старте"""
    await update.message.reply_text(
        "👋 Привет! Я *QA Allure Bot*.\n\n"
        "Я умею запускать тесты и отправлять Allure-отчёты.\n"
        "Доступные команды:\n"
        "/runtests – Запуск тестов\n"
        "/allurereport – Генерация отчёта\n"
        "/fullreport – Тесты + отчёт\n"
        "/about – Информация о боте",
        parse_mode="MarkdownV2"
    )

if __name__ == "__main__":
    main()
