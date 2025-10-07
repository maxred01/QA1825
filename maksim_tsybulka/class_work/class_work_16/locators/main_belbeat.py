import os
from super_puper_frame.page.base_page import WebPage
from super_puper_frame.page.elements import ManyWebElements, WebElement


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://belbet.by/'

        super().__init__(web_driver, url)

    btn_header_1 = WebElement(id='uw-main-button')
    btn_header_2 = WebElement(id='uw-button-chat')
    btn_header_3 = WebElement(xpath='//textarea[@placeholder="Введите текст"]')
    btn_header_4 = WebElement(xpath='//*[contains(text(),"Отклонить")]')
    btn_header_5 = WebElement(xpath='//a[@href="/games"]')
