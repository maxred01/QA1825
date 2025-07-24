import time
import allure
from allure_commons.types import Severity
from allure_commons.types import LabelType

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pytest_check as check
# from maksim_tsybulka.class_work.class_work_15.locators.locators_demo_qa import LocatorsCheckBox as Cl
#
#
# @allure.title('Это тест проверяет заполнение и результат заполнения формы')
# @allure.description("""Тест вводит текст для полей user_name и тд и сверяет результат в полях  name и тд""")
# @allure.tag("Smoke")
# @allure.severity(Severity.CRITICAL)
# @allure.label(LabelType.LANGUAGE, "python")
# @allure.id("123")
# @allure.manual
# @allure.link("https://hoster.by/", name="Тест-кейсы теста")
# @allure.issue("AUTH-123")
# @allure.testcase("TMS-456")
# @allure.epic("UI автотетсы")
# @allure.feature("Раздел Elements")
# @allure.story("Вкладка Test Box")
# def test_selenium():
#
#     with allure.step('Подготовка тестовых данных'):
#         user_name = 'tri-kota'
#         user_email = 'test@gmail.com'
#         current_address = 'test currentAddress'
#         permanent_address = 'test permanentAddress'
#
#     with allure.step('Запускаем и настройка браузер'):
#         driver = webdriver.Chrome()
#         driver.get("https://demoqa.com/text-box")
#         driver.maximize_window()
#     time.sleep(1)
#
#     elemets_form_send_keys = [
#         (driver.find_element(By.ID, 'userName'), 'Full Name', user_name),
#         (driver.find_element(By.ID, 'userEmail'), 'Email', user_email),
#         (driver.find_element(By.ID, 'currentAddress'), 'Current Address', current_address),
#         (driver.find_element(By.ID, 'permanentAddress'), 'Permanent Address', permanent_address)
#     ]
#     for element, text_elemet, send_keys_element in elemets_form_send_keys:
#         with allure.step(f'Ввод текста для поля {text_elemet}'):
#             element.send_keys(send_keys_element)
#
#     time.sleep(2)
#     with allure.step('Скролл страницы вниз'):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#     with allure.step('Нажатие на кнопку "submit"'):
#         driver.find_element(By.ID, 'submit').click()
#
#     elemets_form = [
#         (driver.find_element(By.ID, 'name'), user_name, 'Name'),
#         (driver.find_element(By.ID, 'email'), user_email, 'Email'),
#         (driver.find_element(By.XPATH, '//p[@id="currentAddress"]'), current_address, 'Current Address'),
#         (driver.find_element(By.XPATH, '//p[@id="permanentAddress"]'), permanent_address, 'Permanent Address')
#     ]
#     for elemet, elemets_text, name_form in elemets_form:
#         with allure.step(f'Проверка поля {name_form}'):
#             check.greater(elemet.text.find("elemets_text"), -1, f"Текста {elemets_text} нет на экарне")
#
#     time.sleep(2)
#     driver.quit()


# @allure.title('Это тест проверяет чекбоксы')
# @allure.description("""Тест вводит нажимает на вложенности и прожимает чекбоксы""")
# @allure.tag("Smoke")
# @allure.severity(Severity.CRITICAL)
# @allure.label(LabelType.LANGUAGE, "python")
# @allure.id("123")
# @allure.manual
# @allure.link("https://hoster.by/", name="Тест-кейсы теста")
# @allure.issue("AUTH-123")
# @allure.testcase("TMS-456")
# @allure.epic("UI автотетсы")
# @allure.feature("Раздел Elements")
# @allure.story("Вкладка Check Box")
# def test_selenium_is_selected():
#     with allure.step('Запускаем и настройка браузер'):
#         driver = webdriver.Chrome()
#         driver.get("https://demoqa.com/checkbox")
#         driver.maximize_window()
#         time.sleep(1)
#
#     with allure.step('Прожатие кнопок для открытие вкладок'):
#         driver.find_element(By.XPATH, '//button[@class="rct-collapse rct-collapse-btn"]').click()
#         driver.find_element(By.XPATH, '(//li[@class="rct-node rct-node-parent rct-node-expanded"]//button[@class="rct-collapse rct-collapse-btn"])[4]').click()
#         driver.find_element(By.XPATH, "//span[contains(text(),'Word File.doc')]").click()
#         driver.find_element(By.XPATH, "//span[contains(text(),'Excel File.doc')]").click()
#
#     with allure.step('Проверка: что нажаты чекбоксы'):
#         assert driver.find_element(By.XPATH, Cl.check_box_word_file).is_selected()
#         assert driver.find_element(By.XPATH, Cl.check_box_excel_file).is_selected()
#
#     with allure.step('Проверка текста: что чекс выбран'):
#         assert driver.find_element(By.ID, Cl.text_result).text.find('downloads') > -1
#         assert driver.find_element(By.ID, Cl.text_result).text.find('wordFile') > -1
#         assert driver.find_element(By.ID, Cl.text_result).text.find('excelFile') > -1
#
#     time.sleep(2)
#     driver.quit()


