import os
from stasya_voishnis.class_work.class_work_16.page.elements import WebElement, ManyWebElements
from stasya_voishnis.deplom.page.base_page import WebPage


class ButtonPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('BUTTON_PAGE') or 'https://demoqa.com/buttons'

        super().__init__(web_driver, url)

    double_click_bth = WebElement(id="doubleClickBtn")
    right_click_bth =  WebElement(id="rightClickBtn")
    upload_file =  WebElement(id="uploadFile")
    double_click_message =  WebElement(id="doubleClickMessage")