import os

from bachko_irina.class_work.class_work_12.page.elements import WebElement, ManyWebElements
from bachko_irina.class_work.class_work_13.base_page import WebPage

class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://spacex.com/"

        super().__init__(web_driver, url)

    Logo = WebElement(xpath='//div[@class="spacex-logo"]')
    Vehicles = WebElement(xpath='//div[@id="spacex-header"]//span[contains(text(),"Vehicles")]')
    Launches = WebElement(xpath='//div[@id="spacex-header"]//a[contains(text(),"Launches")]')
    HumanSpaceflight = WebElement(xpath='//div[@id="spacex-header"]//a[contains(text(),"Human Spaceflight")]')
    Rideshare = WebElement(xpath='//div[@id="spacex-header"]//a[contains(text(),"Rideshare")]')
    Starlink = WebElement(xpath='//div[@id="spacex-header"]//a[contains(text(),"Starlink")]')
    Starshield = WebElement(xpath='//div[@id="spacex-header"]//a[contains(text(),"Starshield")]')
    Company = WebElement(xpath='//div[@id="spacex-header"]//span[contains(text(),"Company")]')
    Shop = WebElement(xpath='//div[@id="spacex-header"]//a[contains(text(),"Shop")]')

    Careers = WebElement(xpath='//div[@class ="footer"]//a[contains(text(),"Careers")]')
    Updates = WebElement(xpath='//div[@class ="footer"]//a[contains(text(),"Updates")]')
    Privacy = WebElement(xpath='//div[@class ="footer"]//a[contains(text(),"Privacy")]')
    Policy = WebElement(xpath='//div[@class ="footer"]//a[contains(text(),"Policy")]')
    Suppliers = WebElement(xpath='//div[@class ="footer"]//a[contains(text(),"Suppliers")]')


