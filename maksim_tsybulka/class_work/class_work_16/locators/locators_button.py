import os
from maksim_tsybulka.class_work.class_work_16.page.base_page import WebPage
from maksim_tsybulka.class_work.class_work_16.page.elements import WebElement, ManyWebElements


class ButtonPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("BUTTON_URL") or 'https://demoqa.com/buttons'

        super().__init__(web_driver, url)

    double_click_btn = WebElement(id="doubleClickBtn")
    right_click_btn = WebElement(id="rightClickBtn")
    upload_file = WebElement(id="uploadFile")
    double_click_message = WebElement(id="doubleClickMessage")
