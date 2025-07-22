from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
from allure_commons.types import LabelType
from allure_commons.types import Severity
import pytest_check as check

def test_selenium():
     full_name = 'Peter Parket'
     email = 'test@test.com'
     current_address = 'Minsk'
     permanent_address = 'New York'

     driver = webdriver.Chrome()
     driver.get("https://demoqa.com/text-box")
     driver.maximize_window()

     driver.find_element(By.CSS_SELECTOR, '[placeholder="Full Name"]').send_keys(full_name)
     driver.find_element(By.CSS_SELECTOR, '[placeholder="name@example.com"]').send_keys(email)
     driver.find_element(By.CSS_SELECTOR, '[placeholder="Current Address"]').send_keys(current_address)
     driver.find_element(By.CSS_SELECTOR, '[id="permanentAddress"]').send_keys(permanent_address)

     #Скрол на определенное кол-во пикселей
     driver.execute_script("window.scrollTo(0, 50);")

     #Скрол в конец всей старницы
     #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);)")

     #скрол через нажатие кнопки
     # driver.find_element(By.CSS_SELECTOR, '[id="submit"]').send_keys(Keys.ARROW_DOWN)


     time.sleep(2)

     driver.find_element(By.CSS_SELECTOR, '[id="submit"]').click()

     time.sleep(1)


     elements = driver.find_elements(By.XPATH, "//p[@class='mb-1']")
     for el in elements:
          print(el.text)


     #Поиск через совпадения
     assert elements[0].text.find(full_name) > -1
     assert elements[1].text.find(email) > -1
     assert elements[2].text.find(current_address) > -1
     assert elements[3].text.find(permanent_address) > -1


     assert elements[0].text == f'Name:{full_name}'
     assert elements[1].text == f'Email:{email}'
     assert elements[2].text == f'Current Address :{current_address}'
     assert elements[3].text == f'Permananet Address :{permanent_address}'

     #Поиск совпадений через pycheck (есть возможность проверки, даже если есть ошибки)
     check.greater(elements[0].text.find(full_name), -1, 'Error')
     check.greater(elements[1].text.find(email), -1, 'Error')
     check.greater(elements[2].text.find(current_address), -1, 'Error')
     check.greater(elements[3].text.find(permanent_address), -1, 'Error')


     driver.quit()

#Вариант через картеж и цикл
@allure.title('Этот тест проверяет выполнение результат заполнения формы')
@allure.description('''Тест вводит текст в поля и сверяет результат п полях''')
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
@allure.story("Вкладка Test Box")
def test_selenium_2():
     with allure.step('Подготовка тестовых данных'):

          user_name = 'Peter Parket'
          user_email = 'test@test.com'
          current_address = 'Minsk'
          permanent_address = 'New York'

     with allure.step('Запускаем браузер'):
          driver = webdriver.Chrome()
          driver.get("https://demoqa.com/text-box")
          driver.maximize_window()
     time.sleep(1)




     elemets_form_send_keys = [
          (driver.find_element(By.ID, 'userName'), 'Full Name', user_name),
          (driver.find_element(By.ID, 'userEmail'), 'Email', user_email),
          (driver.find_element(By.ID, 'currentAddress'), 'Current Address', current_address),
          (driver.find_element(By.ID, 'permanentAddress'), 'Permanent Address', permanent_address)
     ]
     for element, text_elemet, send_keys_element in elemets_form_send_keys:
          with allure.step(f'Ввод текста для поля {text_elemet}'):
               element.send_keys(send_keys_element)

     time.sleep(2)

     with allure.step('Скрол страницы вниз'):
          driver.execute_script("window.scrollBy(0, 50);")
          driver.find_element(By.ID, 'submit').send_keys(Keys.DOWN)

     with allure.step('Нажатие кнопки Submit'):
          driver.find_element(By.ID, 'submit').click()

     output_form = driver.find_element(By.ID, 'output')

     assert output_form.is_displayed(), 'Результат формы не появился на экарне'

     elemets_form = [
          (driver.find_element(By.ID, 'name'), user_name, 'Name'),
          (driver.find_element(By.ID, 'email'), user_email, 'Email'),
          (driver.find_element(By.XPATH, '//p[@id="currentAddress"]'), current_address, 'Current Address'),
          (driver.find_element(By.XPATH, '//p[@id="permanentAddress"]'), permanent_address, 'Permanent Address')
     ]
     for elemet, elemets_text, name_form in elemets_form:
          with allure.step(f'Проверка поля {name_form}'):
               check.greater(elemet.text.find(elemets_text), -1, f"Текста {elemets_text} нет на экарне")

     time.sleep(2)
     driver.quit()