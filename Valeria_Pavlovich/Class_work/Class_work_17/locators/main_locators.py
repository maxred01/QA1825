import os
from Valeria_Pavlovich.Class_work.Class_work_17.page.base_page import WebPage
from Valeria_Pavlovich.Class_work.Class_work_17.page.elements import WebElement
from Valeria_Pavlovich.Class_work.Class_work_17.page.elements import ManyWebElements
class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_URL') or 'https://hotels.belavia.by/'

        super().__init__(web_driver, url)
    belavia_logo = WebElement(xpath='//*[@data-testid="header-logo-link"]//*[@alt=""]')
    ostrovok_logo = WebElement(xpath='(//*[@alt="" and @src="https://f.worldota.net/ostrota/theme/ostrovok_v2/logo-20240322100815.svg"])[1]')
    language_widget = WebElement(xpath='//*[@data-testid="language-widget-control"]')
    currency_widget = WebElement(xpath='//*[@data-testid="currency-control"]')
    feedback_form = WebElement(xpath='//*[@data-testid="support-control"]')
    sign_in_button = WebElement(xpath='//*[@data-testid="sing-in-control"]')
    menu_button = WebElement(xpath='//*[@data-testid="menu-widget-control"]')