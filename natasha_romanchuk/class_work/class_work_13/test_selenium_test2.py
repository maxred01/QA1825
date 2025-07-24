import time
import allure
from allure_commons.types import LabelType

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pytest_check as check

@allure.title("Этот тест проверяет заполнение и результат заполнения формы")
@allure.description("""Тест вводит текст для полей user_name и тд и сверяет результат в полях name и тд""")
@allure.tag("Smoke")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("123")
@allure.manual
@allure.link("https://hoster.by/", name="Тест-кейсы теста")
@allure.issue("AUTH-123")
@allure.epic("UI автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Test Box")

def test_selenium():

    with allure.step('Подготовка тестовых даных'):
        user_name = 'Nata'
        user_email = 'nata@gmail.com'
        current_address = 'Minsk'
        permanent_address = 'Brest'

    with allure.step('Запускаем и настраиваем браузер'):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/text-box")
        driver.maximize_window()
    time.sleep(1)

    elemets_form_send_keys = [
        (driver.find_element(By.ID, 'userName'), 'Full Name', user_name),
        (driver.find_element(By.ID, 'userEmail'), 'Email', user_email),
        (driver.find_element(By.ID, 'currentAddress'), 'Current Address', current_address),
        (driver.find_element(By.ID, 'permanentAddress'), 'Permanent Address', permanent_address)
    ]
    for element, text_elemet, send_keys_element in elemets_form_send_keys:
        element.send_keys(send_keys_element)

    time.sleep(2)
    with allure.step('Скролл страницы вниз'):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    with allure.step('Нажатие на кнопку "submit"'):
        driver.find_element(By.ID, 'submit').click()

    elemets_form = [
         (driver.find_element(By.ID, 'name'), user_name, 'Name'),
         (driver.find_element(By.ID, 'email'), user_email, 'Email'),
         (driver.find_element(By.XPATH, '//p[@id="currentAddress"]'), current_address, 'Current Address'),
         (driver.find_element(By.XPATH, '//p[@id="permanentAddress"]'), permanent_address, 'Permanent Address')
    ]
    for element, elemets_text, name_form in elemets_form:
        with allure.step(f'Проверка поля, {name_form}'):
            check.greater(element.text.find(elemets_text), -1, f"Текста {elemets_text} нет на экране")

    time.sleep(2)
    driver.quit()


