import time

import allure
from allure_commons.types import Severity, LabelType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pytest_check as check

@allure.title("Этот тест проверяет заполнение формы")
@allure.description("""Тест вводит поля""")
@allure.tag("Smoky")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("123")
@allure.manual
@allure.link("https://hoster.by/", name="Тест-кейсы теста")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@allure.epic("UI автотесты")
@allure.feature("раздел Elements")
@allure.story("Вкладка Test Box")


def test_selenium():

    with allure.step('Подготовка тестовых данных'):
        user_name = 'tri-kota'
        user_email = 'test@gmail.com'
        current_address = 'test currentAddress'
        permanent_address = 'test permanentAddress'

    with allure.step('Запуск и настройка браузера'):
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
#       with allure.step(f'Ввод текста для поля {text_element}'):
            element.send_keys(send_keys_element)

    time.sleep(2)
    with allure.step('Скролл страницы вниз'):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # driver.execute_script("window.scrollBy(0, 50);")    # driver.find_element(By.ID, 'submit').send_keys(Keys.DOWN)    driver.find_element(By.ID, 'submit').click()
    output_form = driver.find_element(By.ID, 'output')

    assert output_form.is_displayed(), 'Результат формы не появился на экарне'
    elemets_form = [
        (driver.find_element(By.ID, 'name'), user_name, 'Name'),
        (driver.find_element(By.ID, 'email'), user_email, 'Email'),
        (driver.find_element(By.XPATH, '//p[@id="currentAddress"]'), current_address, 'Current Address'),
        (driver.find_element(By.XPATH, '//p[@id="permanentAddress"]'), permanent_address, 'Permanent Address')
    ]
    for elemet, elemets_text in elemets_form:
        check.greater(elemet.text.find(elemets_text), -1, f"Текста {elemets_text} нет на экране")

    time.sleep(2)
    driver.quit()