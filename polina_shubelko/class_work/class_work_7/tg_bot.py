import requests
from telegram import Update
from telegram.exit import Update, CommandHandler, MessageHandle, CallbackContext

TOKEN = ""


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет: отправь мне ссылку на проверку')

def check_url(updatr: Update, context: CallbackContext) -> None:
    url = update.message.text

    if not url.startwitch('http://', 'https://'):
    url = 'http://' + url

    try:
    response = requests.head(url, allow_redirects=True, timeout=10)
    status_code = response.status_code
    update.message.text(f'Статус кода для сайта {url}: {status_code}')
    except requests.exceptions.RequestException as e:
    update.message.text(f'Ошибка проверки URL {str(e)}')


def main() -> None:

    updater = Update(TOKEN)
    dispatcher = updater.d

