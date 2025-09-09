import os
from B2_framework.page.base_page import WebPage
from B2_framework.page.elements import ManyWebElements, WebElement

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

    support_service = WebElement(xpath='(//*[@id="footer"]//p[text()="Справочная служба"])')
    contacts = WebElement(xpath='//*[@id="footer"]//*[@id="belarus-only"]')
    email = WebElement(xpath='(//*[@id="footer"]//a[text()="support@belavia.by"])')
    official_name = WebElement(xpath='//*[@id="footer"]//*[@itemprop="name"]')
    address = WebElement(xpath='//*[@id="footer"]//*[@itemprop="address"]')

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

    slide_00 = WebElement(xpath='//*[@aria-describedby="slick-slide00"]')
    slide_01 = WebElement(xpath='//*[@aria-describedby="slick-slide01"]')
    slide_02 = WebElement(xpath='//*[@aria-describedby="slick-slide02"]')
    slide_03 = WebElement(xpath='//*[@aria-describedby="slick-slide03"]')
    slide_04 = WebElement(xpath='//*[@aria-describedby="slick-slide04"]')
    slide_05 = WebElement(xpath='//*[@aria-describedby="slick-slide05"]')
    slide_06 = WebElement(xpath='//*[@aria-describedby="slick-slide06"]')



