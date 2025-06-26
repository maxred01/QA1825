import requests
import time
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    ContextTypes, filters, CallbackQueryHandler
)

from test_api import test_run_api_tests

TOKEN = "8156293984:AAF9EszcYfG-Wmi9SCKbzTBcpNsOq9owog0"
ABOUT_TEXT = """*Обо мне*
Привет! Меня зовут *Полина Шубелько*, и я маленький тестировщик, который начинает свой путь. 
Закончила экономический университет, отработала 3 года в госах, и поняла, что нужно что-то менять в своей жизни. 
Попала на стажировку в белорусскую it-компанию, где работаю уже третий год ассистентом отдела продаж.
Говорят любовь живет три года, вот и я решила начать новую главу в своей трудовой деятельности. 
Дороги привели меня в тестирование, и мне тут нравится.
"""

ALLOWED_USERS = [1115361815]


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
    keyboard = [
        [InlineKeyboardButton("Запустить тесты", callback_data="run_tests")],
        [InlineKeyboardButton("Обо мне", callback_data="about"),
         InlineKeyboardButton("Контакты", callback_data="contact")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Привет! Я бот для тестирования веб-ресурсов.\n\n"
        "Я могу:\n"
        "• Проверить доступность любого сайта (просто отправь URL)\n"
        "• Запустить комплекс API-тестов\n"
        "• Показать информацию о разработчике\n\n"
        "Выбери действие:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(
            text=ABOUT_TEXT,
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text(ABOUT_TEXT, parse_mode="Markdown")


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Написать Полине", url="https://t.me/polinashubelko")]
    ])

    text = "Нажмите кнопку ниже, чтобы написать мне в Telegram:"

    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(
            text=text,
            reply_markup=keyboard,
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text(
            text,
            reply_markup=keyboard,
            parse_mode="Markdown"
        )


async def check_url(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = update.message.text.strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

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


async def run_tests_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.callback_query:
        user_id = update.callback_query.from_user.id
        message = update.callback_query.message
    else:
        user_id = update.message.from_user.id
        message = update.message

    if user_id not in ALLOWED_USERS:
        response = "⛔ У вас нет прав на выполнение этой команды!"
        if update.callback_query:
            await update.callback_query.answer(response, show_alert=True)
        else:
            await message.reply_text(response)
        return

    if update.callback_query:
        await update.callback_query.answer()
        status_message = await update.callback_query.edit_message_text(
            "🚀 Запускаю API-тесты... Пожалуйста, подождите...",
            parse_mode="Markdown"
        )
    else:
        status_message = await update.callback_query.edit_message_text(
            "🚀 Запускаю API-тесты... Пожалуйста, подождите...",
            parse_mode="Markdown"
        ) if update.callback_query else await message.reply_text(
            "🚀 Запускаю API-тесты... Пожалуйста, подождите...",
            parse_mode="Markdown"
        )

    try:
        loop = asyncio.get_running_loop()
        test_results = await loop.run_in_executor(None, test_run_api_tests)

        response_text = f"🔍 <b>Результаты API-тестов:</b>\n\n{test_results}"
        await context.bot.edit_message_text(
            chat_id=status_message.chat_id,
            message_id=status_message.message_id,
            text=response_text,
            parse_mode="HTML"
        )
    except Exception as e:
        error_text = f"⚠️ <b>Ошибка при выполнении тестов:</b>\n{str(e)}"
        await context.bot.edit_message_text(
            chat_id=status_message.chat_id,
            message_id=status_message.message_id,
            text=error_text,
            parse_mode="HTML"
        )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "run_tests":
        await run_tests_command(update, context)
    elif query.data == "about":
        await about(update, context)
    elif query.data == "contact":
        await contact(update, context)


def main() -> None:
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CommandHandler("runtests", run_tests_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_url))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()


if __name__ == "__main__":
    main()