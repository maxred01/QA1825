import os

from bachko_irina.class_work.class_work_12.page.elements import WebElement, ManyWebElements
from bachko_irina.class_work.class_work_13.base_page import WebPage

class ShopPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://shop.spacex.com/"

        super().__init__(web_driver, url)

    btn_heder_1 = WebElement(xpath='//img[@alt="STARSHIP TORCH"]')

    text_heder_1 = WebElement(xpath='//a[@href="/collections/trending/products/starship-torch-2"]')

    text_price_1 = WebElement(xpath='//span[@data-product-id = "6993329717327"]')

    product_item= WebElement(xpath='//div[@class="ProductItem "]')

