import time
import allure
from allure_commons.types import LabelType

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pytest_check as check

@allure.title('Это тест проверяет форму')
@allure.description("""Тест проверяет редактирование и удаление""")
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
@allure.story("Вкладка Web Tables")

def test_selenium_is_selected():
    with allure.step('Запускаем и настраиваем браузер'):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/webtables")
        driver.maximize_window()
        driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(2)

    with allure.step('Нажатие кнопок для открытия вкладок'):
        elements = driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]')
        driver.find_element(By.CSS_SELECTOR, 'span[title="Delete"]').click()
        elements_delete = driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]')
        time.sleep(3)
        check.not_equal(elements, elements_delete)
        driver.quit()


