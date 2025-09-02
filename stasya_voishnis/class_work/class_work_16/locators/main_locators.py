import os

from selenium.webdriver.common.by import By

from stasya_voishnis.class_work.class_work_16.page.elements import WebElement, ManyWebElements
from stasya_voishnis.deplom.page.base_page import WebPage


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_URL') or 'https://www.royal.uk/'

        super().__init__(web_driver, url)

    the_king_bth = WebElement(xpath='(//*[@aria-labelledby="block-mainnavigation-menu"]//a)[1]')
    the_queen_bth = WebElement(xpath = '(//*[@aria-labelledby="block-mainnavigation-menu"]//a)[2]')
    the_coronation_bth = WebElement(xpath = '(//*[@aria-labelledby="block-mainnavigation-menu"]//a)[3]')
    the_royal_family_bth = WebElement(xpath = '(//*[@aria-labelledby="block-mainnavigation-menu"]//a)[4]')
    queen_elizabeth_2_bth = WebElement(xpath = '(//*[@aria-labelledby="block-mainnavigation-menu"]//a)[5]')
    royal_residences_bth = WebElement(xpath = '(//*[@aria-labelledby="block-mainnavigation-menu"]//a)[6]')
    news_bth = WebElement(xpath = '(//*[@data-drupal-link-system-path="news"])[1]')