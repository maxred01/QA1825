import os
from Valery_Hehenia.Class_work.Class_work_18.page.base_page import WebPage
from Valery_Hehenia.Class_work.Class_work_18.page.elements import WebElement, ManyWebElements


class ButtonPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("BUTTON_URL") or 'https://demoqa.com/buttons'

        super().__init__(web_driver, url)

    double_click_btn = WebElement(id="doubleClickBtn")
    right_click_btn = WebElement(id="rightClickBtn")
    left_click_btn = WebElement(id="dynamicClickMessage")
    upload_file = WebElement(id="INPUT")
    double_click_btn_message = WebElement(id="doubleClickMessage")
    right_click_btn_message = WebElement(id="rightClickMessage")

