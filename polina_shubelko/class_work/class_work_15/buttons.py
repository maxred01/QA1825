import time
import allure
from allure_commons.types import LabelType

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pytest_check as check

@allure.title('Это тест проверяет баттон')
@allure.description("""Тест нажимает по каждой кнопке и проверяет баттон""")
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
@allure.story("Вкладка Buttons")

def test_selenium_buttons():
    with allure.step('Запускаем и настройка браузер'):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/buttons")
        driver.maximize_window()
        driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(1)

    with allure.step ('Двойной клик'):
        elements_double_click_btn = driver.find_element(By.XPATH, '//*[@id="doubleClickBtn"]')
        ActionChains(driver).double_click(elements_double_click_btn).perform()
        time.sleep(2)

    with allure.step('Клик правой кнопкой мыши'):
        elements_right_click_btn = driver.find_element(By.XPATH, '//*[@id="rightClickBtn"]')
        ActionChains(driver).context_click(elements_right_click_btn).perform()
        time.sleep(2)

    with allure.step('Проверка текста: что текст выбран'):
        assert driver.find_element(By.XPATH, '//*[@id="doubleClickMessage"]').text.find
        assert driver.find_element(By.XPATH, '//*[@id="rightClickMessage"]').text.find

    time.sleep(2)
    driver.quit()
