import requests
import time
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8156293984:AAF9EszcYfG-Wmi9SCKbzTBcpNsOq9owog0"

ABOUT_TEXT = """*Обо мне*
Привет! Меня зовут *Полина Шубелько*, и я маленький тестировщик, который начинает свой путь. 
Закончила экономический университет, отработала 3 года в госах, и поняла, что нужно что-то менять в своей жизни. 
Попала на стажировку в белорусскую it-компанию, где работаю уже третий год ассистентом отдела продаж.
Говорят любовь живет три года, вот и я решила начать новую главу в своей трудовой деятельности. 
Дороги привели меня в тестирование, и мне тут нравится.
"""


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
        [InlineKeyboardButton("Написать Полине", url="https://t.me/polinashubelko")]
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
