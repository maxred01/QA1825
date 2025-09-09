from B2_framework.page.base_page import WebPage
from B2_framework.page.elements import WebElement
from B2_framework.page.elements import ManyWebElements
from B2_framework.locators.main_locators import MainPage
from B2_framework.tests.conftest import web_browser
def test_main(web_browser):
    driver = MainPage(web_browser)
    driver.language_btn.is_visible()

