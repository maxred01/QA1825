import time

import allure
from allure_commons.types import Severity, LabelType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bachko_irina.class_work_7.conftest import web_browser
import pytest_check as check
from bachko_irina.class_work_7.locators.locators_buttons import LocatorsButton

@allure.feature("Heder")
@allure.story("logo_Heder")
def test_heder_logo(web_browser):
    with allure.step('Запуск и настройка браузера'):
        driver = web_browser
        driver.get("https://www.spacex.com/")

    with allure.step('Отображение логотипа'):
        driver.find_element(By.XPATH, LocatorsButton.logo)
        time.sleep(2)

@allure.feature("раздел Elements")
@allure.story("Вкладка upload-download")
def test_buttons(web_browser):
        with allure.step('Запуск и настройка браузера'):
            driver = web_browser
            driver.get("https://demoqa.com/buttons")

driver.get("https://shop.spacex.com")
driver.maximize_window()
driver.find_element(By.XPATH,  '//button[@class="Heading Link Link--primary Text--subdued u-h8"]').click()

driver.find_element(By.XPATH, '//input[@id="search-input"]').send_keys('abc')



time.sleep(5)

# Закрыть браузер
driver.quit()

time.sleep(2)



