
import requests
import time
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    ContextTypes, filters, CallbackQueryHandler
)

from natasha_romanchuk.class_work.class_work_7.tests.API.test_api import test_run_api_tests

TOKEN = "7821707602:AAHEhMXrg9-Bgxnv74g66_wNR67xloS42zM"
ABOUT_TEXT = """*Обо мне*  
Привет! Меня зовут  Наталья Романчук и я Junior QA Automation Engineer (Python)

🎓 Образование:
Компьютерная академия IT Step (QA Automation, Python, 2025)
Белорусский государственный аграрный технический университет (Менеджмент, 2012)
Школа интернет профессий (Специалист по интернет-рекламе Яндекс, 2017)

🧑‍🔧 Опыт работы:
🔹QA Automation Engineer (обучение), IT Step (февраль 2025 — н.в.)
Проект: «Заметки путешественника» — веб-приложение для создания заметок о путешествиях
Тест-дизайн: требования, тест-кейсы (Trello)
Инструменты: 
Trello (тест кейсы)
Jira (баг-репорты),
Postman (авто-тесты), https://web.postman.co/workspace/My-Workspace~5954eb37-dd10-410c-8512-44f63bcd65c1/collection/43826529-18d4f61b-09a2-4858-8776-dbf561de793b?action=share&source=copy-link&creator=43826529
отчетность

🔹 Ведущий специалист по маркетингу, РУП "БелЭЗ" (5 лет 4 месяца)
Тендеры, закупки, договора, аналитика, отчеты, запуск филиалов

🔹 Ведущий экономист, в/ч 15738 (2 года)
Бюджет, документация, отчеты, инвентаризации

📜 Сертификаты:
Introduction to SQL
https://www.sololearn.com/certificates/CC-3FIYZUGW
Introduction to Python
https://www.sololearn.com/certificates/CC-UCATCQ4M

🔧 Инструменты и технологии:
Python, Postman, Jira, Trello, Git
Тестирование REST API, написание чек-листов, баг-репортов
Основы автоматизации и написания автотестов

🔗 GitHub: [какую ссылку добавить?]

✉️ Сопроводительное письмо:
Я начинающий AQA Engineer с реальным опытом работы над учебным проектом. Уверенно применяю Postman для тестирования API, работаю с баг-трекингом в Jira, умею писать тест-кейсы и автоматизировать их. Готова развиваться в команде, где ценят ответственность и системный подход.
"""
ALLOWED_USERS = [815451005]


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
        [InlineKeyboardButton("Написать Наташе", url="https://t.me/lam_natali")]
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
        error_text = f'⚠️ < b > Ошибка при выполнении тестов: < / b >\n {str(e)} '
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