import os
from Valeria_Pavlovich.Class_work.Class_work_17.page.base_page import WebPage
from Valeria_Pavlovich.Class_work.Class_work_17.page.elements import WebElement
from Valeria_Pavlovich.Class_work.Class_work_17.page.elements import ManyWebElements
class ButtonPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('BUTTON_URL') or 'https://demoqa.com/buttons'

        super().__init__(web_driver, url)
    double_click_btn = WebElement(id='doubleClickBtn')
    right_click_btn = WebElement(id='rightClickBtn')
    upload_file = WebElement(id='uploadFile')
    double_click_messsage = WebElement(id='doubleClickMessage')