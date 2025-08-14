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

    with allure.step('Запускаем и настраиваем браузер / Проверка поля "First Name"'):
            driver = webdriver.Chrome()
            driver.get("https://demoqa.com/webtables")
            driver.maximize_window()
            driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(2)

    driver.find_element(By.XPATH, '//button[@id="addNewRecordButton"]').click()

    Last_Name = 'Sport'
    Email = 'stas.sport@example.com'
    Age = '46'
    Salary = '90000'
    Department = 'IT'

    elements_form_send_keys = [
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

            driver.find_element(By.XPATH, '// button[ @ id = "submit"]').click()

    def is_submit_active():
            submit_btn = driver.find_element(By.XPATH, '// button[ @ id = "submit"]')
            return submit_btn.is_enabled()

    assert is_submit_active()

    with allure.step('Проверка поля "First Name"'):
            first_name_input = driver.find_element(By.XPATH, '//input[@placeholder="First Name"]')

            long_input = 'a' * 26
            first_name_input.clear()
            first_name_input.send_keys(long_input)
            time.sleep(1)

    current_value = first_name_input.get_attribute('value')

    print(f"Введено символов: {len(current_value)}")
    assert len(current_value) <= 25, f"Длина введенного текста {len(current_value)} превышает допустимый лимит"
    time.sleep(1)



def test_selenium_web_tables_8():

    with allure.step('Запускаем и настраиваем браузер / Проверка поля "Last Name"'):
            driver = webdriver.Chrome()
            driver.get("https://demoqa.com/webtables")
            driver.maximize_window()
            driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(2)

    driver.find_element(By.XPATH, '//button[@id="addNewRecordButton"]').click()

    First_Name = 'Stas'
    Email = 'stas.sport@example.com'
    Age = '46'
    Salary = '90000'
    Department = 'IT'

    elements_form_send_keys = [
            (driver.find_element(By.XPATH, '//input[@placeholder="First Name"]'), 'First Name', First_Name),
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

            driver.find_element(By.XPATH, '// button[ @ id = "submit"]').click()

    def is_submit_active():
            submit_btn = driver.find_element(By.XPATH, '// button[ @ id = "submit"]')
            return submit_btn.is_enabled()

    assert is_submit_active()

    with allure.step('Проверка поля "Last Name"'):
        last_name_input = driver.find_element(By.XPATH, '//input[@placeholder="Last Name"]')

        long_input = 'b' * 26
        last_name_input.clear()
        last_name_input.send_keys(long_input)
        time.sleep(1)

        current_value = last_name_input.get_attribute('value')

        print(f"Введено символов: {len(current_value)}")
        assert len(current_value) <= 25, f"Длина введенного текста {len(current_value)} превышает допустимый лимит"
        time.sleep(1)

def test_selenium_web_tables_10():

    with allure.step('Запускаем и настраиваем браузер / Проверка поля "Email"'):
            driver = webdriver.Chrome()
            driver.get("https://demoqa.com/webtables")
            driver.maximize_window()
            driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(2)
    driver.find_element(By.XPATH, '//button[@id="addNewRecordButton"]').click()

    First_Name = 'Stas'
    Last_Name = 'Sport'
    Age = '46'
    Salary = '90000'
    Department = 'IT'

    elements_form_send_keys = [
        (driver.find_element(By.XPATH, '//input[@placeholder="First Name"]'), 'First Name', First_Name),
        (driver.find_element(By.XPATH, '//input[@placeholder="Last Name"]'), 'Last Name', Last_Name),
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

        driver.find_element(By.XPATH, '// button[ @ id = "submit"]').click()

    def is_submit_active():
        submit_btn = driver.find_element(By.XPATH, '// button[ @ id = "submit"]')
        return submit_btn.is_enabled()

    assert is_submit_active()

    with allure.step('Проверка поля "Email"'):
        email_input = driver.find_element(By.XPATH, '//input[@placeholder="name@example.com"]')
        email_input.clear()
        email_input.send_keys('testemail.com')

        driver.find_element(By.XPATH, '// button[ @ id = "submit"]').click()
        time.sleep(1)

        assert is_submit_active()

        email_input = driver.find_element(By.XPATH, '//input[@placeholder="name@example.com"]')
        email_input.clear()
        email_input.send_keys('test@')

        driver.find_element(By.XPATH, '// button[ @ id = "submit"]').click()
        time.sleep(1)

        assert is_submit_active()

def test_selenium_web_tables_11():

    with allure.step('Запускаем и настраиваем браузер / Проверка поля "Age"'):
            driver = webdriver.Chrome()
            driver.get("https://demoqa.com/webtables")
            driver.maximize_window()
            driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(2)
    driver.find_element(By.XPATH, '//button[@id="addNewRecordButton"]').click()

    First_Name = 'Stas'
    Last_Name = 'Sport'
    Email = 'stas.sport@example.com'
    Salary = '90000'
    Department = 'IT'

    elements_form_send_keys = [
        (driver.find_element(By.XPATH, '//input[@placeholder="First Name"]'), 'First Name', First_Name),
        (driver.find_element(By.XPATH, '//input[@placeholder="Last Name"]'), 'Last Name', Last_Name),
        (driver.find_element(By.XPATH, '//input[@placeholder="name@example.com"]'), 'Email', Email),
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

        driver.find_element(By.XPATH, '// button[ @ id = "submit"]').click()

    def is_submit_active():
        submit_btn = driver.find_element(By.XPATH, '// button[ @ id = "submit"]')
        return submit_btn.is_enabled()

    assert is_submit_active()

    with allure.step('Проверка поля "Age"'):
        age_input = driver.find_element(By.XPATH, '//input[@pattern="\d*"]')
        age_input.clear()
        age_input.send_keys('ss')

        driver.find_element(By.XPATH, '// button[ @ id = "submit"]').click()
        time.sleep(1)

        assert is_submit_active()

        age_input = driver.find_element(By.XPATH, '//input[@pattern="\d*"]')
        age_input.clear()
        age_input.send_keys('!?')

        driver.find_element(By.XPATH, '// button[ @ id = "submit"]').click()
        time.sleep(1)

        assert is_submit_active()

    with allure.step('Проверка поля "Age"'):
        age_input = driver.find_element(By.XPATH, '//input[@pattern="\d*"]')
        age_input.clear()
        age_input.send_keys('123')
        time.sleep(1)

        current_value = age_input.get_attribute('value')

        print(f"Введено символов: {len(current_value)}")
        assert len(current_value) <= 2, f"Длина введенного текста {len(current_value)} превышает допустимый лимит"
        time.sleep(1)

def test_selenium_web_tables_12():

    with allure.step('Запускаем и настраиваем браузер / Проверка поля "Salary"'):
            driver = webdriver.Chrome()
            driver.get("https://demoqa.com/webtables")
            driver.maximize_window()
            driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(2)
    driver.find_element(By.XPATH, '//button[@id="addNewRecordButton"]').click()

    First_Name = 'Stas'
    Last_Name = 'Sport'
    Email = 'stas.sport@example.com'
    Age = '46'
    Department = 'IT'

    elements_form_send_keys = [
            (driver.find_element(By.XPATH, '//input[@placeholder="First Name"]'), 'First Name', First_Name),
            (driver.find_element(By.XPATH, '//input[@placeholder="Last Name"]'), 'Last Name', Last_Name),
            (driver.find_element(By.XPATH, '//input[@placeholder="name@example.com"]'), 'Email', Email),
            (driver.find_element(By.XPATH, '//input[@pattern="\d*"]'), 'Age', Age),
            (driver.find_element(By.XPATH, '//input[@placeholder="Department"]'), 'Department', Department)
        ]

    for locator, name_form, input_value in elements_form_send_keys:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.clear()
            element.send_keys(input_value)

            time.sleep(1)

            driver.find_element(By.XPATH, '// button[ @ id = "submit"]').click()

    def is_submit_active():
            submit_btn = driver.find_element(By.XPATH, '// button[ @ id = "submit"]')
            return submit_btn.is_enabled()

    assert is_submit_active()

    with allure.step('Проверка поля "Salary"'):
        salary_input = driver.find_element(By.XPATH, '//input[@placeholder="Salary"]')
        salary_input.clear()
        salary_input.send_keys('ppp')

        driver.find_element(By.XPATH, '// button[ @ id = "submit"]').click()
        time.sleep(1)

        assert is_submit_active()

        salary_input = driver.find_element(By.XPATH, '//input[@placeholder="Salary"]')
        salary_input.clear()
        salary_input.send_keys('!?')

        driver.find_element(By.XPATH, '// button[ @ id = "submit"]').click()
        time.sleep(1)

        assert is_submit_active()

    with allure.step('Проверка поля "Salary"'):
        salary_input = driver.find_element(By.XPATH, '//input[@placeholder="Salary"]')
        long_input = '5' * 11
        salary_input.clear()
        salary_input.send_keys(long_input)
        time.sleep(1)

        current_value = salary_input.get_attribute('value')

        print(f"Введено символов: {len(current_value)}")
        assert len(current_value) <= 10, f"Длина введенного текста {len(current_value)} превышает допустимый лимит"
        time.sleep(1)

def test_selenium_web_tables_13():

    with allure.step('Запускаем и настраиваем браузер / Проверка поля "Department"'):
            driver = webdriver.Chrome()
            driver.get("https://demoqa.com/webtables")
            driver.maximize_window()
            driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(2)

    driver.find_element(By.XPATH, '//button[@id="addNewRecordButton"]').click()

    First_Name = 'Stas'
    Last_Name = 'Sport'
    Email = 'stas.sport@example.com'
    Age = '46'
    Salary = '90000'

    elements_form_send_keys = [
            (driver.find_element(By.XPATH, '//input[@placeholder="First Name"]'), 'First Name', First_Name),
            (driver.find_element(By.XPATH, '//input[@placeholder="Last Name"]'), 'Last Name', Last_Name),
            (driver.find_element(By.XPATH, '//input[@placeholder="name@example.com"]'), 'Email', Email),
            (driver.find_element(By.XPATH, '//input[@pattern="\d*"]'), 'Age', Age),
            (driver.find_element(By.XPATH, '//input[@placeholder="Salary"]'), 'Salary', Salary),
        ]

    for locator, name_form, input_value in elements_form_send_keys:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.clear()
            element.send_keys(input_value)

            time.sleep(1)

            driver.find_element(By.XPATH, '// button[ @ id = "submit"]').click()

    def is_submit_active():
            submit_btn = driver.find_element(By.XPATH, '// button[ @ id = "submit"]')
            return submit_btn.is_enabled()

    assert is_submit_active()

    with allure.step('Проверка поля "Department"'):
            department_input = driver.find_element(By.XPATH, '//input[@placeholder="Department"]')

            long_input = 'd' * 26
            department_input.clear()
            department_input.send_keys(long_input)
            time.sleep(1)

            current_value = department_input.get_attribute('value')

            print(f"Введено символов: {len(current_value)}")
            assert len(current_value) <= 25, f"Длина введенного текста {len(current_value)} превышает допустимый лимит"
            time.sleep(1)





    driver.quit()