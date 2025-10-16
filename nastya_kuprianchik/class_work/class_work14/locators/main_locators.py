import os
from xml.etree.ElementPath import xpath_tokenizer

from nastya_kuprianchik.class_work.class_work14.page.base_page import WebPage
from nastya_kuprianchik.class_work.class_work14.page.elements import WebElement
from bsuir.page.base_page import  WebPage
from bsuir.page.elements import WebElement

class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.hoyolab.com/circles/2/27/official?page_type=27&page_sort=news'
        super().__init__(web_driver, url)

    btn_header1 = WebElement(xpath='(//div[@id="header"]//div[contains(concat(' ', normalize-space(@class), ' '), " header-tab ")])[1]')
    #btn_header2 = WebElement(xpath='//div[@id="header"]//*[normalize-space(text())="Группа"]')
    #btn_header3 = WebElement(xpath='//div[@id="header"]//div[@role="button" and @title="Опубликуйте пост!"]')#опубликовать
    #btn_header4 = WebElement(xpath='//div[@id="header"]//div[@role="button" and @title="Уведомления"]')#уведомление
    #btn_header5 = WebElement(xpath='//div[@id="header"]//div[contains(@class,"header-account")]')#аккаунт
    #btn_footer1 = WebElement(xpath='//div[@class="footer"]//p[@class="footer__itemtext", "Контакты"]')
    #btn_footer2 = WebElement(xpath='//div[@class="footer"]//a[@href="/agreement?type=privacy", "Политика"]')
    #btn_footer3 = WebElement(xpath='//div[@class="footer"]//a[@href="/agreement", "Условия"]')
    #btn_footer4 = WebElement(xpath='//div[@class="footer"]//a[@href="https://account.hoyoverse.com/?lang=ru-ru&bbs_theme=dark&bbs_theme_device=1#/about/privacy", "Политика учетной записи"]')
    #btn_footer5 = WebElement(xpath='//div[@class="footer"]//a[@href="https://account.hoyoverse.com/?lang=ru-ru&bbs_theme=dark&bbs_theme_device=1#/about/userAgreement", "Условия учетной записи"]')
    #btn_footer6 = WebElement(xpath='//div[@class="footer"]//a[@href="hoyolab.com/article/928383?bbs_theme=dark&bbs_theme_device=1", "Правила сообщества"]')
    #btn_footer7 = WebElement(xpath='//div[@class="footer"]//a[@href="hoyolab.com/article/928383?bbs_theme=dark&bbs_theme_device=1", "Правила сообщества"]')

    btn_sel = WebElement(xpath='((//*[@data-route-name="circles-game_id-channel_id-official"]//button)[3]//*[local-name() = "font"])[2]')
    btn_close_login_popup = WebElement(xpath='//*[@aria-label="close"]')

    search_button = WebElement(xpath='//div[@id="header"]//*[contains(concat(' ', normalize-space(@class), ' '), "mhy-search-bar__input")]')
