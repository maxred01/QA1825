import time

import allure
from allure_commons.types import Severity, LabelType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.devtools.v136.dom import get_attributes
from selenium.webdriver.common.devtools.v136.log import clear
from selenium.webdriver.common.keys import Keys
from bachko_irina.class_work_7.conftest import web_browser
import pytest_check as check
from bachko_irina.class_work_7.locators.locators_buttons import LocatorsButton

@allure.feature("Heder")
@allure.story("logo_Heder")
def test_heder_logo(web_browser):
    with allure.step('Запуск и настройка браузера'):
        driver = web_browser
        driver.get("https://spacex.com/")

    with allure.step('Отображение логотипа'):
        logo = driver.find_element(By.XPATH, LocatorsButton.logo)
        assert logo.is_displayd()
        time.sleep(2)

@allure.feature("Heder")
@allure.story("Search_Heder")
def test_heder_search(web_browser):
    with allure.step('Запуск и настройка браузера'):
        driver = web_browser
        driver.get("https://spacex.com")

    with allure.step('Проверка строки поиска'):
        search = driver.find_element(By.XPATH, LocatorsButton.shop)
        assert search.is_displayd()
        driver.find_element(By.XPATH, LocatorsButton.search).click()
        enter_fild = driver.find_element(By.XPATH, '//input[@id="search-input"]').send_keys('abc')
        print(enter_fild, get_attributes("abc"))
        time.sleep(2)
        enter_fild = clear()
        enter_fild = driver.find_element(By.XPATH, '//input[@id="search-input"]').send_keys('shits')


time.sleep(5)

# Закрыть браузер
driver.quit()





