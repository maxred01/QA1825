import os
from natasha_romanchuk.class_work.class_work_13.page.base_page import WebPage
from natasha_romanchuk.class_work.class_work_13.page.elements import WebElement ,ManyWebElements


class ButtonPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_URL') or 'https://demoqa.com/buttons'

        super().__init__(web_driver, url)

    double_click_btn = WebElement(id='doubleClickBtn')
    right_click_btn = WebElement(id='rightClickBtn')
    upload_click_btn = WebElement(id='uploadFile')
    double_click_btn_message = WebElement(id='doubleClickMessage')
