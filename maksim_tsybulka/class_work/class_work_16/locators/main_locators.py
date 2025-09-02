import os
from maksim_tsybulka.class_work.class_work_16.page.base_page import WebPage
from maksim_tsybulka.class_work.class_work_16.page.elements import WebElement, ManyWebElements


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://emall.by/'

        super().__init__(web_driver, url)

    btn_header_1 = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Акции")]')
    btn_header_2 = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Товары-везунчики")]')
    btn_header_3 = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Промокоды")]')
    btn_header_4 = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Новинки")]')
    btn_header_5 = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Срочный товар!")]')
    btn_header_6 = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Упаковкой выгоднее")]')
    btn_header_7 = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Наушники беспроводные")]')
    btn_header_8 = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Школа")]')
    btn_header_9 = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Детская стирка")]')
    btn_header_10 = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Доставка и оплата")]')
    btn_header_11 = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Оплата частями")]')
    btn_header_12 = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Продавайте на emall")]')
    btn_header_13 = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Emall для юр. лиц")]')
    btn_header_14 = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Edostavka")]')
    
    btn_footer_1 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Компания")]')
    btn_footer_2 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"О сервисе")]')
    btn_footer_3 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Новости")]')
    btn_footer_4 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Вакансии")]')
    btn_footer_5 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Сотрудничество")]')
    btn_footer_6 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Доставка для юр.лиц")]')
    btn_footer_7 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Поставщикам")]')
    btn_footer_8 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Рекламодателям")]')
    btn_footer_9 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Стать продавцом")]')
    btn_footer_10 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Продажа автомобилей")]')
    btn_footer_11 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Покупателям")]')
    btn_footer_12 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Пользовательское соглашение")]')
    btn_footer_13 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Вопрос-ответ")]')
    btn_footer_14 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Доставка и оплата")]')
    btn_footer_15 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Каталог")]')
    btn_footer_16 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Товары от магазина Emall")]')
    btn_footer_17 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Пункты выдачи")]')
    btn_footer_18 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Соглашение о кредитных ресурсах")]')
    btn_footer_19 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Наши друзья")]')
    btn_footer_20 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Едоставка")]')
    btn_footer_21 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Европочта")]')
    btn_footer_22 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Евроопт")]')
    btn_footer_23 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Хит!")]')
    btn_footer_24 = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Грошык")]')


    btn_cookies = WebElement(xpath='//div[@id="cookies-modal-title"]//span[contains(text(), "Принять")]')
    btn_onboarding = WebElement(xpath='//div[@id="onboarding-banner"]//span[contains(text(), "Закрыть")]')

    btn_brands = ManyWebElements(xpath='class="adult-wrapper_adult__yIhdE vertical_product__hiLyN products_product__DBmFj"')
