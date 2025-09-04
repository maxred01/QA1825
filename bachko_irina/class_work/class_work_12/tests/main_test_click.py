import time
import allure
from selenium.webdriver.support.expected_conditions import element_located_selection_state_to_be

from bachko_irina.class_work.class_work_12.locators.main_locators import MainPage
import pytest_check as check

@allure.feature("раздел Elements")
@allure.story("Header")
def test_heders(web_browser):
    with allure.step('Запуск и настройка браузера'):
        driver = MainPage(web_browser)


    with allure.step('Подготовка тестовых данных'):
        elements = [
            (driver.Logo, 'spacex-logo'),
            (driver.Vehicles, 'Vehicles'),
            (driver.Launches,'Launches'),
            (driver.HumanSpaceflight,'Human Spaceflight'),
            (driver.Rideshare,'Rideshare'),
            (driver.Starlink,'Starlink'),
            (driver.Starshield,'Starshield'),
            (driver.Company,'Company'),
            (driver.Shop,'Shop'),

            ]

    with allure.step('Проверка элемента'):
        for element, text_element in elements:
            with allure.step(f'Проверка элемента {text_element} на отображение'):
                check.is_true(element.is_visible(), f'Элемента {text_element} нет визуально на экарне')

            with allure.step(f'Проверка элемента {text_element} на кликабельность'):
                check.is_true(element.is_clickable(), f'Элемента {text_element} не кликабелен')

@allure.feature("Главная страница")
@allure.story("Footer")
def test_footers(web_browser):
    with allure.step('Запускаем и настройка браузер'):
            driver = MainPage(web_browser)

    with allure.step('Подготовка тестовых данных'):
            elements = [
                (driver.Vehicles, 'Vehicles'),
                (driver.Careers, 'Careers'),
                (driver.Updates, 'Updates'),
                (driver.Privacy, 'Privacy'),
                (driver.Policy, 'Policy'),
                (driver.Suppliers, 'Suppliers'),
            ]

    with allure.step('Проверка элемента'):
        for element, text_element in elements:
            with allure.step(f'Проверка элемента {text_element} на отображение'):
                    check.is_true(element.is_visible(), f'Элемента {text_element} нет визуально на экарне')

            with allure.step(f'Проверка элемента {text_element} на кликабельность'):
                    check.is_true(element.is_clickable(), f'Элемента {text_element} не кликабелен')



