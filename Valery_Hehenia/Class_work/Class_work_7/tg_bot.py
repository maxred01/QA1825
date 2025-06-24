import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# Токен вашего бота (замените на свой)
TOKEN = "8025703170:AAGtK4ey87I3gyaPoVVrIwSg7y-KG2JpPoo"

#Текст рассказа о себе
ABOUT_TEXT = """ *Обо мне*
     Привет! Меня зовут *Валерий Гегеня*, 
    и я анонимный тестировщий. Ловлю баги по утрам,
    по вечерам пишу TG-бота, а ночью учу Unity)
    """


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Отправь мне URL, и я проверю его HTTP-статус.\n"
        "Например: `https://google.com` или просто `google.com`",
        parse_mode="Markdown"
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(ABOUT_TEXT, parse_mode="Markdown")




async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Написать Валере", url="https://t.me.me/valery_hehenia")],
        [InlineKeyboardButton("Написать кому-то", url="https://t.me.me/valery_hehenia")]
    ])
    await update.message.reply_text(
        "Нажмите кнопку ниже, чтобы написать мне в Telegram:",
        reply_markup=keyboard,
        parse_mode="Markdown"
        )



async def check_url(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = update.message.text.strip()

    # Добавляем схему, если её нет
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        status_code = response.status_code
        await update.message.reply_text(f"🔎 *Статус-код для* `{url}`: `{status_code}`", parse_mode="Markdown")
    except requests.exceptions.RequestException as e:
        await update.message.reply_text(f"❌ Ошибка при проверке URL: `{str(e)}`", parse_mode="Markdown")



def main() -> None:
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_url))

    app.run_polling()


if __name__ == "__main__":
    main()
