import os

from fontTools.subset.svg import xpath
from selenium.webdriver.common.by import By

from stasya_voishnis.deplom.page.elements import WebElement, ManyWebElements
from stasya_voishnis.deplom.page.base_page import WebPage
import pytest_check as check

class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_URL') or 'https://www.royal.uk/'

        super().__init__(web_driver, url)

    btn_cookies = WebElement(xpath='//button[ @ id = "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')

    their_majesties_header_btn = WebElement(xpath='(//header[@class="header"]//a[contains(text(),"Their Majesties")]')
    royal_websites_header_btn = WebElement(xpath='(//header[@class="header"]//*[contains(text(),"Royal websites")]')
    search_header_btn = WebElement(xpath='(//header[@class="header"]//button[@class="search__toggle"]')
    logo_header_btn = WebElement(xpath='(//header[@class="header"]//a[@rel="home"]')
    the_king_header_btn = WebElement(xpath = '(//header[@class="header"]//ul[@class="main-menu__items"]//a[contains(text(),"The King")]')
    the_queen_header_btn = WebElement(xpath = '//header[@class="header"]//ul[@class="main-menu__items"]//a[contains(text(),"The Queen")]')
    the_coronation_header_btn = WebElement(xpath = '//header[@class="header"]//ul[@class="main-menu__items"]//a[contains(text(),"The Coronation")]')
    the_royal_family_header_btn = WebElement(xpath = '//header[@class="header"]//ul[@class="main-menu__items"]//a[contains(text(),"The Royal Family")]')
    queen_elizabeth_2_header_btn = WebElement(xpath = '//header[@class="header"]//ul[@class="main-menu__items"]//a[contains(text(),"Queen Elizabeth II")]')
    royal_residences_header_btn = WebElement(xpath = '//header[@class="header"]//ul[@class="main-menu__items"]//a[contains(text(),"Royal Residences, Art and History")]')
    news_header_btn = WebElement(xpath = '//header[@class="header"]//ul[@class="main-menu__items"]//a[contains(text(),"News")]')

    the_king_footer_btn = WebElement(xpath = '//footer[@class="footer"]//a[contains(text(),"The King")]')
    the_queen_footer_btn = WebElement(xpath = '//footer[@class="footer"]//a[contains(text(),"The Queen")]')
    the_coronation_footer_btn = WebElement(xpath = '//footer[@class="footer"]//a[contains(text(),"The Coronation")]')
    the_royal_family_footer_btn = WebElement(xpath = '//footer[@class="footer"]//a[contains(text(),"The Royal Family")]')
    queen_elizabeth_2_footer_btn = WebElement(xpath = '//footer[@class="footer"]//a[contains(text(),"Queen Elizabeth II")]')
    royal_residences_footer_btn = WebElement(xpath = '//footer[@class="footer"]//a[contains(text(),"Royal Residences, Art and History")]')
    news_footer_btn = WebElement(xpath = '//footer[@class="footer"]//a[contains(text(),"News")]')
    about_this_site_footer_btn = WebElement(xpath = '//footer[@class="footer"]//a[contains(text(),"About this site")]')
    contact_us_footer_btn = WebElement(xpath = '//footer[@class="footer"]//a[contains(text(),"Contact us")]')
    media_centre_footer_btn = WebElement(xpath = '//footer[@class="footer"]//a[contains(text(),"Media centre")]')
    privacy_footer_btn = WebElement(xpath = '//footer[@class="footer"]//a[contains(text(),"Privacy")]')
    report_a_vulnerability_footer_btn = WebElement(xpath = '//footer[@class="footer"]//a[contains(text(),"Report a Vulnerability")]')
    social_media_footer_btn = WebElement(xpath = '//footer[@class="footer"]//a[contains(text(),"Social Media Community Guidelines")]')
    working_for_us_footer_btn = WebElement(xpath = '//footer[@class="footer"]//a[contains(text(),"Working for us")]')
    logo_footer_footer_btn = WebElement(xpath = '//footer[@class="footer"]//img[@class="footer__crest"]")]')
    the_royal_household_footer_btn = WebElement(xpath = '//footer[@class="footer"]//p[@class="footer__copyright"]')

    news_blok = WebElement(xpath= '//a[@class="infinity-card__link"]')
