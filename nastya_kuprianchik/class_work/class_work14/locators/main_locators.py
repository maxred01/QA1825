import os
from nastya_kuprianchik.class_work.class_work14.page.base_page import WebPage
from nastya_kuprianchik.class_work.class_work14.page.elements import WebElement
from bsuir.page.base_page import  WebPage
from bsuir.page.elements import WebElement

class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.hoyolab.com/circles/2/27/official?page_type=27&page_sort=news'
        super().__init__(web_driver, url)

    btn_gl = WebElement(xpatch='//div[@id="header"]//[text()="Главная"]')
    btn_gr = WebElement(xpatch='//div[@id="header"]//*[text()="Группа"]')
    btn_pub = WebElement(xpatch='//div[@id="header"]//div[@role="button" and @title="Опубликуйте пост!"]')#опубликовать
    btn_uv = WebElement(xpatch='//div[@id="header"]//div[@title="Уведомления"]]')#уведомление
    btn_akk = WebElement(xpatch='//div[@id="header"]//div//img[contains(concat(' ', normalize-space(@class), ' '), " mhy-avatar__img ")]"]')#аккаунт
    #btn_footer1 = WebElement(xpatch='//div[@class="footer"]//p[@class="footer__itemtext", "Контакты"]')
    #btn_footer2 = WebElement(xpatch='//div[@class="footer"]//a[@href="/agreement?type=privacy", "Политика"]')
    #btn_footer3 = WebElement(xpatch='//div[@class="footer"]//a[@href="/agreement", "Условия"]')
    #btn_footer4 = WebElement(xpatch='//div[@class="footer"]//a[@href="https://account.hoyoverse.com/?lang=ru-ru&bbs_theme=dark&bbs_theme_device=1#/about/privacy", "Политика учетной записи"]')
    #btn_footer5 = WebElement(xpatch='//div[@class="footer"]//a[@href="https://account.hoyoverse.com/?lang=ru-ru&bbs_theme=dark&bbs_theme_device=1#/about/userAgreement", "Условия учетной записи"]')
    #btn_footer6 = WebElement(xpatch='//div[@class="footer"]//a[@href="hoyolab.com/article/928383?bbs_theme=dark&bbs_theme_device=1", "Правила сообщества"]')
    #btn_footer7 = WebElement(xpatch='//div[@class="footer"]//a[@href="hoyolab.com/article/928383?bbs_theme=dark&bbs_theme_device=1", "Правила сообщества"]')

    btn_sel = WebElement(xpatch='((//*[@data-route-name="circles-game_id-channel_id-official"]//button)[3]//*[local-name() = "font"])[2]')
    btn_close_login_popup = WebElement(xpath='//*[@aria-label="close"]')