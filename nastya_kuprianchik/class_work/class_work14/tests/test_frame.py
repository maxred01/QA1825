from bsuir.page.base_page import WebPage
from bsuir.page.elements import ManyWebElements
from bsuir.tests.conftest import chrome_options
from bsuir.locators.main_locators import MainPage
import time
import allure
from pytest_check import check
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

@allure.feature('Главная страница')
@allure.story("Header")
def test_header(web_browser,chrome_options):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click(20)
            driver.btn_sel.click()



    with allure.step('Подготовка тестовых данных'):
        elements = [
            (driver.btn_gl, 'Главная'),
            (driver.btn_gr, 'Группа'),
            (driver.btn_pub, 'Опубликовать пост!'),
            (driver.btn_uv, 'Уведомления'),
            (driver.btn_akk, 'Аккаунт')
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