import time
import allure
from allure_commons.types import LabelType

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pytest_check as check
@allure.title("Этот тест проверяет чек бокс")
@allure.tag("Smoke")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("123")
@allure.manual
@allure.link("https://hoster.by/", name="Тест-кейсы теста")
@allure.issue("AUTH-123")
@allure.epic("UI автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Chek  Box")
def test_selenium():
    with allure.step('Запускаем и настраиваем браузер'):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/checkbox")
        driver.maximize_window()
        time.sleep(1)
    with allure.step('Скролл страницы вниз'):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    with allure.step('Прожатие кнопок для открытия вкладок'):
        driver.find_element(By.XPATH, '//button[@class="rct-collapse rct-collapse-btn"]').click()
        driver.find_element(By.XPATH,'(//li[@class="rct-node rct-node-parent rct-node-expanded"]//button[@class="rct-collapse rct-collapse-btn"])[4]').click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Word File.doc')]").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Excel File.doc')]").click()

    with allure.step('Проверка что нажаты чек боксы'):
        assert driver.find_element(By. XPATH,'//input[@id="tree-node-wordFile"]').is_selected()
        assert driver.find_element(By.XPATH, '//input[@id="tree-node-excelFile"]').is_selected()

    # with allure.step('Проверка текста что чек выбран'):
    #     assert driver.find_element(By.ID, ).text дописать самой


    time.sleep(1)
    driver.quit()



#######################radio button#####################

allure.title("Этот тест проверяет radio button")
@allure.tag("Smoke")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("123")
@allure.manual
@allure.link("https://hoster.by/", name="Тест-кейсы теста")
@allure.issue("AUTH-123")
@allure.epic("UI автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Chek  Box")
def test_selenium_radio_button():
    with allure.step('Запускаем и настраиваем браузер'):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/radio-button")
        driver.maximize_window()
        time.sleep(1)
    with allure.step('Скролл страницы вниз'):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    with allure.step('Прожатие кнопоки Yes'):
        driver.find_element(By.CSS_SELECTOR, "label[for='yesRadio']").click(),
        check.is_true(driver.find_element(By.XPATH, '//span[@class="text-success"]').text.find('Yes') > -1, 'ожидали в сообщении "Yes" ')
        check.is_true(driver.find_element(By.ID, 'yesRadio').is_selected(), 'кнопка должна быть подсвечена')

    with allure.step('Прожатие кнопоки impressive'):
        driver.find_element(By.CSS_SELECTOR, "label[for='impressiveRadio']").click(),
        check.is_true (driver.find_element(By.XPATH, '//span[@class="text-success"]').text.find('Impressive') > -1),
        check.is_true(driver.find_element(By.ID, 'impressiveRadio').is_selected(), 'кнопка должна быть подсвечена')

    # with allure.step('Прожатие кнопоки No'):
    #     driver.find_element(By.ID, 'noRadio').click()
    #     check.is_false((driver.find_element(By.ID, 'noRadio').is_enabled(), 'ожидалось, что кнопка будет активной'))
    # time.sleep(1)  проверить и исправить ошибки
    driver.quit()



###################################################WEB TABLES############################
allure.title("Этот тест проверяет WEB TABLES")
@allure.tag("Smoke")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("123")
@allure.manual
@allure.link("https://hoster.by/", name="Тест-кейсы теста")
@allure.issue("AUTH-123")
@allure.epic("UI автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Chek  Box")
def test_selenium_DELETE():
    with allure.step('Запускаем и настраиваем браузер'):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/webtables")
        driver.maximize_window()
        time.sleep(1)
    with allure.step('Скролл страницы вниз'):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    with allure.step('Прожатие кнопоки DELETE'):
        elements = (By.CSS_SELECTOR, 'span[title="Delete"]')
        print(len(elements))
        driver.find_element(By.CSS_SELECTOR, 'span[title="Delete"]').click()
        elements_delete = driver.find_element(By.CSS_SELECTOR, 'span[title="Delete"]')
        check.not_equal(elements, elements_delete)

    driver.quit()

def test_selenium_ADD():
    with allure.step('Запускаем и настраиваем браузер'):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/webtables")
        driver.maximize_window()
        time.sleep(1)
    with allure.step('Скролл страницы вниз'):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    with allure.step('Прожатие кнопоки ADD'):
        driver.find_element(By.XPATH, '//*[@class="col-md-7"]').click()

    with allure.step('Подготовка тестовых даных'):
        First_Name = 'Nata'
        Last_Name = 'Rom'
        Email = 'Nat@gmail.com'
        Age = '35'
        Salary = 'klug'
        Department = 'tjut'

    elemets_form_send_keys = [
        (driver.find_element(By.ID, "firstName"), 'First Name', First_Name),
        (driver.find_element(By.ID, "lastName"), 'Last Name', Last_Name),
        (driver.find_element(By.ID, 'userEmail'), 'User Emale',  Email),
        (driver.find_element(By.ID, 'age'), 'Age', Age),
        (driver.find_element(By.ID, 'salary'), 'Salary', Salary),
        (driver.find_element(By.ID, 'department'), 'Departmen', Department)
    ]
    for element, text_elemet, send_keys_element in elemets_form_send_keys:
        element.send_keys(send_keys_element)
    time.sleep(2)

    with allure.step('Скролл страницы вниз'):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    driver.quit()