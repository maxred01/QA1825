import os
from nastya_kuprianchik.class_work.class_work14.page.base_page import WebPage
from nastya_kuprianchik.class_work.class_work14.page.elements import WebElement


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.hoyolab.com'
        super().__init__(web_driver, url)

    btn_header1 = WebElement(xpatch='//div[@id="header"]//p[@class="header-tab-name", "Главная"]')
    btn_header2 = WebElement(xpatch='//div[@id="header"]//div[@class="topbar-game-select", "Группа"]')
    btn_header3 = WebElement(xpatch='//div[@id="header"]//i[@class="mhy-icon iconfont icon-header_post", "Опубликовать пост!"]')
    btn_header4 = WebElement(xpatch='//div[@id="header"]//i[@class="mhy-icon iconfont icon-header_notification", "Уведомления"]')
    btn_header5 = WebElement(xpatch='//div[@id="header"]//div[@class="header-item header-account", "Аккаунт"]')
    btn_footer1 = WebElement(xpatch='//div[@class="footer"]//p[@class="footer__itemtext", "Контакты"]')
    btn_footer2 = WebElement(xpatch='//div[@class="footer"]//a[@href="/agreement?type=privacy", "Политика"]')
    btn_footer3 = WebElement(xpatch='//div[@class="footer"]//a[@href="/agreement", "Условия"]')
    btn_footer4 = WebElement(xpatch='//div[@class="footer"]//a[@href="https://account.hoyoverse.com/?lang=ru-ru&bbs_theme=dark&bbs_theme_device=1#/about/privacy", "Политика учетной записи"]')
    btn_footer5 = WebElement(xpatch='//div[@class="footer"]//a[@href="https://account.hoyoverse.com/?lang=ru-ru&bbs_theme=dark&bbs_theme_device=1#/about/userAgreement", "Условия учетной записи"]')
    btn_footer6 = WebElement(xpatch='//div[@class="footer"]//a[@href="hoyolab.com/article/928383?bbs_theme=dark&bbs_theme_device=1", "Правила сообщества"]')
    btn_footer7 = WebElement(xpatch='//div[@class="footer"]//a[@href="hoyolab.com/article/928383?bbs_theme=dark&bbs_theme_device=1", "Правила сообщества"]')

    btn_selector = WebElement(xpatch='//div[@class="mhy-interest-selector__footer"]//span[contains(text(), "Готово")]')
    btn_close_login_popup = WebElement(xpath='//button[@class="el-dialog__headerbtn"]')