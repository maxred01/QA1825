import time
import allure
from nastya_kuprianchik.class_work.class_work14.locators.main_locators import MainPage
import pytest_check as check


@allure.feature('Главная страница')
@allure.story("Header")
def test_header(web_browser):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(10)
        driver.btn_dialog.click()

    with allure.step('Подготовка тестовых данных'):
        elements = [
            (driver.btn_header1, 'Главная'),
            (driver.btn_header2, 'Группа'),
            (driver.btn_header3, 'Опубликовать пост!'),
            (driver.btn_header4, 'Уведомления'),
            (driver.btn_header5, 'Аккаунт')
        ]
    with allure.step('Проверка элемента'):
        for element, text_element in elements:
            with allure.step(f'Проверка элемента {text_element} на кликабельность'):
                check.is_true(element.is_clickable(), f'Элемента {text_element} не кликабелен')


@allure.feature('Главная страница')
@allure.story("Footer")
def test_footer(web_browser):
    with allure.step('Звпускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(2)#?
        driver.bt14.click()#?

    with allure.step('Подготовка тестовых данных'):
        elements = [
            (driver.btn_footer1, 'Контакты'),
            (driver.btn_footer2, 'Политика'),
            (driver.btn_footer3, 'Условия'),
            (driver.btn_footer4, 'Политика учетной записи'),
            (driver.btn_footer5, 'Условия учетной записи'),
            (driver.btn_footer6, 'Правила сообщества'),
            (driver.btn_footer7, 'Правила сообщества')
        ]
    with allure.step('Проверка элемента'):
        for element, text_element in elements:
            with allure.step(f'Проверка элемента {text_element} на отображение'):
                check.is_true(element.is_visible(), f'Элемента {text_element} нет визуально на экарне')

            with allure.step(f'Проверка элемента {text_element} на кликабельность'):
                check.is_true(element.is_clickable(), f'Элемента {text_element} не кликабелен')