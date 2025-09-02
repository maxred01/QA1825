from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
from allure_commons.types import LabelType
from allure_commons.types import Severity
import pytest_check as check



@allure.title('Этот тест проверяет добавление записи с валидными данными')
@allure.description('''Тест добаляет сотрудников''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("001")
@allure.manual
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/pxovYJbU/1-%D1%84%D1%80-001-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D0%B8-%D0%B2%D0%B0%D0%BB%D0%B8%D0%B4%D0%BD%D1%8B%D0%B5-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5", "ФР-001")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")

def test_demoqa_TC_001():

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

     with allure.step('Поиск добавленного сотрудника в таблицу'):
          rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")

          found = False
          for row in rows:
               print(row.text)
               if first_name in row.text and last_name in row.text and email in row.text:
                    found = True
                    break
     with allure.step('Проверка на добавленную запись'):
          assert found, f"Сотрудник {first_name} {last_name} не найден в таблице."

     driver.quit()


@allure.title('Этот тест проверяет добавление записи с пустыми полями')
@allure.description('''Добавление новой записи с незаполненными данными.''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("002")
@allure.manual
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/NYAU29Fn/2-%D1%84%D1%80-002-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D0%B8-%D0%BF%D1%83%D1%81%D1%82%D1%8B%D0%B5-%D0%BF%D0%BE%D0%BB%D1%8F", "ФР-002")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")

def test_demoqa_TC_002():

     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     first_name = ""
     last_name = ""
     email = ""
     age = ""
     salary = ""
     department = ""

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

     time.sleep(1)
     with allure.step('Проверка, что форма не закрыта.'):
          form = driver.find_element(By.ID, "userForm")
          assert form.is_displayed(), "Форма исчезла, хотя поля были пустыми!"

     driver.quit()



@allure.title('Этот тест проверяет добавление записи с частичным заполнением')
@allure.description('''Добавление новой записи с частично заполненными данными.''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("003")
@allure.manual
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/1R8yzikq/3-%D1%84%D1%80-003-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D0%B8-%D1%87%D0%B0%D1%81%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D0%B5-%D0%B7%D0%B0%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BF%D0%BE%D0%BB%D0%B5%D0%B9", "ФР-003")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")

def test_demoqa_TC_003():

     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     first_name = "Peter"
     last_name = "Parket"
     email = ""
     age = ""
     salary = ""
     department = ""

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

     time.sleep(1)

     with allure.step('Проверка, что форма не закрыта.'):
          form = driver.find_element(By.ID, "userForm")
          assert form.is_displayed(), "Форма исчезла, хотя поля были пустыми!"

     driver.quit()





@allure.title('Этот тест проверяет, что поле First Name не принимает больше 25 символов')
@allure.description('''Добавление новой записи с невалидными данными.''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("004")
@allure.manual
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/0bk1Z0Is/4-%D1%84%D1%80-004-first-name-%D0%BD%D0%B5%D0%B2%D0%B0%D0%BB%D0%B8%D0%B4%D0%BD%D1%8B%D0%B9-%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82", "ФР-004")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
def test_demoqa_TC_004():

     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     first_name = "P" * 26

     with allure.step('Открытие формы заполнения'):
          driver.find_element(By.ID, 'addNewRecordButton').click()

     with allure.step('Заполнение формы сотрудника'):
          first_name_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"')
          first_name_input.send_keys(first_name)

     actual_value = first_name_input.get_attribute("value")

     time.sleep(1)

     with allure.step('Проверка, что поле ввода First Name принимает только 25 символов.'):
          assert len(actual_value) == 25, (
               f"Поле приняло {len(actual_value)} символов вместо 25. Значение: {actual_value}"
          )

     driver.quit()




@allure.title('Этот тест проверяет, что поле Last Name не принимает больше 25 символов')
@allure.description('''Добавление новой записи с невалидными данными.''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("005")
@allure.manual
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/QG3ivElt/5-%D1%84%D1%80-005-last-name-%D0%BD%D0%B5%D0%B2%D0%B0%D0%BB%D0%B8%D0%B4%D0%BD%D1%8B%D0%B9-%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82", "ФР-005")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
def test_demoqa_TC_005():

     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     last_name = "P"*26


     with allure.step('Открытие формы заполнения'):
          driver.find_element(By.ID, 'addNewRecordButton').click()

     with allure.step('Заполнение формы сотрудника'):
          last_name_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"')
          last_name_input.send_keys(last_name)

     actual_value = last_name_input.get_attribute("value")


     time.sleep(1)

     with allure.step('Проверка, что поле ввода Last Name принимает только 25 символов.'):
          assert len(actual_value) == 25, (
               f"Поле приняло {len(actual_value)} символов вместо 25. Значение: {actual_value}"
          )

     driver.quit()





@allure.title('Этот тест проверяет, что поле Email не принимает не валидный формат')
@allure.description('''Добавление новой записи с невалидными данными.''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("006")
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/lvC8bMaz/6-%D1%84%D1%80-006-email-%D0%BD%D0%B5%D0%B2%D0%B0%D0%BB%D0%B8%D0%B4%D0%BD%D1%8B%D0%B9-%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82", "ФР-006")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
def test_demoqa_TC_006():

     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     first_name = "Peter"
     last_name = "Parket"
     age = "25"
     salary = "5000"
     department = "Security"

     test_emails = [
          ("invalid-email.com", False),
          ("user@.com", False),
          ("user@example", False),
          ("user@example_com", False),
          ("user@example.c", False),
          ("user@example,com", False),
          ("user@example.123", False),
          ("user name@example.com", False),
     ]
     with allure.step('Открытие формы заполнения'):
          driver.find_element(By.ID, 'addNewRecordButton').click()


     for email, should_be_valid in test_emails:
          with allure.step(f"Проверка значения Email = '{email}'"):


               driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]').clear()
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"]').clear()
               driver.find_element(By.CSS_SELECTOR, '[placeholder="name@example.com"]').clear()
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Age"]').clear()
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Salary"]').clear()
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Department"]').clear()


               driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]').send_keys(first_name)
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"]').send_keys(last_name)
               driver.find_element(By.CSS_SELECTOR, '[placeholder="name@example.com"]').send_keys(email)
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Age"]').send_keys(age)
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Salary"]').send_keys(salary)
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Department"]').send_keys(department)




          driver.find_element(By.ID, "submit").click()
          time.sleep(0.5)

          form_is_open = driver.find_element(By.ID, "userForm").is_displayed()


          with allure.step('Проверка, что форма остаётся открытой при невалидном email'):
               if not should_be_valid:
                    assert form_is_open, f"Форма закрылась при НЕвалидном email: {email}"


          сlose_button = driver.find_element(By.CSS_SELECTOR, '[aria-modal="true"] [aria-hidden="true"]')
          сlose_button.click()


          with allure.step('Открытие формы заполнения'):
               driver.find_element(By.ID, 'addNewRecordButton').click()

     driver.quit()





