import time
import allure
from allure_commons.types import LabelType

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pytest_check as check

@allure.title('Это тест проверяет загрузку')
@allure.description("""Тест проверяет загрузку файла""")
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
@allure.story("Вкладка Upload and Download")

def test_selenium_buttons():
    with allure.step('Запускаем и настройка браузер'):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/upload-download")
        driver.maximize_window()
        driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(1)

    with allure.step ('Загрузка файла'):
        driver.find_element(By.XPATH, '// input[ @ id = "uploadFile"]').send_keys("C:\\Users\\Polina\\Pictures\\Фоновые изображения рабочего стола\\2. Хаски.jpg")
        time.sleep(1)

        driver.quit()