# @allure.title('Это тест проверяет радиобаттон')
# @allure.description("""Тест нажимает по кажлй кнопки и проверяет выбран ли радиобатон или нет""")
# @allure.tag("Smoke")
# @allure.severity(Severity.CRITICAL)
# @allure.label(LabelType.LANGUAGE, "python")
# @allure.id("123")
# @allure.manual
# @allure.link("https://hoster.by/", name="Тест-кейсы теста")
# @allure.issue("AUTH-123")
# @allure.testcase("TMS-456")
# @allure.epic("UI автотетсы")
# @allure.feature("Раздел Elements")
# @allure.story("Вкладка Check Box")
# def test_selenium_radio_button():
#     with allure.step('Запускаем и настройка браузер'):
#         driver = webdriver.Chrome()
#         driver.get("https://demoqa.com/radio-button")
#         driver.maximize_window()
#         time.sleep(1)
#
#     with allure.step('Прожатие кнопок для открытие вкладок'):
#         driver.find_element(By.CSS_SELECTOR, 'label[for="yesRadio"]').click()
#         check.is_true(driver.find_element(By.ID, 'yesRadio').is_selected(), 'ожидалось: что кнопка будет активной')
#         check.is_false(driver.find_element(By.ID, 'noRadio').is_enabled(), 'ожидалось: что кнопка будет активной')
#
#         check.is_true(driver.find_element(By.ID, 'yesRadio'))
#         check.is_true(driver.find_element(By.ID, "noRadio").is_enabled(), '')
#
#         driver.quit()

@allure.title('Это тест проверяет форму')
@allure.description("""Тест нажимает по кажлй кнопки и проверяет выбран ли радиобатон или нет""")
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("123")
@allure.manual
@allure.link("https://hoster.by/", name="Тест-кейсы теста")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@allure.epic("UI автотетсы")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Check Box")
def test_selenium_radio_button():
    with allure.step('Запускаем и настройка браузер'):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/web tables")
        driver.maximize_window()
        time.sleep(1)

    with allure.step('Прожатие кнопок для открытие вкладок'):
        elements = driver.find_elements(By.CSS_SELECTOR, 'span["title=Delete"]')
        print(len(elements))
        driver.find_elements(By.CSS_SELECTOR, 'span["title=Delete"]').click()
        elements_delete = driver.find_elements(By.CSS_SELECTOR, 'span["title=Delete"]')
        check.not_equal(elements, elements_delete)

        driver.quit()


@allure.title("Этот тест проверяет заполнение формы")
@allure.description("""Тест вводит поля""")
@allure.tag("Smoky")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("123")
@allure.manual
@allure.link("https://hoster.by/", name="Тест-кейсы теста")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@allure.epic("UI автотесты")
@allure.feature("раздел Elements")
@allure.story("Вкладка Web Tables")


def test_selenium():

    with allure.step('Подготовка тестовых данных'):
        first_name = 'tri-kota'
        last_name = 'tri-kota'
        user_email = 'test@gmail.com'
        user_age = '45'
        user_salary = '200'
        user_department = rrrrr


    with allure.step('Запуск и настройка браузера'):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/text-box")
        driver.maximize_window()
    time.sleep(1)

    elemets_form_send_keys = [
        (driver.find_element(By.ID, 'firstName'), 'First Name', first_name),
        (driver.find_element(By.ID, 'lastName'), 'Last Name', last_name),
        (driver.find_element(By.ID, 'userEmail'), 'Email', user_email),
        (driver.find_element(By.ID, 'age'), 'Age', user_age),
        (driver.find_element(By.ID, 'salary'), 'Salary ', user_salary),
        (driver.find_element(By.ID, 'department'), 'Department', user_department)
    ]
    for element, text_elemet, send_keys_element in elemets_form_send_keys:
#       with allure.step(f'Ввод текста для поля {text_element}'):
            element.send_keys(send_keys_element)

    time.sleep(2)
    with allure.step('Скролл страницы вниз'):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # driver.execute_script("window.scrollBy(0, 50);")    # driver.find_element(By.ID, 'submit').send_keys(Keys.DOWN)    driver.find_element(By.ID, 'submit').click()
    output_form = driver.find_element(By.ID, 'output')

    assert output_form.is_displayed(), 'Результат формы не появился на экарне'
    elemets_form = [
        (driver.find_element(By.ID, 'name'), user_name, 'Name'),
        (driver.find_element(By.ID, 'email'), user_email, 'Email'),
        (driver.find_element(By.XPATH, '//p[@id="currentAddress"]'), current_address, 'Current Address'),
        (driver.find_element(By.XPATH, '//p[@id="permanentAddress"]'), permanent_address, 'Permanent Address')
    ]
    for elemet, elemets_text in elemets_form:
        check.greater(elemet.text.find(elemets_text), -1, f"Текста {elemets_text} нет на экране")

    time.sleep(2)
    driver.quit()