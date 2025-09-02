import time
import allure
from allure_commons.types import Severity, LabelType

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pytest_check as check
from torch.fx.experimental.unification.unification_tools import first


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
@allure.story("Вкладка Check Box")

def test_selenium():
    with allure.step('Подготовка тестовых данных'):
        first_name = 'Kira'
        last_name = 'Maccoll'
        age = 52
        email = 'kira@gmail.com'
        salary = 13000
        department = 'Legal'

    with allure.step('Запускаем и настраеваем Браузер'):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/webtables")
        driver.maximize_window()
    time.sleep(1)

    with allure.step('удаление элемента'):
       elements = driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]')
       len(elements)
       driver.find_element(By.ID, 'delete-record-1').click()
       elements_delete = driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]')
       check.not_equal(elements,elements_delete)

    with allure.step('добавление элемента'):
       elements = driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]')
       len(elements)
       driver.find_element(By.ID, 'addNewRecordButton').click()
       elemets_form_send_keys = [
           (driver.find_element(By.ID, 'firstName'), 'First Name', first_name),
           (driver.find_element(By.ID, 'lastName'), 'Last Name', last_name),
           (driver.find_element(By.ID, 'userEmail'), 'Email', email),
           (driver.find_element(By.ID, 'age'), 'Age', age),
           (driver.find_element(By.ID, 'salary'), 'Salary', salary),
           (driver.find_element(By.ID, 'department'), 'Department', department)
       ]
       driver.find_element(By.ID, 'submit').click()

       elements_delete = driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]')
       check.not_equal(elements,elements_delete)



    time.sleep(2)
    driver.quit()