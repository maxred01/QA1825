from bsuir.page.base_page import WebPage
from bsuir.page.elements import ManyWebElements
from bsuir.locators.main_locators import MainPage

def test_main(web_browser):
    driver = MainPage(web_browser)

    driver.btn_header1.click()