@allure.title('Этот тест проверяет, что поле Age не принимает не валидный формат')
@allure.description('''Добавление новой записи с невалидными данными.''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("007")
@allure.manual
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/3OD1S3Vh/7-%D1%84%D1%80-007-age-%D0%B3%D1%80%D0%B0%D0%BD%D0%B8%D1%87%D0%BD%D1%8B%D0%B5-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F", "ФР-007")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
def test_demoqa_TC_007():
     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     first_name = "Peter"
     last_name = "Parker"
     email = "peter.parker@example.com"
     salary = "5000"
     department = "Security"

     test_ages = [
          ("ab", False),
          ("!@", False),
          (-1, False),
          (100, False),
     ]

     for age_input, should_be_valid in test_ages:
          with allure.step(f"Проверка значения Salary = '{age_input}'"):
               driver.find_element(By.ID, 'addNewRecordButton').click()

               driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]').clear()
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"]').clear()
               driver.find_element(By.CSS_SELECTOR, '[placeholder="name@example.com"]').clear()
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Age"]').clear()
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Salary"]').clear()
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Department"]').clear()

               driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]').send_keys(first_name)
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"]').send_keys(last_name)
               driver.find_element(By.CSS_SELECTOR, '[placeholder="name@example.com"]').send_keys(email)
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Age"]').send_keys(age_input)
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Salary"]').send_keys(salary)
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Department"]').send_keys(department)

               driver.find_element(By.ID, "submit").click()
               time.sleep(0.5)

               form_is_open = driver.find_element(By.ID, "userForm").is_displayed()

               with allure.step('Проверка, что форма остаётся открытой при невалидном age'):
                    if not should_be_valid:
                         assert form_is_open, f"Форма закрылась при НЕвалидном age: {age_input}"

               сlose_button = driver.find_element(By.CSS_SELECTOR, '[aria-modal="true"] [aria-hidden="true"]')
               сlose_button.click()


     driver.quit()





@allure.title('Этот тест проверяет, что поле Salary не принимает не валидный формат')
@allure.description('''Добавление новой записи с невалидными данными.''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("008")
@allure.manual
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/NthuES79/8-%D1%84%D1%80-008-salary-%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D1%8B-%D0%B8-%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D1%87%D0%B8%D1%81%D0%BB%D0%B0", name="ФР-008")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
def test_demoqa_TC_008():
     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     first_name = "Peter"
     last_name = "Parker"
     email = "peter.parker@example.com"
     age = 30
     department = "Security"

     test_salarys = [
          ("ab", False),
          ("!@", False),
          (-1, False),
          (1234567890, False),
     ]

     for salary_input, should_be_valid in test_salarys:
          with allure.step(f"Проверка значения Salary = '{salary_input}'"):
               driver.find_element(By.ID, 'addNewRecordButton').click()

               driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]').clear()
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"]').clear()
               driver.find_element(By.CSS_SELECTOR, '[placeholder="name@example.com"]').clear()
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Age"]').clear()
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Salary"]').clear()
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Department"]').clear()

               driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]').send_keys(first_name)
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"]').send_keys(last_name)
               driver.find_element(By.CSS_SELECTOR, '[placeholder="name@example.com"]').send_keys(email)
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Age"]').send_keys(age)
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Salary"]').send_keys(salary_input)
               driver.find_element(By.CSS_SELECTOR, '[placeholder="Department"]').send_keys(department)

               driver.find_element(By.ID, "submit").click()
               time.sleep(0.5)

               form_is_open = driver.find_element(By.ID, "userForm").is_displayed()

               with allure.step('Проверка, что форма остаётся открытой при невалидном age'):
                    if not should_be_valid:
                         assert form_is_open, f"Форма закрылась при НЕвалидном age: {salary_input}"

               сlose_button = driver.find_element(By.CSS_SELECTOR, '[aria-modal="true"] [aria-hidden="true"]')
               сlose_button.click()

     driver.quit()





