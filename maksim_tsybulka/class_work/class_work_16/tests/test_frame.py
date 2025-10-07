from maksim_tsybulka.class_work.class_work_16.locators.main_locators import MainPage
import pytest_check as check
import allure
from super_puper_frame.conftest import web_browser
from super_puper_frame.conftest import chrome_options


@allure.feature("Главная страница")
@allure.story("Хедер")
def test_headers(web_browser, chrome_options):
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
