import time
import allure
from allure_commons.types import Severity
from allure_commons.types import LabelType
from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest_check as check

@allure.title('This test checks form filling and result')
@allure.description('Test enters the text for the User Name field and checks the result')
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
@allure.story("Test Box tab")
def test_alice():
    with allure.step('Test data preparation'):
        user_name = 'Alice'
        user_email = 'rabbit@forest.com'
        current_address = 'Oxford'
        permanent_address = 'Wonderland'

    with allure.step("Browser start"):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/text-box")
        driver.maximize_window()
    time.sleep(1)
    elements_form_send_keys = [
        (driver.find_element(By.XPATH, '//*[@id="userName-wrapper"]//input'), 'Full name', user_name),
        (driver.find_element(By.XPATH, '//*[@id="userEmail-wrapper"]//input'), 'Email', user_email),
        (driver.find_element(By.XPATH, '''//*[@id="currentAddress-wrapper"]//*[local-name() = 'textarea']'''), 'Current address', current_address),
        (driver.find_element(By.XPATH, '''//*[@id="permanentAddress-wrapper"]//*[local-name() = 'textarea']'''), 'Permanent address', permanent_address)
    ]
    for element, text_element, send_keys_element in elements_form_send_keys:
        with allure.step(f"Text entering for the {text_element}"):
            element.send_keys(send_keys_element)

    with allure.step("Scroll down"):
        submit_btn = driver.find_element(By.XPATH, '//*[@id="submit"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    with allure.step("Submit click"):
        submit_btn.click()
    time.sleep(2)

    elements_form = [
        (driver.find_element(By.XPATH, '//*[@id="output"]//*[@id="name"]'), user_name, "Name"),
        (driver.find_element(By.XPATH, '//*[@id="output"]//*[@id="email"]'), user_email, "Email"),
        (driver.find_element(By.XPATH, '//*[@id="output"]//*[@id="currentAddress"]'), current_address, "Current address"),
        (driver.find_element(By.XPATH, '//*[@id="output"]//*[@id="permanentAddress"]'), permanent_address, "Permanent address")
    ]

    for element, elements_text in elements_form:
        check.greater(element.text.find(elements_text), -1, f'Text {elements_text} is not present')

    time.sleep(2)
    driver.quit()