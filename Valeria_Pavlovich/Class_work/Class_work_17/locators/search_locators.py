import os
from B2_framework.page.base_page import WebPage
from B2_framework.page.elements import ManyWebElements, WebElement

class TicketSearch(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_URL') or 'https://belavia.by/'

        super().__init__(web_driver, url)
    dest_from = WebElement(xpath='//*[@id="OriginLocation_Combobox"]')
    dest_to = WebElement(xpath='//*[@id="DestinationLocation_Combobox"]')
    search_button = WebElement(xpath='//*[@id="next-trigger"]')

    one_way = WebElement(xpath='//*[@for="JourneySpan_Ow"]')
    return_way = WebElement(xpath='//*[@for="JourneySpan_Rt"]')
    dept_datepicker = WebElement(xpath='//*[@for="DepartureDate_Datepicker"]')
    return_datepicker = WebElement(xpath='//*[@for="ReturnDate_Datepicker"]')
    passengers = WebElement(xpath='//*[@id="Passengers"]')
    promo = WebElement(xpath='//*[@for="Promocode"]')
    point_pay = WebElement(xpath='//*[@for="IsRedemption"]')



