import os
from Valery_Hehenia.Class_work.Class_work_18.page.base_page import WebPage
from Valery_Hehenia.Class_work.Class_work_18.page.elements import WebElement, ManyWebElements


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("BUTTON_URL") or 'https://www.demoblaze.com/index.html'

        super().__init__(web_driver, url)


    #################Header##################
    logo_btn = WebElement(css_selector = '#nava')
    home_btn = WebElement(css_selector = 'nav a:nth-of-type(2)')
    contact_btn = WebElement(css_selector = '[data-target="#exampleModal"]')
    about_btn = WebElement(css_selector = '#cartur')
    cart_btn = WebElement(xpath = '//a[@id="cartur"]')
    login_btn = WebElement(css_selector = '[data-target="#logInModal"]')
    sugnup_btn = WebElement(css_selector = '[data-target="#signInModal"]')

    #################Footer##################


    about_text = WebElement(xpath = '//b[contains(text(),"About Us")]')
    text_text = WebElement(xpath = '//p[contains(text(),"We believe performance needs to be validated")]')
    get_intouch_text = WebElement(xpath = '//b[contains(text(),"Get in Touch")]')
    address_text = WebElement(xpath = '//p[contains(text(),"Address")]')
    phone_text = WebElement(xpath = '//p[contains(text(),"Phone:")]')
    email_text = WebElement(xpath = '//p[contains(text(),"Email:")]')
    product_text = WebElement(xpath = '//h4[contains(text(),"PRODUCT STORE")]')

