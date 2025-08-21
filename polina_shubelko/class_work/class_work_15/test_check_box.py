import time
import allure
from allure_commons.types import Severity
from allure_commons.types import LabelType

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pytest_check as check

@allure.title('Это тест проверяет чекбоксы')
@allure.description("""Тест нажимает на вложенности и прожимает чекбоксы""")
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("123")
@allure.manual
@allure.link("https://hoster.by/", name="Тест-кейсы теста")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@allure.epic("UI автотетсы")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Check Box")


def test_selenium_check_box():
    with allure.step('Запускаем и настраиваем браузер'):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/checkbox")
        driver.maximize_window()
        driver.execute_script("window.scrollBy(0, 250);")
        time.sleep(2)

    with allure.step('Нажатие кнопок для открытия вкладок'):
        driver.find_element(By.XPATH, '(//*[@aria-label="Toggle"])[1]//*[@stroke="currentColor"]').click()
        driver.find_element(By.XPATH, '(//*[@aria-label="Toggle"])[4]/*[1]').click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Word File.doc')]").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Excel File.doc')]").click()

    with allure.step('Проверка: что нажаты чекбоксы'):
        assert driver.find_element(By.XPATH, '//input[@id="tree-node-wordFile"]').is_selected()
        assert driver.find_element(By.XPATH, '//input[@id="tree-node-excelFile"]').is_selected()

    with allure.step('Проверка текста: что текст выбран'):
        assert driver.find_element(By.ID,"result").text.find('downloads') > -1
        assert driver.find_element(By.ID,"result").text.find('wordFile') > -1
        assert driver.find_element(By.ID,"result").text.find('excelFile') > -1

    time.sleep(2)
    driver.quit()





