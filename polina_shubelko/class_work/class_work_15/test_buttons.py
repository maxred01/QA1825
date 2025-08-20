import time
import allure
from allure_commons.types import LabelType

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from QA1825.polina_shubelko.class_work.class_work_16.conftest import web_browser
from QA1825.polina_shubelko.class_work.class_work_16.locators.locators_button import LocatorsButton

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

def test_selenium_buttons(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = web_browser
        driver.get("https://demoqa.com/buttons")
        time.sleep(1)

    with allure.step ('Двойной клик'):
        elements_double_click_btn = driver.find_element(By.ID, LocatorsButton.double_click_btn)
        ActionChains(driver).double_click(elements_double_click_btn).perform()
        time.sleep(2)
        assert not driver.find_element(By.ID, LocatorsButton.double_click_message).is_displayed()

    with allure.step('Клик правой кнопкой мыши'):
        elements_right_click_btn = driver.find_element(By.ID, LocatorsButton.right_click_btn)
        ActionChains(driver).context_click(elements_right_click_btn).perform()
        time.sleep(2)

    with allure.step('Проверка текста: что текст выбран'):
        assert driver.find_element(By.ID, LocatorsButton.double_click_message).text.find
        assert driver.find_element(By.ID, LocatorsButton.double_click_message).text.find

    time.sleep(2)
    driver.quit()
