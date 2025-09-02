import time
import allure
from maksim_tsybulka.class_work.class_work_16.locators.main_locators import MainPage
import pytest_check as check


@allure.feature("Главная страница")
@allure.story("Хедер")
def test_headers(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.btn_cookies.click()
        driver.btn_onboarding.click()

    with allure.step('Подготовка тестовых данных'):
        elements = [
            (driver.btn_header_1, 'Акции'),
            (driver.btn_header_2, 'Товары-везунчики'),
            (driver.btn_header_3, 'Промокоды'),
            (driver.btn_header_4, 'Новинки'),
            (driver.btn_header_5, 'Срочный товар!'),
            (driver.btn_header_6, 'Упаковкой выгоднее'),
            (driver.btn_header_7, 'Наушники беспроводные'),
            (driver.btn_header_8, 'Школа'),
            (driver.btn_header_9, 'Детская стирка'),
            (driver.btn_header_10, 'Доставка и оплата'),
            (driver.btn_header_11, 'Оплата частями'),
            (driver.btn_header_12, 'Продавайте на emall'),
            (driver.btn_header_13, 'Emall для юр. лиц'),
            (driver.btn_header_14, 'Edostavka')
                    ]

    with allure.step('Проверка элемента'):
        for element, text_element in elements:
            with allure.step(f'Проверка элемента {text_element} на отображение'):
                check.is_true(element.is_visible(), f'Элемента {text_element} нет визуально на экарне')

            with allure.step(f'Проверка элемента {text_element} на кликабельность'):
                check.is_true(element.is_clickable(), f'Элемента {text_element} не кликабелен')


@allure.feature("Главная страница")
@allure.story("Футер")
def test_footers(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.btn_cookies.click()
        driver.btn_onboarding.click()

    with allure.step('Подготовка тестовых данных'):
        elements = [
            (driver.btn_footer_1, 'Компания'),
            (driver.btn_footer_2, 'О сервисе'),
            (driver.btn_footer_3, 'Новости'),
            (driver.btn_footer_4, 'Вакансии'),
            (driver.btn_footer_5, 'Сотруднич'),
            (driver.btn_footer_6, 'Доставка для юр.лиц'),
            (driver.btn_footer_7, 'Поставщикам'),
            (driver.btn_footer_8, 'Рекламодателям'),
            (driver.btn_footer_9, 'Стать продавцом'),
            (driver.btn_footer_10, 'Продажа автомобилей'),
            (driver.btn_footer_11, 'Покупателям'),
            (driver.btn_footer_12, 'Пользовательское соглашение'),
            (driver.btn_footer_13, 'Вопрос-ответ'),
            (driver.btn_footer_14, 'Доставка и оплата'),
            (driver.btn_footer_15, 'Каталог'),
            (driver.btn_footer_16, 'Товары от магазина Emall'),
            (driver.btn_footer_17, 'Пункты выдачи'),
            (driver.btn_footer_18, 'Соглашение о кредитных ресурсах'),
            (driver.btn_footer_19, 'Наши друзья'),
            (driver.btn_footer_20, 'Едоставка'),
            (driver.btn_footer_21, 'Европочта'),
            (driver.btn_footer_22, 'Евроопт'),
            (driver.btn_footer_23, 'Хит!'),
            (driver.btn_footer_24, 'Грошык')
                    ]

        skip_click_check = ['Компания', 'Сотрудничество', "Покупателям", 'Наши друзья']

    with allure.step('Проверка элемента'):
        for element, text_element in elements:
            with allure.step(f'Проверка элемента {text_element} на отображение'):
                check.is_true(element.is_visible(), f'Элемента {text_element} нет визуально на экране')

            if text_element not in skip_click_check:
                with allure.step(f'Проверка элемента {text_element} на кликабельность'):
                    check.is_true(element.is_clickable(), f'Элемент {text_element} не кликабелен')

    with allure.step('Проверка брендов'):
        check.equal(driver.btn_brands.count(), 94)
