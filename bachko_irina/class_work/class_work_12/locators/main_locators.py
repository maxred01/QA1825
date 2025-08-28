import os

from bachko_irina.class_work.class_work_12.page.elements import WebElement, ManyWebElements
from bachko_irina.class_work.class_work_13.base_page import WebPage

class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://spacex.com/"

        super().__init__(web_driver, url)

    vehicles = WebElement(xpath='//div[@id="vehicles-menu-header"]')
    launches = WebElement(xpath='//a[@routerlink="/launches"]')
    humanspaceflight = WebElement(xpath='//a[@href="/humanspaceflight"]')
    rideshare = WebElement(xpath='//a[@href="/rideshare"]')
    starlink = WebElement(xpath='//a[@href="https://starlink.com"]')
    starshield = WebElement(xpath='// a[@href = "/starshield"]')
