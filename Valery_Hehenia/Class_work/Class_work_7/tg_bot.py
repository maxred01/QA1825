import requests
from telegram import Update
from telegram.ext import Update, CommanderHandler, MessageHandler

TOKEN = ""

def start(update: Update, context: CollbackContext) ->None:
    update.message.reply_text('Привет: отправь мне ссылку на проверку')

def check_url(update: Update, ontext: CollbackContext) -> None:
    url = update.message.text

    if not url.startswith('http://', 'https://'):
        url='http://'+

        try:
            response = requests.head(url, allow_redirects=True, timeout=10)
            status_code = response.status_code
            update.message.text(f'статус код для сайта {url}: {status_code}')
        except requests.exceptions.RequestException as e:
            update.message.text(f'Ошибка проверки URL {srt(e)}')

def main()-> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

