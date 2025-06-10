import requests
from telegram import Update
from telegram.ext import Update, CommandHandler, MessageHandler, CallbackContext, Updater

TOKEN = ""

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет: отправь мне ссылку на проверку)

def chek_url(update: Update, context: CallbackContext) -> None:
    url = update.message.reply_text

    if not url.startwith('http://', 'https://'):
        url = 'http://' + url

    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        status_code = response.status_code
        update.message.text(f'Статус код для сайта {url}: {status_code}')
    except requests.exceptions.RequestException as e:
        update.message.text(f'Ошибка проверки URL {str(e)}')

def main() -> None:
    updater = Updater(TOKE)
    dispatcher = updater.d


