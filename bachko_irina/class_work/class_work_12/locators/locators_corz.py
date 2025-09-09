import os
from tehno.page.base_page import WebPage
from tehno.page.elements import ManyWebElements, WebElement


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://spacex.com/"

        super().__init__(web_driver, url)

    Logo = WebElement(xpath='//div[@class="spacex-logo"]')