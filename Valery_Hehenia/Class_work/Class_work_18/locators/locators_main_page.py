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


 #################Categories##################


    cat_block = WebElement(xpath = "//div[@class='list-group']")
    cat_phones = WebElement(xpath = """//a[@onclick="byCat('phone')"]""")
    cat_laptops = WebElement(xpath = """//a[@onclick="byCat('notebook')"]""")
    cat_monitors = WebElement(xpath = """//a[@onclick="byCat('monitor')"]""")


 #################Carusel##################


    carusel_block = WebElement(id = "carouselExampleIndicators")
    carusel_btn_next = WebElement(xpath = '//span[@class="carousel-control-next"]')
    carusel_btn_previous = WebElement(xpath = '//a[@class="carousel-control-prev"]')

    carusel_img_samsung = WebElement(xpath = '//img[@src="Samsung1.jpg"]')
    carusel_img_nexus = WebElement(xpath = '//img[@src="nexus1.jpg"]')
    carusel_img_iphone = WebElement(xpath = '//img[@src="iphone1.jpg"]')


