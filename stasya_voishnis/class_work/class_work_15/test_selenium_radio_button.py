import time
import allure
from allure_commons.types import Severity, LabelType

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
@allure.story("Вкладка Check Box")

def test_selenium():

    with allure.step('Запускаем и настраеваем Браузер'):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/radio-button")
        driver.maximize_window()
    time.sleep(1)

    with allure.step('Cкролл страницы вниз'):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    with allure.step('Нажать Yes'):
        driver.find_element(By.XPATH, '(//label[@class="custom-control-label"])[1]').click()
        check.is_true(driver.find_element(By.ID, 'yesRadio').is_selected(),'Ожидалось: что кнопка будет активной')
        check.is_true(driver.find_element(By.XPATH, '//span[@class="text-success"]').text.find('Yes') > -1,'Ожидалось в сообщении"Yes"')

    with allure.step('Нажать Impressive'):
        driver.find_element(By.XPATH, '(//label[@class="custom-control-label"])[2]').click()
        check.is_true(driver.find_element(By.ID, 'impressiveRadio').is_selected(),'Ожидалось: что кнопка будет активной')
        check.is_true(driver.find_element(By.XPATH, '//span[@class="text-success"]').text.find('Impressive') > -1,'Ожидалось в сообщении"Impressive"')

    with allure.step('Нажать No'):
        driver.find_element(By.XPATH, '(//label[@class="custom-control-label"])[2]').click()
        check.is_false(driver.find_element(By.ID, 'noRadio').is_enabled(), 'Ожидалось: что кнопка будет не активной')

    time.sleep(2)
    driver.quit()