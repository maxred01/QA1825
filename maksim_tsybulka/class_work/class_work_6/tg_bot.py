import requests
import time
import os
import zipfile
import asyncio
from pathlib import Path
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8139847858:AAHQ8oxUiA4gUyWUPQ97GqacTkGoSfl_xzM"

ABOUT_TEXT = """
*Обо мне*  
Привет! Меня зовут *Максим Цыбулько*, и я анонимный тестироващик.
"""


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


async def run_tests(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Запуск тестов и сохранение результатов"""
    await update.message.reply_text("🔍 Запускаю тесты...")

    # Подготовка директории для результатов
    results_dir = Path("./allure-results")
    results_dir.mkdir(exist_ok=True)

    # Очистка предыдущих результатов
    for file in results_dir.glob("*"):
        file.unlink()

    # Запуск pytest
    result = await execute_command(
        "pytest -s -v tests --alluredir=./allure-results",
        update
    )

    # Проверка наличия результатов тестов
    if not any(results_dir.iterdir()):
        await update.message.reply_text("⚠️ Внимание: allure-results пуст. Возможно, тесты не запустились.")
        return

    # Отправка сокращенного отчета
    short_result = "\n".join([line for line in result.split("\n") if "FAILED" in line or "ERROR" in line])
    await update.message.reply_text(
        f"📊 Результаты тестов:\n{short_result[:3000]}" if short_result else "✅ Все тесты прошли успешно!"
    )


async def check_response_time(url: str) -> dict:
    result = {
        'status_code': None,
        'response_time_ms': None,
        'content_size': None,
        'error': None
    }

    try:
        start_time = time.time()
        response = requests.get(url, timeout=10)
        end_time = time.time()

        result['status_code'] = response.status_code
        result['response_time_ms'] = round((end_time - start_time) * 1000)
        result['content_size'] = len(response.content)

    except requests.exceptions.RequestException as e:
        result['error'] = str(e)

        return result


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Я могу:\n"
        "1. Проверить статус и время отклика сайта (просто отправь URL)\n"
        "2. Рассказать обо мне (/about)\n"
        "3. Связаться со мной (/contact)\n\n"
        "Пример: https://google.com или просто google.com",
        parse_mode="Markdown"
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(ABOUT_TEXT, parse_mode="Markdown")


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Написать Максиму", url="https://t.me/max_red01")]
    ])
    await update.message.reply_text(
        "Нажмите кнопку ниже, чтобы написать мне в Telegram:",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )


async def check_url(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = update.message.text.strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    # Используем отдельную функцию для проверки
    site_info = await check_response_time(url)

    if site_info['error']:
        await update.message.reply_text(f"Ошибка: `{site_info['error']}`", parse_mode="Markdown")
    else:
        message = (
            f" *Результат проверки {url}:*\n"
            f" Код статуса: `{site_info['status_code']}`\n"
            f" Время отклика: `{site_info['response_time_ms']} мс`\n"
            f" Размер контента: `{site_info['content_size']} байт`"
        )
        await update.message.reply_text(message, parse_mode="Markdown")


def main() -> None:
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_url))

    app.run_polling()


if __name__ == "__main__":
    main()
