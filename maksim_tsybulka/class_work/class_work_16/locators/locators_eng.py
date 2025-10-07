import os
from super_puper_frame.page.base_page import WebPage
from super_puper_frame.page.elements import ManyWebElements, WebElement


class EngPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("royal_URL") or 'https://www.royal.uk/'

        super().__init__(web_driver, url)

    btn_cooke = WebElement(id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    btn_news_all_main = ManyWebElements(xpath='//div[@class="infinity-card__content"]')
