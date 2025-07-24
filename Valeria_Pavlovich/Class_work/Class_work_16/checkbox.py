import time
import allure
from allure_commons.types import Severity
from allure_commons.types import LabelType
from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest_check as check
from Valeria_Pavlovich.Class_work.Class_work_16.locators.locators import LocatorsCheckBox as Cl


@allure.title('This test checks checkboxes')
@allure.description('Test clicks the arrows and ticks checkboxes')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, 'PYTHON')
@allure.id('1')
@allure.manual
@allure.link("https://www.google.com/?hl=en")
@allure.issue('A-1')
@allure.testcase('B-2')
@allure.epic("UI autotests")
@allure.feature('Elements section')
@allure.story("Checkbox tab")
def test_checkbox():

    with allure.step("Browser start"):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/checkbox")
        driver.maximize_window()
        time.sleep(1)

    with allure.step('Clicking the buttons to open the tabs'):
        driver.find_element(By.XPATH, Cl.check_box_home).click()
        driver.find_element(By.XPATH, Cl.check_box_downloads).click()
        driver.find_element(By.XPATH, Cl.btn_word_file).click()
        driver.find_element(By.XPATH, Cl.btn_excel_file).click()

    with allure.step('Checking the checkboxes'):
        assert driver.find_element(By.XPATH, Cl.check_box_word_file).is_selected()
        assert driver.find_element(By.XPATH, Cl.check_box_excel_file).is_selected()
    with allure.step('Checking the text: checkbox is selected'):
        assert driver.find_element(By.ID, Cl.text_result).text.find('downloads') > -1
        assert driver.find_element(By.ID, Cl.text_result).text.find('wordFile') > -1
        assert driver.find_element(By.ID, Cl.text_result).text.find('excelFile') > -1

    time.sleep(2)
    driver.quit()


@allure.title('This test checks radiobuttons')
@allure.description('Test clicks the radiobuttons')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, 'PYTHON')
@allure.id('1')
@allure.manual
@allure.link("https://www.google.com/?hl=en")
@allure.issue('A-1')
@allure.testcase('B-2')
@allure.epic("UI autotests")
@allure.feature('Elements section')
@allure.story("Radiobutton tab")
def test_radiobutton():
    with allure.step("Browser start"):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/radio-button")
        driver.maximize_window()
        time.sleep(1)

    with allure.step('Clicking the buttons to open the tabs'):
        driver.find_element(By.CSS_SELECTOR, 'label[for="yesRadio"]').click()
        check.is_true(driver.find_element(By.ID, 'yesRadio').is_selected(), 'The button is expected to be active')
        check.is_true(driver.find_element(By.ID, 'noRadio').is_enabled(), 'The button is expected to be active')

        driver.quit()

@allure.title('This test checks web tables')
@allure.description('This test adds, updates and deletes information')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, 'PYTHON')
@allure.id('1')
@allure.manual
@allure.link("https://www.google.com/?hl=en")
@allure.issue('A-1')
@allure.testcase('B-2')
@allure.epic("UI autotests")
@allure.feature('Elements section')
@allure.story("Web tables tab")
def test_webtable():
    with allure.step("Browser start"):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/webtables")
        driver.maximize_window()
        time.sleep(1)

    # with allure.step('Clicking the button to delete a record'):
    #     elements = driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]')
    #     driver.find_element(By.CSS_SELECTOR, 'span[title="Delete"]').click()
    #     elements_delete = driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]')
    #     check.not_equal(len(elements), len(elements_delete))
    #     driver.quit()

    with allure.step('Clicking the Add button to add a record'):
        driver.find_element(By.XPATH, '//*[@id="addNewRecordButton"]').click()
        driver.find_element(By.XPATH, '//*[@placeholder="First Name" and @id="firstName"]').send_keys('A')
        driver.find_element(By.XPATH, '//*[@placeholder="Last Name" and @id="lastName"]').send_keys('B')
        driver.find_element(By.XPATH, '//*[@placeholder="name@example.com" and @id="userEmail"]').send_keys('C@D.EF')
        driver.find_element(By.XPATH, '//*[@placeholder="Age" and @id="age"]').send_keys('30')
        driver.find_element(By.XPATH, '//*[@placeholder="Salary" and @id="salary"]').send_keys('10000')
        driver.find_element(By.XPATH, '//*[@placeholder="Department" and @id="department"]').send_keys('G')
        driver.find_element(By.XPATH, '// *[@id="submit"]').click()


        # elements = driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]')
        # driver.find_element(By.CSS_SELECTOR, 'span[title="Delete"]').click()
        # elements_delete = driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]')
        # check.not_equal(len(elements), len(elements_delete))
        # driver.quit()