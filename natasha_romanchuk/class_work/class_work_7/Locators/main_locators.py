import os
from nuts_nuts_nuts.page1.base_page import WebPage
from nuts_nuts_nuts.page1.elements import WebElement ,ManyWebElements


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_URL') or 'https://emall.by/'

        super().__init__(web_driver, url)


    logotip = WebElement(xpath='//div[@id="header__inner"]//*[@class="logo_logo__LbCcG"]')
    search_input = WebElement(xpath='//div[@id="header__inner"]//input[@placeholder="Поиск товаров"]')
    search_button = WebElement(xpath='//*[@aria-label="Начать поиск"]')
    catalog_button = WebElement(xpath='//*[@class="catalog_button__yhaM7"]')

    # авторизация
    action_button_enter = WebElement(xpath='//div[@id="header__inner"]//span[contains(text(),"Войти")]')
    action_button_orders = WebElement(xpath='//div[@id="header__inner"]//span[contains(text(),"Заказы")]')
    action_button_favorites = WebElement(xpath='//div[@id="header__inner"]//span[contains(text(),"Избранное")]')
    action_button_basket = WebElement(xpath='//a[@href="https://emall.by/cart"]')

    # разделы
    actions_button = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Акции")]')
    lucky_goods_button = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Товары-везунчики")]')
    promocodes_button = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Промокоды")]')
    new_button = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Новинки")]')
    urgent_goods_button = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Срочный товар!")]')
    take_more_button = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Упаковкой выгоднее")]')
    naushniki_besprovodnye_button = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Наушники беспроводные")]')
    school_button = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Школа")]')
    detskaya_stirka_button = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Детская стирка")]')

    # верхнее меню
    adress_text = WebElement(xpath='//div[@id="header__inner"]//span[contains(text(),"Адрес доставки")]')
    ykazat_adress_button = WebElement(xpath='//div[@id="header__inner"]//button[contains(text(),"Указать")]')
    payment_delivery_button = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Доставка и оплата")]')
    oplata_chastyami_button = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Оплата частями")]')
    seller_emall_button = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Продавайте на emall")]')
    business_emall_button = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Emall для юр. лиц")]')
    edostavka_button = WebElement(xpath='//div[@id="header__inner"]//a[contains(text(),"Edostavka")]')

   # футер

    compania_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Компания")]')
    servise_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"О сервисе")]')
    contacty_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Контакты")]')
    news_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Новости")]')
    vacansii_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Вакансии")]')
    sotrydnichestvo_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Сотрудничество")]')
    dostavca_dlya_urlic_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Доставка для юр.лиц")]')
    postavsikam_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Поставщикам")]')
    reklamodatelam_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Рекламодателям")]')
    stat_prodavcom_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Стать продавцом")]')
    prodaza_avto_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Продажа автомобилей")]')
    pokypatelam_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Покупателям")]')
    polz_soglashenie_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Пользовательское соглашение")]')
    vopros_otvet_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Вопрос-ответ")]')
    dostavka_oplata_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Доставка и оплата")]')
    katalog_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Каталог")]')
    tovari_ot_emall_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Товары от магазина Emall")]')
    punkti_vidachi_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Пункты выдачи")]')
    soglashenie_o_creditax_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Соглашение о кредитных ресурсах")]')
    nashi_druzia_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Наши друзья")]')
    edostavca_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Едоставка")]')
    evropochta_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Европочта")]')
    evroopt_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Евроопт")]')
    xit_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Хит!")]')
    groshik_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Грошык")]')
    my_socsetyax_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Мы в соц. сетях")]')
    nashi_prilozenia_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Наши приложения")]')
    sviazatsa_snamy_button = WebElement(xpath='//footer[@id="footer"]//*[contains(text(),"Связаться с нами")]')
    
    cookies_button = WebElement(xpath='//button[@type="button"]//*[contains(text(),"Принять")]')
    close_button = WebElement(xpath='//button[@type="button"]//*[contains(text(),"Закрыть")]')

    brands_button = ManyWebElements(xpath='//a[@class="brands_link__3NOhi"]')

    all_products = ManyWebElements(xpath='//div[@class="adult-wrapper_adult__yIhdE vertical_product__hiLyN products_product__DBmFj"]')
    search_results = WebElement(xpath='//span[@class="search_heading_query__Ci6uB"]')

    vkorzine_btn = ManyWebElements(xpath='//div[@class="vertical_actions__YjIyP"]')
    v_korzine_dtn_1 = WebElement(xpath='(//div[@class="adult-wrapper_adult__yIhdE vertical_product__hiLyN products_product__DBmFj"]//span[contains(text(),"В корзину")])[1]')
    korzina_product_name = WebElement(xpath='//a[@class="product_name__4NbXl"]')
    main_product_name = WebElement(xpath='(//a[@class="vertical_title__FM_Ud"])[1]')
    korzina_product_counter = WebElement(xpath='//div[@class="cart_prices__value__3mhYj"]//*[contains(text(),"товар")]')
    product_counter = WebElement(xpath='//div[@class="product_counter__nqFWd"]//*[@aria-label="Количество"]')
    korzina_product_price= WebElement(xpath='//div[@class="cart_prices__total__Gtyvn"]//*[contains(text(),"р.")]')
    main_product_price= WebElement(xpath='(//div[@data-nosnippet="true"]//span[@class="price_main__ZI_hw price_main_red__nTPA_"])[1]')
    main_skidka= WebElement(xpath='(//div[@bis_skin_checked="1"]//span[@class="tag_tag__1KrVp tag_tag_size_small__qndcB tag_tag_reverse__qv92T"])[1]')
    bage_korzina_count= WebElement(xpath='//span[@class="badge-animation_badge__nBsm5 medium"]')
    main_izbrannoe= WebElement(xpath='(//*[@aria-label="Добавить в избранное"])[1]')
    main_img= WebElement(xpath='(//*[@class="product-webp-png-image_image__TCZIc card-image_image__eENi8"])[1]')
    main_name= WebElement(xpath='(//a[@class="vertical_title__FM_Ud"])[1]')
    favorite_name= WebElement(xpath='//a[@style="-webkit-line-clamp: 3;"]')

