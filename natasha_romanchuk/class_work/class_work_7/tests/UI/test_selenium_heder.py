import allure
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By # стратегии поиска элементов
from selenium.webdriver.support.expected_conditions import element_located_selection_state_to_be
from selenium.webdriver.support.wait import WebDriverWait

from natasha_romanchuk.class_work.class_work_7.Locators.main_locators import MainPage
from natasha_romanchuk.class_work.class_work_7.tests.UI.conftest import web_browser
import pytest_check as check

@allure.feature("Header Navigation")
@allure.story("Visual Elements Display")
@allure.severity(allure.severity_level.NORMAL)
def test_header_elements_displayed(web_browser):
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
        check.greater_equal(products, 10)
        check.less_equal(products, 60)

@allure.feature("Главная страница")
@allure.story("Кнопки В корзине кликабельны")
def test_vkorzine(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()
    with allure.step('Скролл страницы вниз'):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    with allure.step('Кликаем по кнопке "В корзине"'):
        for btn in driver.vkorzine_btn:
            btn.click()
        assert btn.is_clickable()




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