@allure.title('Этот тест проверяет редактирование существующей записи')
@allure.description('''Редактирование существующей записи валидными данными''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("009")
@allure.manual
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/2UC5ZD8S/9-%D1%80%D0%B7-001-%D1%80%D0%B5%D0%B4%D0%B0%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D1%83%D1%8E%D1%89%D0%B5%D0%B9-%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D0%B8",name="РЗ-001")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")

def test_demoqa_rz_001():

     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     first_name = "Peter"
     last_name = "Parket"
     email = "spider@mail.com"
     age = "25"
     salary = "5000"
     department = "QA"

     with allure.step('Открытие формы редактирования записи сотрудника'):
          time.sleep(1)
          driver.find_element(By.CSS_SELECTOR, '[data-toggle="tooltip"] [stroke="currentColor"]').click()


     time.sleep(1)

     with allure.step('Заполнение формы'):
          fields = [
               ("First Name", '[placeholder="First Name"]', first_name),
               ("Last Name", '[placeholder="Last Name"]', last_name),
               ("Email", '[placeholder="name@example.com"]', email),
               ("Age", '[placeholder="Age"]', age),
               ("Salary", '[placeholder="Salary"]', salary),
               ("Department", '[placeholder="Department"]', department)
          ]

          for field_name, selector, value in fields:
               element = driver.find_element(By.CSS_SELECTOR, selector)
               with allure.step(f'Очистка поля {field_name}'):
                    element.clear()
               with allure.step(f'Заполнение поля {field_name}'):
                    element.send_keys(value)
     time.sleep(1)


     with allure.step('Нажатие кнопки Submit'):
          driver.find_element(By.ID, 'submit').click()


     driver.quit()





@allure.title('Этот тест проверяет редактирование существующей записи')
@allure.description('''Редактирование существующей записи с не валидными данными''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("010")
@allure.manual
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/caDxOg6h/10-%D1%80%D0%B7-002-%D1%80%D0%B5%D0%B4%D0%B0%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D1%83%D1%8E%D1%89%D0%B5%D0%B9-%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D0%B8-%D1%81-%D0%BD%D0%B5-%D0%B2%D0%B0%D0%BB%D0%B8%D0%B4%D0%BD%D1%8B%D0%BC%D0%B8-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%BC%D0%B8",name="РЗ-002")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
def test_demoqa_rz_002():

     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     first_name = "Peter"
     last_name = "Parket"
     email = "123@"
     age = "qa"
     salary = "qwerty"
     department = "QA"

     with allure.step('Открытие формы редактирования записи сотрудника'):
          time.sleep(1)
          driver.find_element(By.CSS_SELECTOR, '[data-toggle="tooltip"] [stroke="currentColor"]').click()


     time.sleep(1)

     with allure.step('Заполнение формы'):
          fields = [
               ("First Name", '[placeholder="First Name"]', first_name),
               ("Last Name", '[placeholder="Last Name"]', last_name),
               ("Email", '[placeholder="name@example.com"]', email),
               ("Age", '[placeholder="Age"]', age),
               ("Salary", '[placeholder="Salary"]', salary),
               ("Department", '[placeholder="Department"]', department)
          ]

          for field_name, selector, value in fields:
               element = driver.find_element(By.CSS_SELECTOR, selector)
               with allure.step(f'Очистка поля {field_name}'):
                    element.clear()
               with allure.step(f'Заполнение поля {field_name}'):
                    element.send_keys(value)
     time.sleep(1)


     with allure.step('Нажатие кнопки Submit'):
          driver.find_element(By.ID, 'submit').click()

     with allure.step('Проверка, что форма не закрыта.'):
          form = driver.find_element(By.ID, "userForm")
          assert form.is_displayed(), "Форма исчезла, хотя поля были пустыми!"

     driver.quit()





@allure.title('Этот тест проверяет удаление записи')
@allure.description('''Удаление существующей записи''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("011")
@allure.manual
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/dY3CqgbL/11-%D1%83%D0%B7-001-%D1%83%D0%B4%D0%B0%D0%BB%D0%BD%D0%B8%D0%B5-%D0%BE%D0%B4%D0%BD%D0%BE%D0%B9-%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D0%B8",name="УЗ-001")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
def test_demoqa_rz_002():

     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     with allure.step('Проверка количества записей в таблице до удаления'):
          rows = driver.find_elements(By.CSS_SELECTOR, '.rt-table .rt-tr-group')
          non_empty_rows_to = []

          for row in rows:
               cells = row.find_elements(By.CSS_SELECTOR, '.rt-td')
               if any(cell.text.strip() != '' for cell in cells):
                    non_empty_rows_to.append(row)
          with allure.step(f'Количество записей {len(non_empty_rows_to)}'):
               print(f'Количество записей в таблице до: {len(non_empty_rows_to)}')

     with allure.step('Удаление первой записи в таблице'):
          time.sleep(0.2)
          elements = driver.find_elements(By.CSS_SELECTOR, '[data-toggle="tooltip"]')
          second_element = elements[1]
          path_element = second_element.find_element(By.CSS_SELECTOR, 'path')
          path_element.click()

     with allure.step('Проверка количества записей в таблице после удаления'):
          rows = driver.find_elements(By.CSS_SELECTOR, '.rt-table .rt-tr-group')
          non_empty_rows_after = []

          for row in rows:
               cells = row.find_elements(By.CSS_SELECTOR, '.rt-td')
               if any(cell.text.strip() != '' for cell in cells):
                    non_empty_rows_after.append(row)
          with allure.step(f'Количество записей {len(non_empty_rows_after)}'):
               print(f'Количество записей в таблице после: {len(non_empty_rows_after)}')

     time.sleep(0.5)

     assert non_empty_rows_to > non_empty_rows_after, "Число записей не изменилось, либо стало больше!"

     driver.quit()






@allure.title('Этот тест проверяет поиск по полю First Name')
@allure.description('''Поиск по полю First Name''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("012")
@allure.manual
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/7T3ko8qY/12-%D0%BF%D0%B7-001-%D0%BF%D0%BE%D0%B8%D1%81%D0%BA-%D0%BF%D0%BE-%D0%B8%D0%BC%D0%B5%D0%BD%D0%B8",name="ПЗ-001")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
def test_demoqa_pz_001():

     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     with allure.step('Поиск всех имен в таблице'):
          names = [
               cell.text.strip()
               for cell in driver.find_elements(By.CSS_SELECTOR, '.rt-tbody .rt-tr-group .rt-td:nth-child(1)')
               if cell.text.strip() != ''
          ]

          # print(f"Список имён: {names}")

     with allure.step('Перебор всех имен в строке поиска'):
          for name in names:
               search_box = driver.find_element(By.ID, 'searchBox')
               search_box.clear()
               time.sleep(0.5)
               search_box.send_keys(name)

     with allure.step('Получение имен во время поиска'):
          results = [
               cell.text.strip()
               for cell in driver.find_elements(By.CSS_SELECTOR, '.rt-tbody .rt-tr-group .rt-td:nth-child(1)')
               if cell.text.strip() != ''
          ]
     with allure.step('Сравнение результатов'):
          assert all(name in res for res in results), f"Поиск не сработал для {name}"

     driver.quit()





@allure.title('Этот тест проверяет поиск по полю Last Name')
@allure.description('''Поиск по полю Last Name''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("013")
@allure.manual
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/YErNgAkt/13-%D0%BF%D0%B7-002-%D0%BF%D0%BE%D0%B8%D1%81%D0%BA-%D0%BF%D0%BE-%D1%84%D0%B0%D0%BC%D0%B8%D0%BB%D0%B8%D0%B8",name="ПЗ-002")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
def test_demoqa_pz_002():

     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     with allure.step('Поиск всех фамилий в таблице'):
          lnames = [
               cell.text.strip()
               for cell in driver.find_elements(By.CSS_SELECTOR, '.rt-tbody .rt-tr-group .rt-td:nth-child(2)')
               if cell.text.strip() != ''
          ]

          print(f"Список имён: {lnames}")

     with allure.step('Перебор всех фамилий в строке поиска'):
          for lname in lnames:
               search_box = driver.find_element(By.ID, 'searchBox')
               search_box.clear()
               time.sleep(0.5)
               search_box.send_keys(lname)

     with allure.step('Получение фамилий во время поиска'):
          results = [
               cell.text.strip()
               for cell in driver.find_elements(By.CSS_SELECTOR, '.rt-tbody .rt-tr-group .rt-td:nth-child(2)')
               if cell.text.strip() != ''
          ]
     with allure.step('Сравнение результатов'):
          assert all(lname in res for res in results), f"Поиск не сработал для {lname}"

     driver.quit()





@allure.title('Этот тест проверяет поиск по полю Email')
@allure.description('''Поиск по полю Email''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("014")
@allure.manual
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/n7KSTDZQ/14-%D0%BF%D0%B7-003-%D0%BF%D0%BE%D0%B8%D1%81%D0%BA-%D0%BF%D0%BE-email",name="ПЗ-003")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
def test_demoqa_pz_003():

     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     with allure.step('Поиск всех Email в таблице'):
          emails = [
               cell.text.strip()
               for cell in driver.find_elements(By.CSS_SELECTOR, '.rt-tbody .rt-tr-group .rt-td:nth-child(4)')
               if cell.text.strip() != ''
          ]

          print(f"Список имён: {emails}")

     with allure.step('Перебор всех Email в строке поиска'):
          for email in emails:
               search_box = driver.find_element(By.ID, 'searchBox')
               search_box.clear()
               time.sleep(0.5)
               search_box.send_keys(email)

     with allure.step('Получение Email во время поиска'):
          results = [
               cell.text.strip()
               for cell in driver.find_elements(By.CSS_SELECTOR, '.rt-tbody .rt-tr-group .rt-td:nth-child(4)')
               if cell.text.strip() != ''
          ]
     with allure.step('Сравнение результатов'):
          assert all(email in res for res in results), f"Поиск не сработал для {email}"

     driver.quit()





@allure.title('Этот тест проверяет поиск по полю Age')
@allure.description('''Поиск по полю Age''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("015")
@allure.manual
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/AS6wKNQ0/15-%D0%BF%D0%B7-004-%D0%BF%D0%BE%D0%B8%D1%81%D0%BA-%D0%BF%D0%BE-%D0%B2%D0%BE%D0%B7%D1%80%D0%BE%D1%81%D1%82%D1%83",name="ПЗ-004")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
def test_demoqa_pz_004():

     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     with allure.step('Поиск возроста в таблице'):
          ages = [
               cell.text.strip()
               for cell in driver.find_elements(By.CSS_SELECTOR, '.rt-tbody .rt-tr-group .rt-td:nth-child(3)')
               if cell.text.strip() != ''
          ]

          print(f"Список имён: {ages}")

     with allure.step('Перебор всех возростов в строке поиска'):
          for age in ages:
               search_box = driver.find_element(By.ID, 'searchBox')
               search_box.clear()
               time.sleep(0.5)
               search_box.send_keys(age)

     with allure.step('Получение возроста во время поиска'):
          results = [
               cell.text.strip()
               for cell in driver.find_elements(By.CSS_SELECTOR, '.rt-tbody .rt-tr-group .rt-td:nth-child(3)')
               if cell.text.strip() != ''
          ]
     with allure.step('Сравнение результатов'):
          assert all(age in res for res in results), f"Поиск не сработал для {age}"

     driver.quit()





@allure.title('Этот тест проверяет поиск по полю Salary')
@allure.description('''Поиск по полю Salary''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("016")
@allure.manual
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/gVDb5tBE/16-%D0%BF%D0%B7-005-%D0%BF%D0%BE%D0%B8%D1%81%D0%BA-%D0%BF%D0%BE-%D0%B7%D0%BF",name="ПЗ-005")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
def test_demoqa_pz_005():

     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     with allure.step('Поиск всех Salary в таблице'):
          salarys = [
               cell.text.strip()
               for cell in driver.find_elements(By.CSS_SELECTOR, '.rt-tbody .rt-tr-group .rt-td:nth-child(5)')
               if cell.text.strip() != ''
          ]

          print(f"Список имён: {salarys}")

     with allure.step('Перебор всех Salary в строке поиска'):
          for salary in salarys:
               search_box = driver.find_element(By.ID, 'searchBox')
               search_box.clear()
               time.sleep(0.5)
               search_box.send_keys(salary)

     with allure.step('Получение Salary во время поиска'):
          results = [
               cell.text.strip()
               for cell in driver.find_elements(By.CSS_SELECTOR, '.rt-tbody .rt-tr-group .rt-td:nth-child(5)')
               if cell.text.strip() != ''
          ]
     with allure.step('Сравнение результатов'):
          assert all(salary in res for res in results), f"Поиск не сработал для {salary}"

     driver.quit()





@allure.title('Этот тест проверяет поиск по полю Department')
@allure.description('''Поиск по полю Department''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("017")
@allure.manual
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/nkp55SUs/18-%D0%BF%D0%B7-006-%D0%BF%D0%BE%D0%B8%D1%81%D0%BA-%D0%BF%D0%BE-%D0%BE%D1%82%D0%B4%D0%B5%D0%BB%D1%83",name="ПЗ-006")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
def test_demoqa_pz_006():

     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     with allure.step('Поиск всех Department в таблице'):
          departments = [
               cell.text.strip()
               for cell in driver.find_elements(By.CSS_SELECTOR, '.rt-tbody .rt-tr-group .rt-td:nth-child(5)')
               if cell.text.strip() != ''
          ]

          print(f"Список имён: {departments}")

     with allure.step('Перебор всех Department в строке поиска'):
          for department in departments:
               search_box = driver.find_element(By.ID, 'searchBox')
               search_box.clear()
               time.sleep(0.5)
               search_box.send_keys(department)

     with allure.step('Получение Department во время поиска'):
          results = [
               cell.text.strip()
               for cell in driver.find_elements(By.CSS_SELECTOR, '.rt-tbody .rt-tr-group .rt-td:nth-child(5)')
               if cell.text.strip() != ''
          ]
     with allure.step('Сравнение результатов'):
          assert all(department in res for res in results), f"Поиск не сработал для {department}"

     driver.quit()





@allure.title('Этот тест проверяет поиск по несуществующим даным')
@allure.description('''Поиск по не существующим данным''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("018")
@allure.manual
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/VwBI8kYX/17-%D0%BF%D0%B7-007-%D0%BF%D0%BE%D0%B8%D1%81%D0%BA-%D0%BF%D0%BE-%D0%BD%D0%B5-%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D1%83%D1%8E%D1%89%D0%B8%D0%BC-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%BC",name="ПЗ-007")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
def test_demoqa_pz_007():

     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     with allure.step('Поиск по несуществующей записи в таблице'):
          search_box = driver.find_element(By.ID, 'searchBox')
          search_box.clear()
          search_box.send_keys('qwerty123!@#')  # точно несуществующее значение

     with allure.step('Проверка на отсуствие записей'):
          no_rows_message = driver.find_element(By.CLASS_NAME, 'rt-noData').text
          assert no_rows_message == 'No rows found', "Ожидалось, что данных не будет"

     driver.quit()





@allure.title('Этот тест проверяет пагинацию по 5 записям')
@allure.description('''Пагинация по 5 записям''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("018")
@allure.manual
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/kyXtFGly/21-%D0%BF-001-%D0%BF%D0%B0%D0%B3%D0%B8%D0%BD%D0%B0%D1%86%D0%B8%D1%8F-5-%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D0%B5%D0%B9",name="П-001")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
def test_demoqa_p_001():
     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     first_names = ["Peter", "Bruce", "Tony", "Steve", "Natasha", "Clint", "Wanda", "Scott", "Stephen", "Carol"]
     last_names = ["Parker", "Wayne", "Stark", "Rogers", "Romanoff", "Barton", "Maximoff", "Lang", "Strange", "Danvers"]
     emails = [
          "peter@mail.com", "bruce@mail.com", "tony@mail.com", "steve@mail.com", "natasha@mail.com",
          "clint@mail.com", "wanda@mail.com", "scott@mail.com", "stephen@mail.com", "carol@mail.com"
     ]
     ages = ["21", "35", "48", "33", "29", "38", "27", "32", "42", "36"]
     salaries = ["10000", "15000", "20000", "25000", "12000", "18000", "16000", "22000", "30000", "27000"]
     departments = ["QA", "Dev", "PM", "HR", "Design", "Support", "Ops", "Security", "R&D", "Marketing"]

     rows_per_page=5

     with allure.step(f'Отображение 100 записей в таблице'):
          select_element = driver.find_element(By.CSS_SELECTOR, 'select[aria-label="rows per page"]')
          select_element.click()
          driver.find_element(By.CSS_SELECTOR, 'select[aria-label="rows per page"] option[value="100"]').click()

     with allure.step(f'Заполнение таблицы 10 записями'):
          for i in range(10):
               with allure.step(f'Заполнение формы #{i+1}'):

                    with allure.step('Открытие формы заполнения'):
                         time.sleep(0.1)
                         driver.find_element(By.ID, 'addNewRecordButton').click()

                    time.sleep(0.1)

                    fields = [
                         ("First Name", '[placeholder="First Name"]', first_names[i]),
                         ("Last Name", '[placeholder="Last Name"]', last_names[i]),
                         ("Email", '[placeholder="name@example.com"]', emails[i]),
                         ("Age", '[placeholder="Age"]', ages[i]),
                         ("Salary", '[placeholder="Salary"]', salaries[i]),
                         ("Department", '[placeholder="Department"]', departments[i])
                    ]

                    for field_name, selector, value in fields:
                         element = driver.find_element(By.CSS_SELECTOR, selector)
                         with allure.step(f'Очистка поля {field_name}'):
                              element.clear()
                         with allure.step(f'Заполнение поля {field_name}'):
                              element.send_keys(value)
                    time.sleep(0.1)

               with allure.step('Нажатие кнопки Submit'):
                    driver.find_element(By.ID, 'submit').click()

     with allure.step('Проверка количества записей в таблице'):
          rows = driver.find_elements(By.CSS_SELECTOR, '.rt-table .rt-tr-group')
          non_empty_rows_to = []

          for row in rows:
               cells = row.find_elements(By.CSS_SELECTOR, '.rt-td')
               if any(cell.text.strip() != '' for cell in cells):
                    non_empty_rows_to.append(row)

          with allure.step(f'Количество записей {len(non_empty_rows_to)}'):
               print(f'Количество записей в таблице: {len(non_empty_rows_to)}')


          pages = (len(non_empty_rows_to)+rows_per_page-1) // rows_per_page
          with allure.step(f'Количество страниц, которое должно отобразится - {pages}'):
               print(pages)

     driver.execute_script("window.scrollBy(0, 10000);")
     time.sleep(0.1)


     with allure.step(f'Отображение 5 записей в таблице'):
          select_element = driver.find_element(By.CSS_SELECTOR, 'select[aria-label="rows per page"]')
          select_element.click()
          driver.find_element(By.CSS_SELECTOR, 'select[aria-label="rows per page"] option[value="5"]').click()

     buttons = driver.find_elements(By.CSS_SELECTOR, '[type="button"]')
     button = buttons[3]
     # button.click()

     with allure.step(f'Проверка пагинации'):
          for i in range(pages - 1):
               with allure.step(f'Переход на страницу {i+2}'):
                    assert button.is_enabled(), f"Кнопка 'Next' должна быть активна на странице {i + 1}"
                    button.click()

               time.sleep(0.5)

               buttons = driver.find_elements(By.CSS_SELECTOR, '[type="button"]')
               button = buttons[3]

     with allure.step(f'Проверка, на то, что больше нет страниц для перехода'):
          assert not button.is_enabled(), "Кнопка 'Next' должна быть неактивна на последней странице"


     time.sleep(0.5)
     driver.quit()





@allure.title('Этот тест проверяет пагинацию по 10 записям')
@allure.description('''Пагинация по 5 записям''')
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("019")
@allure.manual
@allure.issue("https://trello.com/b/Hre2AC4l/qatest-casedemoqa", name="WT-001")
@allure.testcase("https://trello.com/c/K1ou7Rct/22-%D0%BF-002-%D0%BF%D0%B0%D0%B3%D0%B8%D0%BD%D0%B0%D1%86%D0%B8%D1%8F-%D0%BF%D0%B5%D1%80%D0%B5%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D1%8B-%D0%B2%D0%BF%D0%B5%D1%80%D0%B5%D0%B4",name="П-002")
@allure.epic("Функциональные автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
def test_demoqa_p_002():
     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/webtables")
     driver.maximize_window()

     first_names = [
          "Peter", "Bruce", "Tony", "Steve", "Natasha", "Clint", "Wanda", "Scott", "Stephen", "Carol",
          "Sam", "Bucky", "Nick", "Maria", "Peggy", "Shuri", "Hope", "Jane", "Loki", "Gamora"
     ]

     last_names = [
          "Parker", "Wayne", "Stark", "Rogers", "Romanoff", "Barton", "Maximoff", "Lang", "Strange", "Danvers",
          "Wilson", "Barnes", "Fury", "Hill", "Carter", "T'Challa", "Van Dyne", "Foster", "Laufeyson", "Zen-Whoberi"
     ]

     emails = [
          "peter@mail.com", "bruce@mail.com", "tony@mail.com", "steve@mail.com", "natasha@mail.com",
          "clint@mail.com", "wanda@mail.com", "scott@mail.com", "stephen@mail.com", "carol@mail.com",
          "sam@mail.com", "bucky@mail.com", "nick@mail.com", "maria@mail.com", "peggy@mail.com",
          "shuri@mail.com", "hope@mail.com", "jane@mail.com", "loki@mail.com", "gamora@mail.com"
     ]

     ages = [
          "21", "35", "48", "33", "29", "38", "27", "32", "42", "36",
          "31", "39", "50", "28", "34", "26", "30", "37", "45", "29"
     ]

     salaries = [
          "10000", "15000", "20000", "25000", "12000", "18000", "16000", "22000", "30000", "27000",
          "14000", "19500", "21000", "15500", "17000", "13000", "18500", "24000", "26000", "17500"
     ]

     departments = [
          "QA", "Dev", "PM", "HR", "Design", "Support", "Ops", "Security", "R&D", "Marketing",
          "QA", "Dev", "PM", "HR", "Design", "Support", "Ops", "Security", "R&D", "Marketing"
     ]

     rows_per_page=10

     with allure.step(f'Отображение 100 записей в таблице'):
          select_element = driver.find_element(By.CSS_SELECTOR, 'select[aria-label="rows per page"]')
          select_element.click()
          driver.find_element(By.CSS_SELECTOR, 'select[aria-label="rows per page"] option[value="100"]').click()

     with allure.step(f'Заполнение таблицы 20 записями'):
          for i in range(20):
               with allure.step(f'Заполнение формы #{i+1}'):

                    with allure.step('Открытие формы заполнения'):
                         time.sleep(0.1)
                         driver.find_element(By.ID, 'addNewRecordButton').click()

                    time.sleep(0.1)

                    fields = [
                         ("First Name", '[placeholder="First Name"]', first_names[i]),
                         ("Last Name", '[placeholder="Last Name"]', last_names[i]),
                         ("Email", '[placeholder="name@example.com"]', emails[i]),
                         ("Age", '[placeholder="Age"]', ages[i]),
                         ("Salary", '[placeholder="Salary"]', salaries[i]),
                         ("Department", '[placeholder="Department"]', departments[i])
                    ]

                    for field_name, selector, value in fields:
                         element = driver.find_element(By.CSS_SELECTOR, selector)
                         with allure.step(f'Очистка поля {field_name}'):
                              element.clear()
                         with allure.step(f'Заполнение поля {field_name}'):
                              element.send_keys(value)
                    time.sleep(0.1)

               with allure.step('Нажатие кнопки Submit'):
                    driver.find_element(By.ID, 'submit').click()

     with allure.step('Проверка количества записей в таблице'):
          rows = driver.find_elements(By.CSS_SELECTOR, '.rt-table .rt-tr-group')
          non_empty_rows_to = []

          for row in rows:
               cells = row.find_elements(By.CSS_SELECTOR, '.rt-td')
               if any(cell.text.strip() != '' for cell in cells):
                    non_empty_rows_to.append(row)

          with allure.step(f'Количество записей {len(non_empty_rows_to)}'):
               print(f'Количество записей в таблице: {len(non_empty_rows_to)}')


          pages = (len(non_empty_rows_to)+rows_per_page-1) // rows_per_page
          with allure.step(f'Количество страниц, которое должно отобразится - {pages}'):
               print(pages)

     driver.execute_script("window.scrollBy(0, 10000);")
     time.sleep(0.1)


     with allure.step(f'Отображение 5 записей в таблице'):
          select_element = driver.find_element(By.CSS_SELECTOR, 'select[aria-label="rows per page"]')
          select_element.click()
          driver.find_element(By.CSS_SELECTOR, 'select[aria-label="rows per page"] option[value="10"]').click()

     buttons = driver.find_elements(By.CSS_SELECTOR, '[type="button"]')
     button = buttons[3]
     # button.click()

     with allure.step(f'Проверка пагинации'):
          for i in range(pages - 1):
               with allure.step(f'Переход на страницу {i+2}'):
                    assert button.is_enabled(), f"Кнопка 'Next' должна быть активна на странице {i + 1}"
                    button.click()

               time.sleep(0.5)

               buttons = driver.find_elements(By.CSS_SELECTOR, '[type="button"]')
               button = buttons[3]

     with allure.step(f'Проверка, на то, что больше нет страниц для перехода'):
          assert not button.is_enabled(), "Кнопка 'Next' должна быть неактивна на последней странице"


     time.sleep(0.5)
     driver.quit()