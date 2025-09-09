import os

from tehno.page.base_page import WebPage
from tehno.page.elements import WebElement, ManyWebElements

class ShopPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://shop.spacex.com"

        super().__init__(web_driver, url)

    btn_heder_1 = WebElement(xpath='//img[@alt="STARSHIP TORCH"]')

    text_heder_1 = WebElement(xpath='//span[@class="ProductItem__Title Heading"]//a[@href="/collections/trending/products/starship-torch-2"]')

    text_price_1 = WebElement(xpath='//span[@data-product-id = "6993329717327"]')

    product_item= ManyWebElements(xpath='//div[@class="ProductItem "]')

    product_item_2 = ManyWebElements(xpath='//div[@class="ProductItem__Info ProductItem__Info--center"]')
    product_item_name = ManyWebElements(xpath='//div[@class="ProductItem__Info ProductItem__Info--center"]//a')
    product_item_price = ManyWebElements(xpath='//div[@class="ProductItem__Info ProductItem__Info--center"]//span[@class="money"]')

