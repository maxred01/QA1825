import time

import allure
from allure_commons.types import Severity, LabelType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bachko_irina.class_work.class_work_12.conftest import web_browser
import pytest_check as check
from bachko_irina.class_work.class_work_12.locators.locators_buttons import LocatorsButton

@allure.feature("раздел Elements")
@allure.story("Вкладка upload-download")
def test_upload_download():
    with allure.step('Запуск и настройка браузера'):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/upload-download")
        driver.maximize_window()

    with allure.step('Загрузка файла'):
        driver.find_element(By.ID, 'uploadFile').send_keys('C:\\Users\\Irina\\Desktop\\def_7.txt')
        time.sleep(2)

@allure.feature("раздел Elements")
@allure.story("Вкладка upload-download")
def test_buttons(web_browser):
        with allure.step('Запуск и настройка браузера'):
            driver = web_browser
            driver.get("https://demoqa.com/buttons")

        with allure.step('Двойной клик'):
            elements_double_click_btn = driver.find_element(By.ID, LocatorsButton.double_click_btn)
            ActionChains(driver).double_click(elements_double_click_btn).perform()
            time.sleep(2)
            assert not driver.find_element(By.ID, LocatorsButton.double_click_message).is_displayed()


        with allure.step('Клик правой кнопкой мыши'):
            elements_right_click_btn = driver.find_element(By.ID, LocatorsButton.right_click_btn)
            ActionChains(driver).context_click(elements_right_click_btn).perform()
            time.sleep(2)

time.sleep(2)



