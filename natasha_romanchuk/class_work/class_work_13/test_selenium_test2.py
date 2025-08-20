import time
import allure
from allure_commons.types import LabelType

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pytest_check as check

@allure.title("Этот тест проверяет заполнение и результат заполнения формы")
@allure.description("""Тест вводит текст для полей user_name и тд и сверяет результат в полях name и тд""")
@allure.tag("Smoke")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.id("123")
@allure.manual
@allure.link("https://hoster.by/", name="Тест-кейсы теста")
@allure.issue("AUTH-123")
@allure.epic("UI автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Test Box")

def test_selenium():
    with allure.step('Подготовка тестовых даных'):
        user_name = 'Nata'
        user_email = 'nata@gmail.com'
        current_address = 'Minsk'
        permanent_address = 'Brest'

    with allure.step('Запускаем и настраиваем браузер'):
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
        element.send_keys(send_keys_element)

    time.sleep(2)
    with allure.step('Скролл страницы вниз'):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    with allure.step('Нажатие на кнопку "submit"'):
        driver.find_element(By.ID, 'submit').click()

    elemets_form = [
         (driver.find_element(By.ID, 'name'), user_name, 'Name'),
         (driver.find_element(By.ID, 'email'), user_email, 'Email'),
         (driver.find_element(By.XPATH, '//p[@id="currentAddress"]'), current_address, 'Current Address'),
         (driver.find_element(By.XPATH, '//p[@id="permanentAddress"]'), permanent_address, 'Permanent Address')
    ]
    for element, elemets_text, name_form in elemets_form:
        with allure.step(f'Проверка поля, {name_form}'):
            check.greater(element.text.find(elemets_text), -1, f"Текста {elemets_text} нет на экране")

    time.sleep(2)
    driver.quit()

############class_work_14######################test_clik
import time
import allure
from allure_commons.types import LabelType

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pytest_check as check
from natasha_romanchuk.class_work.conftest import web_browser
from natasha_romanchuk.class_work.class_work_13.locators.locators_button import LocatorsButton


@allure.feature("Раздел Elements")
@allure.story("Вкладка Buttons")
def test_selenium_button(web_browser):
    with allure.step('Запускаем и настраиваем браузер'):
        driver = web_browser
        driver.get("https://demoqa.com/buttons")

    with allure.step('Двойной клик'):
        elements_double_click_btn = driver.find_element(By.ID, LocatorsButton.double_click_btn).click()
        ActionChains(driver).double_click(elements_double_click_btn).perform()
        time.sleep(2)
        # assert not driver.find_element(By.ID, LocatorsButton.double_click_btn_message).is_displayed()

    with allure.step('Клик правой кнопной мыши'):
        elements_right_click_btn = driver.find_element(By.ID, LocatorsButton.right_click_btn)
        ActionChains(driver).context_click(elements_right_click_btn).perform()
        # assert driver.find_element(By.ID, 'rightClickMessage').text == 'You have done a right click'
        time.sleep(2)


    # with allure.step('Одиночный клик'):
    #     driver.find_element(By.ID, '(//*[contains(text(),'Click Me')])[3]').click()


@allure.feature("Раздел Elements")
@allure.story("Вкладка upload-download")
def test_selenium(web_browser):
    with allure.step('Запускаем и настраиваем браузер'):
        driver = web_browser
        driver.get("https://demoqa.com/upload-download")

    with allure.step('Upload'):  ###локатор обязательно с инпутом и путь к файлу с двойным слешем
        driver.find_element(By.ID, LocatorsButton.upload_click_btn).send_keys('C:\\Users\\natal\\OneDrive\\Изображения\\1-3.jpg')

        time.sleep(2)

####ФИКСТУРЫ######################
