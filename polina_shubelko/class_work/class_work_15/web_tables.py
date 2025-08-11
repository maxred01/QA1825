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


def test_selenium_web_tables_1():

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
        time.sleep(2)
        check.not_equal(elements, elements_delete)
        time.sleep(2)

def test_selenium_web_tables_2():

    with allure.step('Запускаем и настраиваем браузер'):
            driver = webdriver.Chrome()
            driver.get("https://demoqa.com/webtables")
            driver.maximize_window()
            driver.execute_script("window.scrollBy(0, 200);")
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

            with allure.step(f'Проверка текста в поле {name_form}'):
                text_in_element = element.get_attribute('value')
                index = text_in_element.find(input_value)
                check.greater(index, -1, f"Текста {input_value} нет в поле {name_form}")
                time.sleep(1)

                driver.find_element(By.XPATH, '// button[ @ id = "submit"]').click()

    time.sleep(2)

def test_selenium_web_tables_3():

    with allure.step('Запускаем и настраиваем браузер'):
            driver = webdriver.Chrome()
            driver.get("https://demoqa.com/webtables")
            driver.maximize_window()
            driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(2)

    with allure.step('Проверка редактирования записи'):
        elements_before = driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]')
        driver.find_element(By.CSS_SELECTOR, 'span[title="Edit"]').click()
        time.sleep(2)
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
            time.sleep(1)

        with allure.step(f'Проверка текста в поле {name_form}'):
                text_in_element = element.get_attribute('value')
                index = text_in_element.find(input_value)
                check.greater(index, -1, f"Текста {input_value} нет в поле {name_form}")

                driver.find_element(By.XPATH, '// button[ @ id = "submit"]').click()
                time.sleep(2)

def test_selenium_web_tables_4():

    with allure.step('Запускаем и настраиваем браузер'):
            driver = webdriver.Chrome()
            driver.get("https://demoqa.com/webtables")
            driver.maximize_window()
            driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(2)

    with allure.step('Проверка поля "Search"'):
        element = driver.find_element(By.XPATH, '//input[@id="searchBox"]')
        element.send_keys("Kierra")
        time.sleep(2)

        with allure.step('Проверка текста: что текст найден'):
            assert driver.find_element(By.XPATH, '(//*[@role="gridcell"])[15]').text.find('Kierra')
        time.sleep(2)
        element.clear()
        time.sleep(2)

        element = driver.find_element(By.XPATH, '//input[@id="searchBox"]')
        element.send_keys("Polina")
        time.sleep(2)

        with allure.step('Проверка текста: что текст не найден'):
            assert driver.find_element(By.XPATH, '//div[@class="ReactTable -striped -highlight"]')
        time.sleep(2)
        element.clear()
        time.sleep(2)

def test_selenium_web_tables_5():

    with allure.step('Запускаем и настраиваем браузер'):
            driver = webdriver.Chrome()
            driver.get("https://demoqa.com/webtables")
            driver.maximize_window()
            driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(2)

    with allure.step('Проверка пагинации'):
        for _ in range(10):
            driver.find_element(By.XPATH, '//button[@id="addNewRecordButton"]').click()

            First_Name = 'Ron'
            Last_Name = 'Rew'
            Email = 'ron.rew@example.com'
            Age = '48'
            Salary = '82000'
            Department = 'Support'

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

                with allure.step(f'Проверка текста в поле {name_form}'):
                    text_in_element = element.get_attribute('value')
                    index = text_in_element.find(input_value)
                    check.greater(index, -1, f"Текста {input_value} нет в поле {name_form}")

                    driver.find_element(By.XPATH, '// button[ @ id = "submit"]').click()

    time.sleep(2)
    with allure.step('Проверка, что номер страницы изменился'):
        assert driver.find_element(By.XPATH, '//div[@class="ReactTable -striped -highlight"]').text.find

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        driver.find_element(By.XPATH, '(//*[@type="button"])[4]').click()
        time.sleep(2)

        assert driver.find_element(By.XPATH, '//input[@aria-label="jump to page"]'), 'value = "2"'
        driver.find_element(By.XPATH, '(//*[@type="button"])[3]').click()
        time.sleep(2)
        assert driver.find_element(By.XPATH, '//input[@aria-label="jump to page"]'), 'value = "1"'
        time.sleep(2)

def test_selenium_web_tables_6():

    with allure.step('Запускаем и настраиваем браузер'):
            driver = webdriver.Chrome()
            driver.get("https://demoqa.com/webtables")
            driver.maximize_window()
            driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(2)

    with allure.step('Проверка поля "First Name"'):
        driver.find_element(By.XPATH, '//button[@id="addNewRecordButton"]').click()
        first_name_input = driver.find_element(By.XPATH, '//input[@placeholder="First Name"]')

        long_input = 'a' * 26
        first_name_input.clear()
        first_name_input.send_keys(long_input)
        time.sleep(1)

        current_value = first_name_input.get_attribute('value')

        print(f"Введено символов: {len(current_value)}")
        assert len(current_value) <= 25, f"Длина введенного текста {len(current_value)} превышает допустимый лимит"
        time.sleep(1)

def test_selenium_web_tables_7():

    with allure.step('Запускаем и настраиваем браузер'):
            driver = webdriver.Chrome()
            driver.get("https://demoqa.com/webtables")
            driver.maximize_window()
            driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(2)

    with allure.step('Проверка поля "Last Name"'):
        driver.find_element(By.XPATH, '//button[@id="addNewRecordButton"]').click()
        last_name_input = driver.find_element(By.XPATH, '//input[@placeholder="Last Name"]')

        long_input = 'b' * 26
        last_name_input.clear()
        last_name_input.send_keys(long_input)
        time.sleep(1)

        current_value = last_name_input.get_attribute('value')

        print(f"Введено символов: {len(current_value)}")
        assert len(current_value) <= 25, f"Длина введенного текста {len(current_value)} превышает допустимый лимит"
        time.sleep(1)

def test_selenium_web_tables_8():

    with allure.step('Запускаем и настраиваем браузер'):
            driver = webdriver.Chrome()
            driver.get("https://demoqa.com/webtables")
            driver.maximize_window()
            driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(2)

    with allure.step('Проверка поля "Email"'):




    driver.quit()