import time
import allure
import uuid


from Valery_Hehenia.Class_work.Class_work_18.locators.locators_main_page import MainPage
from das_magaz.conftest import webdriver
from das_magaz.conftest import chrome_options, web_browser
import pytest_check as check




def generate_random_user():
    username = f"user_{uuid.uuid4().hex[:6]}"
    password = f"pass_{uuid.uuid4().hex[:8]}"
    return username, password


@allure.feature("Авторизация")
@allure.story("Логин пользователя")
def test_register_and_login_and_logout(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)

    with allure.step('Генерация тестовых данных'):
        username, password = generate_random_user()

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
    with allure.step('Проверка успешной регистрации'):
        alert = web_browser.switch_to.alert
        assert "Sign up successful" in alert.text
        alert.accept()



    with allure.step('Авторизация'):
        with allure.step('Нажатие кнопки Log in'):
            driver.login_btn.click()
            time.sleep(1)
        with allure.step('Заполнение тестовых данных'):
            driver.login_username.send_keys(username)
            driver.login_password.send_keys(password)
        with allure.step('Нажатие кнопки Log in'):
            driver.btn_login_confirm.click()
            time.sleep(2)

    with allure.step('Проверка успешного входа'):
        expected_text = f"Welcome {username}"
        time.sleep(1)
        actual_text = driver.nameofuser_btn.get_attribute("innerText")
        check.equal(actual_text, expected_text, f"Ожидалось '{expected_text}', но получили '{actual_text}'")

    with allure.step('Проверка успешного выхода из учетной записи'):
        driver.logout_btn.click()
        time.sleep(1)
        check.is_false(driver.nameofuser_btn.is_visible(), "Элемент с именем пользователя всё ещё виден после выхода")
        check.is_true(driver.login_btn.is_visible(), "Кнопка 'Log in' не видна после выхода")