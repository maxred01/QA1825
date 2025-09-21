import time
import allure
import uuid


from Valery_Hehenia.Class_work.Class_work_18.locators.locators_main_page import MainPage
from das_magaz.conftest import webdriver
from das_magaz.conftest import chrome_options, web_browser
import pytest_check as check
from allure_commons.types import LabelType



def generate_random_user():
    username = f"user_{uuid.uuid4().hex[:6]}"
    password = f"pass_{uuid.uuid4().hex[:8]}"
    return username, password


@allure.feature("Регистрация")
@allure.story("Регистрация с пустыми полями")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/fKiXRvsE/2-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D1%81-%D0%BF%D1%83%D1%81%D1%82%D1%8B%D0%BC%D0%B8-%D0%BF%D0%BE%D0%BB%D1%8F%D0%BC%D0%B8", "РА-002")
def test_register_empty_field(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)

    with (allure.step('Подготовка тестовых данных')):
        username = ''
        password = ''

    with allure.step('Регистрация'):

        with allure.step('Нажатие кнопки Sign up'):
            driver.sugnup_btn.click()
            time.sleep(1)
        with allure.step('Заполнение тестовых данных'):
            driver.signup_username.send_keys(username)
            driver.signup_password.send_keys(password)
        with allure.step('Нажатие кнопки Sign up'):
            driver.btn_signup_confirm.click()
            time.sleep(1)
    with allure.step('Проверка на корректное поведение системы'):
        alert = web_browser.switch_to.alert
        assert "Please fill out Username and Password." in alert.text
        alert.accept()


@allure.feature("Регистрация")
@allure.story("Регистрация с пустым полем Пароль")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/D7VkSLnt/3-%D1%80%D0%B0-3-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D1%81-%D0%BF%D1%83%D1%81%D1%82%D1%8B%D0%BC-%D0%BF%D0%BE%D0%BB%D0%B5%D0%BC-%D0%BF%D0%B0%D1%80%D0%BE%D0%BB%D1%8C", "РА-003")
def test_register_no_password(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)

    with (allure.step('Подготовка тестовых данных')):
        username, password= generate_random_user()
        password = ''

    with allure.step('Регистрация'):

        with allure.step('Нажатие кнопки Sign up'):
            driver.sugnup_btn.click()
            time.sleep(1)
        with allure.step('Заполнение тестовых данных'):
            driver.signup_username.send_keys(username)
            driver.signup_password.send_keys(password)
        with allure.step('Нажатие кнопки Sign up'):
            driver.btn_signup_confirm.click()
            time.sleep(1)
    with allure.step('Проверка на корректное поведение системы'):
        alert = web_browser.switch_to.alert
        assert "Please fill out Username and Password." in alert.text
        alert.accept()



@allure.feature("Регистрация")
@allure.story("Регистрация с пустым полем Логин")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/FLKFDjYR/4-%D1%80%D0%B0-004-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D1%81-%D0%BF%D1%83%D1%81%D1%82%D1%8B%D0%BC-%D0%BF%D0%BE%D0%BB%D0%B5%D0%BC-%D0%BB%D0%BE%D0%B3%D0%B8%D0%BD", "РА-004")
def test_register_no_login(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)

    with (allure.step('Подготовка тестовых данных')):
        username, password= generate_random_user()
        username = ''

    with allure.step('Регистрация'):

        with allure.step('Нажатие кнопки Sign up'):
            driver.sugnup_btn.click()
            time.sleep(1)
        with allure.step('Заполнение тестовых данных'):
            driver.signup_username.send_keys(username)
            driver.signup_password.send_keys(password)
        with allure.step('Нажатие кнопки Sign up'):
            driver.btn_signup_confirm.click()
            time.sleep(1)
    with allure.step('Проверка на корректное поведение системы'):
        alert = web_browser.switch_to.alert
        assert "Please fill out Username and Password." in alert.text
        alert.accept()



@allure.feature("Регистрация")
@allure.story("Регистраиция: ввод 50 символов")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/USqer7zf/5-%D1%80%D0%B0-5-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D0%B8%D1%86%D0%B8%D1%8F-%D0%B2%D0%B2%D0%BE%D0%B4-50-%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D0%BE%D0%B2", "РА-005")
def test_register_fifty_symbol(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)

    with (allure.step('Подготовка тестовых данных')):
        username = f"{uuid.uuid4().hex[:50]}"
        password = f"{uuid.uuid4().hex[:50]}"

    with allure.step('Регистрация'):

        with allure.step('Нажатие кнопки Sign up'):
            driver.sugnup_btn.click()
            time.sleep(1)
        with allure.step('Заполнение тестовых данных'):
            driver.signup_username.send_keys(username)
            driver.signup_password.send_keys(password)
        with allure.step('Нажатие кнопки Sign up'):
            driver.btn_signup_confirm.click()
            time.sleep(1)
    with (allure.step('Проверка на корректное поведение системы')):
        alert = web_browser.switch_to.alert
        assert "Please fill out Username and Password." in alert.text
        alert.accept()




@allure.feature("Регистрация")
@allure.story("Регистрация: использование спец символов")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/M99vsAD0/6-%D1%80%D0%B0-6-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D0%BF%D0%B5%D1%86-%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D0%BE%D0%B2", "РА-006")
def test_register_spec_symbol(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)

    with (allure.step('Подготовка тестовых данных')):
        username = '“№;%;%:?*'
        password = '“№;%;%:?*'

    with allure.step('Регистрация'):

        with allure.step('Нажатие кнопки Sign up'):
            driver.sugnup_btn.click()
            time.sleep(1)
        with allure.step('Заполнение тестовых данных'):
            driver.signup_username.send_keys(username)
            driver.signup_password.send_keys(password)
        with allure.step('Нажатие кнопки Sign up'):
            driver.btn_signup_confirm.click()
            time.sleep(1)
    with allure.step('Проверка на корректное поведение системы'):
        alert = web_browser.switch_to.alert
        assert "Please fill out Username and Password." in alert.text
        alert.accept()