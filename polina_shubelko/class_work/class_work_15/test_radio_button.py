import time
import allure
from allure_commons.types import LabelType

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pytest_check as check

@allure.title('Это тест проверяет радиобаттон')
@allure.description("""Тест нажимает по каждой кнопке и проверяет выбран ли радиобатон или нет""")
@allure.tag("Smoke")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("123")
@allure.manual
@allure.link("https://hoster.by/", name="Тест-кейсы теста")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@allure.epic("UI автотетсы")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Radio Button")

def test_selenium_radio_button():
    with allure.step('Запускаем и настройка браузер'):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/radio-button")
        driver.maximize_window()
        driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(1)

    with allure.step('Прожатие кнопок для открытие вкладок'):
        driver.find_element(By.CSS_SELECTOR, 'label[for="yesRadio"]').click()
        check.is_true (driver.find_element(By.ID, 'yesRadio').is_selected(), 'ожидалось: что кнопка будет активной')
        check.is_false (driver.find_element(By.ID, 'noRadio').is_enabled(), 'ожидалось: что кнопка будет активной')

        driver.quit()
