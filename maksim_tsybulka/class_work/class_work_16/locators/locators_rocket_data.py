import os
from super_puper_frame.page.base_page import WebPage
from super_puper_frame.page.elements import ManyWebElements, WebElement


class RocketDataPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("ROCKET_URL") or 'https://rocketdata.ru/'

        super().__init__(web_driver, url)

    btn_header_1 = WebElement(xpath='(//*[@data-field-widthunits-value="px"])[4]//a')
    btn_header_2 = WebElement(xpath="(//a[@href='/upravlenie-dannymi-v-geoservisah' and contains(text(), 'Управление данными в геосервисах')])[1]")
    btn_header_3 = WebElement(xpath='(//*[@data-field-widthunits-value="px"])[2]//a')
    btn_cookies = WebElement(xpath='//button[@id="CybotCookiebotDialogBodyButtonAccept"]')
    btn_header_4 = WebElement(xpath='//div[@id="carrotquest-messenger-collapsed-container"]')
    btn_header_5 = WebElement(xpath='//textarea[@id="opened-textfield"]')
    btn_header_6 = WebElement(xpath='//button[@class="button button_xs opened-send-button accent svelte-v6ndz1"]')
    btn_header_7 = WebElement(xpath='//div[@class="t-popup__close t-popup__block-close"]')
    btn_header_8 = WebElement(xpath='//a[@href="#click_tel"]')



    resheniiya_btn = WebElement(xpath = '(//*[@data-field-widthunits-value="px"])[4]//a')
    upravlenie_dannymi_btn = WebElement(xpath = "(//a[@href='/upravlenie-dannymi-v-geoservisah' and contains(text(), 'Управление данными в геосервисах')])[1]")