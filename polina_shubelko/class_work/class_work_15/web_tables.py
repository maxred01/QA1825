import time
import allure
from allure_commons.types import LabelType

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


def test_selenium_web_tables():
    with allure.step('Запускаем и настраиваем браузер'):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/webtables")
        driver.maximize_window()
        driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(2)

    with allure.step('Проверка удаление записи'):
        elements = driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]')
        driver.find_element(By.CSS_SELECTOR, 'span[title="Delete"]').click()
        elements_delete = driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]')
        time.sleep(3)
        check.not_equal(elements, elements_delete)
        time.sleep(2)

    with allure.step('Проверка добавление записи'):
        driver.find_element(By.XPATH, '//button[@id="addNewRecordButton"]').click()

        First_Name = 'Pavel'
        Last_Name = 'Post'
        Email = 'pavel.post@example.com'
        Age = '33'
        Salary = '50000'
        Department = 'IT'

        elements_form_send_keys = [
            (driver.find_element(By.XPATH, '//input[@placeholder="First Name"]'), 'First Name', First_Name),
            (driver.find_element(By.XPATH, '//input[@placeholder="Last Name"]'), 'Last Name', Last_Name),
            (driver.find_element(By.XPATH, '//input[@placeholder="name@example.com"]'), 'Email', Email),
            (driver.find_element(By.XPATH, '//input[@pattern="\d*"]'), 'Age', Age),
            (driver.find_element(By.XPATH, '//input[@placeholder="Salary"]'), 'Salary', Salary),
            (driver.find_element(By.XPATH, '//input[@placeholder="Department"]'), 'Department', Department)

        ]
        for element, name_form, input_value in elements_form_send_keys:
            with allure.step(f'Заполнение поля {name_form}'):
                element.clear()
                element.send_keys(input_value)
                time.sleep(2)
            with allure.step(f'Проверка текста в поле {name_form}'):
                text_in_element = element.get_attribute('value')
                index = text_in_element.find(input_value)
                check.greater(index, -1, f"Текста {input_value} нет в поле {name_form}")
                time.sleep(2)

                driver.find_element(By.XPATH, '// button[ @ id = "submit"]').click()

    with allure.step('Проверка редактирования записи'):
        elements_before = driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]')
        driver.find_element(By.CSS_SELECTOR, 'span[title="Edit"]').click()
        time.sleep(3)
        elements_after = driver.find_elements(By.CSS_SELECTOR, 'span[title="Edit"]')
        check.not_equal(elements_before, elements_after)
        time.sleep(2)

        First_Name = 'Tom'
        Last_Name = 'Trast'
        Email = 'tom.trast@example.com'
        Age = '27'
        Salary = '70000'
        Department = 'HR'

        elements_form_send_keys = [
            (driver.find_element(By.XPATH, '//input[@placeholder="First Name"]'), 'First Name', First_Name),
            (driver.find_element(By.XPATH, '//input[@placeholder="Last Name"]'), 'Last Name', Last_Name),
            (driver.find_element(By.XPATH, '//input[@placeholder="name@example.com"]'), 'Email', Email),
            (driver.find_element(By.XPATH, '//input[@pattern="\d*"]'), 'Age', Age),
            (driver.find_element(By.XPATH, '//input[@placeholder="Salary"]'), 'Salary', Salary),
            (driver.find_element(By.XPATH, '//input[@placeholder="Department"]'), 'Department', Department)

        ]

        for locator, name_form, input_value in elements_form_send_keys:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.clear()
            element.send_keys(input_value)
            time.sleep(2)

        with allure.step(f'Проверка текста в поле {name_form}'):
                text_in_element = element.get_attribute('value')
                index = text_in_element.find(input_value)
                check.greater(index, -1, f"Текста {input_value} нет в поле {name_form}")
                time.sleep(2)

                driver.find_element(By.XPATH, '// button[ @ id = "submit"]').click()


        time.sleep(2)
        driver.quit()