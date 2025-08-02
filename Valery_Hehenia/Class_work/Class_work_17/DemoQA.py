Valery Hehenia, [02.08.2025 19:54]
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
from allure_commons.types import LabelType
from allure_commons.types import Severity
import pytest_check as check



@allure.title('Этот тест проверяет выбор чек-боксов')
@allure.description('''Тест переходит по дереву, и выбирает чек-боксы''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("123")
@allure.manual
@allure.link("https://hoster.by/", name="Тест-кейсы теста")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@allure.epic("UI автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Check Box")

def test_demoqa_checkbox():

     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/checkbox")
     driver.maximize_window()


     with allure.step('Прожатие кнопок лоя открытия вкладок'):
          toggle = driver.find_elements(By.CSS_SELECTOR, '[aria-label="Toggle"]')[0]
          toggle.find_element(By.CSS_SELECTOR, '[stroke="currentColor"]').click()

          toggle = driver.find_elements(By.CSS_SELECTOR, '[aria-label="Toggle"]')[3]
          toggle.find_element(By.CSS_SELECTOR, '[stroke="currentColor"]').click()

     with allure.step('Скрол страницы вниз'):
          driver.execute_script("window.scrollBy(0, 150);")

     with allure.step('Нажатие необходимых чек боксов'):
          toggle1 = driver.find_elements(By.CSS_SELECTOR,'[for="tree-node-wordFile"] [stroke="currentColor"]')[0]
          toggle1.click()

          toggle2 = driver.find_elements(By.CSS_SELECTOR, '[for="tree-node-excelFile"] [stroke="currentColor"]')[0]
          toggle2.click()

     time.sleep(2)

     with allure.step('Проверка выбора чек-боксов'):
          assert driver.find_element(By.XPATH, '//input[@id="tree-node-wordFile"]').is_selected()
          assert driver.find_element(By.XPATH, '//input[@id="tree-node-excelFile"]').is_selected()

     with allure.step('Проверка вывода текста'):
          spans = driver.find_elements(By.CSS_SELECTOR, "#result span.text-success")

          texts = [span.text for span in spans]
          assert "wordFile" in texts
          assert "excelFile" in texts


     driver.quit()




@allure.title('Этот тест проверяет RadioButton')
@allure.description('''Проверяем выбор RadioButtons''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("123")
@allure.manual
@allure.link("https://hoster.by/", name="Тест-кейсы теста")
@allure.issue("AUTH-1234")
@allure.testcase("TMS-4567")
@allure.epic("UI автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка RadioButton")
def test_demoqa_radioButton():

     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/radio-button")
     driver.maximize_window()


     with allure.step('Выбор Yes'):
          driver.find_element(By.CSS_SELECTOR, '[for="yesRadio"]').click()

     time.sleep(1)
     with allure.step('Проверка вывода текста'):
          text_yes = driver.find_element(By.XPATH, '//span[@class="text-success"]')
          check.is_false = text_yes.text == "Yes", 'Ожидалось Yes'



     with allure.step('Выбор Impressive'):
          driver.find_element(By.CSS_SELECTOR, '[for="impressiveRadio"]').click()

     time.sleep(1)
     with allure.step('Проверка активности NO'):
          text_Impressive = driver.find_element(By.XPATH, '//span[@class="text-success"]')
          check.is_false = text_Impressive.text == "Impressive", 'Impressive'



     with allure.step('Выбор NO'):
          check.is_false = text_Impressive.is_enabled()

     time.sleep(2)
     driver.quit()

##########################################################################################################

Valery Hehenia, [02.08.2025 19:54]
@allure.title('Этот тест проверяет добавление сотрудника в таблицу')
@allure.description('''Тест добаляет сотрудников''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("123")
@allure.manual
@allure.link("https://hoster.by/", name="Тест-кейсы теста")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@allure.epic("UI автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка WebSite")

def test_demoqa_Web_tables():

     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     first_name = "Peter"
     last_name = "Parket"
     email = "spider@mail.com"
     age = "25"
     salary = "5000"
     department = "Security"

     with allure.step('Открытие формы заполнения'):
          driver.find_element(By.ID, 'addNewRecordButton').click()

     with allure.step('Заполнение формы сотрудника'):
          elemets_form_send_keys = [
               (driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"'), 'first_name', first_name),
               (driver.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"]'), 'last_name', last_name),
               (driver.find_element(By.CSS_SELECTOR, '[placeholder="name@example.com"]'), 'email', email),
               (driver.find_element(By.CSS_SELECTOR, '[placeholder="Age"]'), 'age', age),
               (driver.find_element(By.CSS_SELECTOR, '[placeholder="Salary"]'), 'salary', salary),
               (driver.find_element(By.CSS_SELECTOR, '[placeholder="Department"]'), 'department', department)
          ]
          for element, text_elemet, send_keys_element in elemets_form_send_keys:
               with allure.step(f'Ввод текста для поля {text_elemet}'):
                    element.send_keys(send_keys_element)

     time.sleep(1)

     with allure.step('Добавление сотрудника в таблицу'):
          driver.find_element(By.ID, 'submit').click()

     time.sleep(2)

     with allure.step('Удаление записи'):
          elements = driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]')
          driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]').click()
          elements_delete = driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]')
          check.not_equal(len(elements), len(elements_delete))


     driver.quit()