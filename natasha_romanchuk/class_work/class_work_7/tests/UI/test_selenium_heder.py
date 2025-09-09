import allure
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from nuts_nuts_nuts.conftest import chrome_options
from natasha_romanchuk.class_work.class_work_7.Locators.main_locators import MainPage
from nuts_nuts_nuts.conftest import web_browser
import pytest_check as check
from nuts_nuts_nuts.page1.base_page import WebPage
from nuts_nuts_nuts.page1.elements import WebElement

@allure.feature("Header Navigation")
@allure.story("Visual Elements Display")
@allure.severity(allure.severity_level.NORMAL)
def test_header_elements_displayed(web_browser, chrome_options):
    with allure.step('Запускаем и настраиваем браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step('Подготовка тестовых данных'):
        elements = [
            ( driver.logotip,"логотип"),
            ( driver.search_input,"строка поиска"),
            ( driver.search_button,"иконка поиска"),
            ( driver.catalog_button,"кнопка каталог"),
            ( driver.action_button_enter,"войти"),
            ( driver.action_button_orders,"заказы"),
            ( driver.action_button_favorites,"избранное"),
            ( driver.action_button_basket,"корзина"),
            ( driver.actions_button,"акции"),
            ( driver.lucky_goods_button,"товары-везунчики"),
            ( driver.promocodes_button,"промокоды"),
            ( driver.new_button,"новинки"),
            ( driver.urgent_goods_button,"срочный товар"),
            ( driver.take_more_button,"упаковкой выгоднее"),
            ( driver.naushniki_besprovodnye_button,"наушники беспроводные"),
            ( driver.school_button,"школа"),
            ( driver.detskaya_stirka_button,"детская стирка"),

    ]


    with allure.step('Проверка элемента'):
        for element, text_element in elements:
            with allure.step(f'Проверка элемента {text_element} на отображение'):
                check.is_true(element.is_visible(), f'Элемента {text_element} нет визуально')

            with allure.step(f'Проверка элемента {text_element} на кликабельность'):
                check.is_true(element.is_clickable(), f'Элемента {text_element} не кликабелен')

@allure.feature("Главная страница")
@allure.story("Футер")
def test_footers(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step('Подготовка тестовых данных'):
        elements = [
            (driver.compania_button, 'Компания'),
            (driver.servise_button, 'О сервисе'),
            (driver.news_button, 'Новости'),
            (driver.vacansii_button, 'Вакансии'),
            (driver.sotrydnichestvo_button, 'Сотрудничество'),
            (driver.dostavca_dlya_urlic_button, 'Доставка для юр.лиц'),
            (driver.postavsikam_button, 'Поставщикам'),
            (driver.reklamodatelam_button, 'Рекламодателям'),
            (driver.stat_prodavcom_button, 'Стать продавцом'),
            (driver.prodaza_avto_button, 'Продажа автомобилей'),
            (driver.pokypatelam_button, 'Покупателям'),
            (driver.polz_soglashenie_button, 'Пользовательское соглашение'),
            (driver.vopros_otvet_button, 'Вопрос-ответ'),
            (driver.dostavka_oplata_button, 'Доставка и оплата'),
            (driver.catalog_button, 'Каталог'),
            (driver.tovari_ot_emall_button, 'Товары от магазина Emall'),
            (driver.punkti_vidachi_button, 'Пункты выдачи'),
            (driver.soglashenie_o_creditax_button, 'Соглашение о кредитных ресурсах'),
            (driver.nashi_druzia_button, 'Наши друзья'),
            (driver.edostavka_button, 'Едоставка'),
            (driver.evropochta_button, 'Европочта'),
            (driver.evroopt_button, 'Евроопт'),
            (driver.xit_button, 'Хит!'),
            (driver.groshik_button, 'Грошык')
        ]

        skip_click_chek = ['Компания','Сотрудничество','Покупателям','Наши друзья']

    with allure.step('Проверка элемента'):
        for element, text_element in elements:
            with allure.step(f'Проверка элемента {text_element} на отображение'):
                check.is_true(element.is_visible(), f'Элемента {text_element} нет визуально на экарне')

            if text_element not in skip_click_chek:
                with allure.step(f'Проверка элемента {text_element} на кликабельность'):
                    check.is_true(element.is_clickable(), f'Элемента {text_element} не кликабелен')



    with allure.step('Проверка брендов'):
        check.equal(driver.brands_button.count(),20)


@allure.feature("Главная страница")
@allure.story("Хэдер")
def test_search_product(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step('Вводим запрос и нажимаем Enter'):
        search_product = driver.search_input
        search_product.send_keys("iPhone")
        search = driver.search_button
        search.click()
        time.sleep(10)

    with allure.step('Проверяем, что результаты поиска отображаются'):
        check.is_true(driver.search_results.is_visible(),"Результаты поиска не отображаются на странице")

        search_product.send_keys(Keys.CONTROL + "a") # Выделить все
        search_product.send_keys(Keys.DELETE)         # Очистить


@allure.feature("Главная страница")
@allure.story("Подсчет товаров и проверка наличия картинок")
def test_count_products(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step('Подсчет количества товаров'):

        products = driver.all_products.count()
        check.greater_equal(products, 10)  #от 10
        check.less_equal(products, 99)      # до 99

@allure.feature('Главная страница')
@allure.story('Кнопки "В корзине" кликабельны')
def test_vkorzine(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step("Скроллим страницу вниз"):
        driver._web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    with allure.step("Проверяем кликабельность кнопок 'В корзине'"):
        vkorzine_buttons = driver.vkorzine_btn.find()  # получаем список кнопок
        if not vkorzine_buttons:
            print("Кнопки 'В корзине' не найдены!")
            assert False, "Кнопки 'В корзине' не найдены!"

        wait = WebDriverWait(driver._web_driver, 10)

        for i, btn in enumerate(vkorzine_buttons, start=1):
            # Скроллим к кнопке
            driver._web_driver.execute_script("arguments[0].scrollIntoView(true);", btn)

            try:
                # Ждём, пока кнопка станет кликабельной
                wait.until(EC.element_to_be_clickable(btn))
                print(f"Кнопка {i} кликабельна ")
            except:
                print(f"Кнопка {i} НЕ кликабельна ")

@allure.feature('Главная страница')
@allure.story('Переход на сраницу "Контакты"через футер')
def test_kontakty(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step("Скроллим страницу вниз"):
        driver._web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    with allure.step('Нажимаем на кнопку "Контакты" в футуре'):
        driver.contacty_button.click()
    with allure.step("Проверяем, что открылась страница Контакты"):
        current_url = "https://emall.by/information/company/contacts"
        # print("Текущий URL:", current_url)
        assert current_url == "https://emall.by/information/company/contacts", \
            f"Ожидали страницу Контакты, а открылась {current_url}"



@allure.feature('Главная страница')
@allure.story('Переход по ссылкам футера')
def test_footer_links(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step('Подготовка тестовых данных'):
        footer_links = [
            (driver.servise_button, "https://emall.by/information/company/about-service"),
            (driver.contacty_button, "https://emall.by/information/company/contacts"),
            (driver.news_button, "https://emall.by/news"),
            (driver.postavsikam_button, "https://emall.by/information/company/conditions-for-selecting-a-counterparty"),
            (driver.reklamodatelam_button, "https://emall.by/information/company/advertisement"),
            (driver.vopros_otvet_button, "https://emall.by/information/help"),
            (driver.dostavka_oplata_button, "https://emall.by/information/help/132"),
            (driver.tovari_ot_emall_button, "https://emall.by/shop/1"),
            (driver.punkti_vidachi_button, "https://emall.by/map"),

        ]

        for button, expected_url in footer_links:
            with allure.step(f"Кликаем по кнопке и проверяем страницу"):
                button.click()
                driver.wait_page_loaded()
                current_url = driver.get_current_url()

                assert current_url == expected_url, f"Ожидали {expected_url}, а получили {current_url}"
                driver.go_back()

@allure.feature('Главная страница')
@allure.story('Добавление товара в корзину')
def test_add_goods(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step('Добавляем товар в корзину'):
        driver.v_korzine_dtn_1.click()



        # with allure.step('Отображение логотипа'):
    #     logo = driver.find_element(By.XPATH, driver.logotip)
    #     assert logo.is_displayed()
    #
    # with allure.step('Отображение строки поиска'):
    #     search  = driver.find_element(By.XPATH, driver.search_input)
    #     assert search.is_displayed()
    #
    # with allure.step('Отображение иконки поиска'):
    #     search_btn  = driver.find_element(By.XPATH, driver.search_button)
    #     assert search_btn.is_displayed()
    #
    # with allure.step('Отображение кнопки каталог'):
    #     catalog_btn  = driver.find_element(By.XPATH, driver.catalog_button)
    #     assert catalog_btn.is_displayed()