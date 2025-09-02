import os
from Valeria_Pavlovich.Class_work.Class_work_17.page.base_page import WebPage
from Valeria_Pavlovich.Class_work.Class_work_17.page.elements import WebElement
from Valeria_Pavlovich.Class_work.Class_work_17.page.elements import ManyWebElements
class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_URL') or 'https://belavia.by/'

        super().__init__(web_driver, url)
    menu_btn = WebElement(id='select-main-menu')
    language_btn = WebElement(id='select-lang')
    account_btn = WebElement(id='ffp-account')
    bad_vision_version = WebElement(id='bad_vision')
    belavia_logo = WebElement(xpath='//img[@alt="БЕЛАВИА - Авиакомпания Республики Беларусь"]')

    support_service = WebElement(xpath='(//*[@id="footer"]//p[text()="Справочная служба"])[1]')

    sales_office = WebElement(xpath='(//*[@id="footer"]//a[text()="Кассы продаж"])')
    timetable = WebElement(xpath='(//*[@id="footer"]//a[text()="Расписание"])')
    departure_arrival = WebElement(xpath='(//*[@id="footer"]//a[text()="Табло вылета/прилета"])')
    citizen_request = WebElement(xpath='(//*[@id="footer"]//a[text()="Обращения граждан"])')
    cargo_transport = WebElement(xpath='(//*[@id="footer"]//a[text()="Грузовые перевозки"])')
    for_agents = WebElement(xpath='(//*[@id="footer"]//a[text()="Агентам"])')
    on_air_magazine = WebElement(xpath='(//*[@id="footer"]//a[text()="Журнал OnAir"])')
    feedback = WebElement(xpath='(//*[@id="footer"]//a[text()="Обратная связь"])')
    media_contact = WebElement(xpath='(//*[@id="footer"]//a[text()="Для СМИ"])')
    improvement_year = WebElement(xpath='(//*[@id="footer"]//a[text()="2025 – Год благоустройства"])')

    facebook = WebElement(xpath='//*[@id="footer"]//*[@alt="Facebook"]')
    twitter = WebElement(xpath='//*[@id="footer"]//*[@alt="Twitter"]')
    instagram = WebElement(xpath='//*[@id="footer"]//*[@alt="Instagram"]')
    youtube = WebElement(xpath='//*[@id="footer"]//*[@alt="Youtube"]')
    vk = WebElement(xpath='//*[@id="footer"]//*[@alt="VKontakte"]')
    telegram = WebElement(xpath='//*[@id="footer"]//*[@alt="Telegram"]')





