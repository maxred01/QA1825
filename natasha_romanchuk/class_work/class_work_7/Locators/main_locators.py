import os
from natasha_romanchuk.class_work.class_work_13.page.base_page import WebPage
from natasha_romanchuk.class_work.class_work_13.page.elements import WebElement ,ManyWebElements


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_URL') or 'https://emall.by/'

        super().__init__(web_driver, url)


    logotip = WebElement(xpath='//*[@alt="Емолл"]')
    search_input = WebElement(xpath='//*[@enterkeyhint="search"]')
    search_button = WebElement(xpath='//*[@aria-label="Начать поиск"]')
    catalog_button = WebElement(xpath='//*[@class="catalog_button__yhaM7"]')

    # авторизация
    action_button_enter = WebElement(xpath="//a[contains(@href, '/login')]")
    action_button_orders = WebElement(xpath="//a[contains(@href, '/orders')]")
    action_button_favorites = WebElement(xpath="//a[contains(@href, '/favorites')]")
    action_button_basket = WebElement(xpath="//a[contains(@href, '/cart')]")

    # разделы
    actions_button = WebElement(xpath="//a[contains(@href, '/actions')]")
    lucky_goods_button = WebElement(xpath="//a[contains(@href, '/actions/lucky-goods')]")
    promocodes_button = WebElement(xpath="//a[contains(@href, '/actions/promocodes')]")
    new_button = WebElement(xpath="//a[contains(@href, '/actions/new')]")
    urgent_goods_button = WebElement(xpath="//a[contains(@href, '/actions/urgent-goods')]")
    take_more_button = WebElement(xpath="//a[contains(@href, '/actions/take-more')]")
    naushniki_besprovodnye_button = WebElement(xpath="//a[contains(@href, '/category/naushniki-besprovodnye')]")
    school_button = WebElement(xpath="//a[contains(@href, '/actions/school-supplies')]")
    detskaya_stirka_button = WebElement(xpath="//a[contains(@href, '/category/4006')]")

    # верхнее меню
    adress_text = WebElement(xpath="//*[@class='address_slot_text__kNia1']")
    ykazat_adress_button = WebElement(xpath="//*[@class='touchable_button__c9Zij address_set_address_button__8ixQx']")
    payment_delivery_button = WebElement(xpath="//a[contains(@href, '/information/help/132') and contains(@class, 'desktop_top__link__')]")
    oplata_chastyami_button = WebElement(xpath="//a[contains(@href, '/news/3')]")
    seller_emall_button = WebElement(xpath="//a[contains(@href, 'seller.emall.by') and contains(@class, 'desktop_top__link__')]")
    business_emall_button = WebElement(xpath="//a[contains(@href, 'business.emall.by') and contains(@class, 'desktop_top__link__')]")
    edostavka_button = WebElement(xpath="//a[contains(@href, 'edostavka.by') and contains(@class, 'desktop_top__link__')]")

