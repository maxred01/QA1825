import os

from bachko_irina.class_work.class_work_12.page.elements import WebElement, ManyWebElements
from bachko_irina.class_work.class_work_13.base_page import WebPage

class ButtonPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("BUTTON_URL") or "https://demoqa.com/buttons"

        super().__init__(web_driver, url)

    right_click_btn = WebElement(id="rightClickBtn")
    double_click_btn = WebElement(id="doubleClickBtn")
    upload_file = WebElement(id="uploadFile")
    double_click_message = WebElement(id="doubleClickMessage")