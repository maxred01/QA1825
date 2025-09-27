import time
import allure
import uuid


from Valery_Hehenia.Class_work.Class_work_18.locators.locators_main_page import MainPage
from das_magaz.conftest import webdriver
from das_magaz.conftest import chrome_options, web_browser
import pytest_check as check
from allure_commons.types import LabelType




def generate_random_message():
    email = f"{uuid.uuid4().hex[:10]}@email.com"
    name = f"Nick_{uuid.uuid4().hex[:8]}"
    message = f"Message{uuid.uuid4().hex[:30]}"
    return email, name, message


def generate_long_message():
    email = f"{uuid.uuid4().hex[:10]}@email.com"
    name = f"Nick_{uuid.uuid4().hex[:8]}"
    long_message = ''.join([uuid.uuid4().hex for _ in range(32)])[:1000]
    return email, name, long_message




@allure.feature("Модальное окно Contact")
@allure.story("Отправка пустой формы")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/aDU5Cbo8/28-mc-002-%D0%B2%D0%B0%D0%BB%D0%B8%D0%B4%D0%BD%D0%B0%D1%8F-%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0", "MC-001")
def test_submitting_empty_form(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)

    with allure.step('Нажатие кнопки Contact'):
        driver.contact_btn.click()
        time.sleep(1)


    with (allure.step('Подготовка тестовых данных')):
        email = ''
        name = ''
        message = ''


    with allure.step('Заполнение полей email, name и message'):
        driver.contact_email.send_keys(email)
        driver.contact_name.send_keys(name)
        driver.contact_message.send_keys(message)


    with allure.step('Нажатие кнопки Send message'):
        driver.contact_send_message.click()
        time.sleep(1)


    with allure.step('Проверка отправки сообщения'):
            alert = web_browser.switch_to.alert
            check.is_in("Please fill in all fields!", alert.text, "Сообщение имеет другое содержимое!")
            alert.accept()



@allure.feature("Модальное окно Contact")
@allure.story("Валидная отправка")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/aDU5Cbo8/28-mc-002-%D0%B2%D0%B0%D0%BB%D0%B8%D0%B4%D0%BD%D0%B0%D1%8F-%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0", "MC-002")
def test_submitting_form_with_valid_data(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)

    with allure.step('Нажатие кнопки Contact'):
        driver.contact_btn.click()
        time.sleep(1)


    with (allure.step('Подготовка тестовых данных')):
        email, name, message = generate_random_message()


    with allure.step('Заполнение полей email, name и message'):
        driver.contact_email.send_keys(email)
        driver.contact_name.send_keys(name)
        driver.contact_message.send_keys(message)


    with allure.step('Нажатие кнопки Send message'):
        driver.contact_send_message.click()
        time.sleep(1)


    with allure.step('Проверка отправки сообщения'):
            alert = web_browser.switch_to.alert
            check.is_in("Thanks for the message!!", alert.text, "Сообщение имеет другое содержимое!")
            alert.accept()



@allure.feature("Модальное окно Contact")
@allure.story("Неверный email")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/htXLW9Z9/29-mc-003-%D0%BD%D0%B5%D0%B2%D0%B5%D1%80%D0%BD%D1%8B%D0%B9-email", "MC-003")
def test_submitting_no_email(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)

    with allure.step('Нажатие кнопки Contact'):
        driver.contact_btn.click()
        time.sleep(1)


    with (allure.step('Подготовка тестовых данных')):
        email, name, message = generate_random_message()
        email = f'Email@'


    with allure.step('Заполнение полей email, name и message'):
        driver.contact_email.send_keys(email)
        driver.contact_name.send_keys(name)
        driver.contact_message.send_keys(message)


    with allure.step('Нажатие кнопки Send message'):
        driver.contact_send_message.click()
        time.sleep(1)


    with allure.step('Проверка отправки сообщения'):
            alert = web_browser.switch_to.alert
            check.is_in("Invalid Email!!", alert.text, "Сообщение имеет другое содержимое!")
            alert.accept()




@allure.feature("Модальное окно Contact")
@allure.story("Пустое имя")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/w9Dqfx9Q/30-mc-004-%D0%BF%D1%83%D1%81%D1%82%D0%BE%D0%B5-%D0%B8%D0%BC%D1%8F", "MC-004")
def test_submitting_no_name(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)

    with allure.step('Нажатие кнопки Contact'):
        driver.contact_btn.click()
        time.sleep(1)


    with (allure.step('Подготовка тестовых данных')):
        email, name, message = generate_random_message()
        name = f''


    with allure.step('Заполнение полей email, name и message'):
        driver.contact_email.send_keys(email)
        driver.contact_name.send_keys(name)
        driver.contact_message.send_keys(message)


    with allure.step('Нажатие кнопки Send message'):
        driver.contact_send_message.click()
        time.sleep(1)


    with allure.step('Проверка отправки сообщения'):
            alert = web_browser.switch_to.alert
            check.is_in("Fill in the name!!", alert.text, "Сообщение имеет другое содержимое!")
            alert.accept()



@allure.feature("Модальное окно Contact")
@allure.story("Пустое сообщение")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/mrlLiCJY/31-mc-005-%D0%BF%D1%83%D1%81%D1%82%D0%BE%D0%B5-%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D0%B5", "MC-005")
def test_submitting_no_message(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)

    with allure.step('Нажатие кнопки Contact'):
        driver.contact_btn.click()
        time.sleep(1)


    with (allure.step('Подготовка тестовых данных')):
        email, name, message = generate_random_message()
        message= f''


    with allure.step('Заполнение полей email, name и message'):
        driver.contact_email.send_keys(email)
        driver.contact_name.send_keys(name)
        driver.contact_message.send_keys(message)


    with allure.step('Нажатие кнопки Send message'):
        driver.contact_send_message.click()
        time.sleep(1)


    with allure.step('Проверка отправки сообщения'):
            alert = web_browser.switch_to.alert
            check.is_in("The message cannot be empty!!", alert.text, "Сообщение имеет другое содержимое!")
            alert.accept()



@allure.feature("Модальное окно Contact")
@allure.story("Длинный ввод в Message")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/BRwkiTaj/26-mc-006-%D0%B4%D0%BB%D0%B8%D0%BD%D0%BD%D1%8B%D0%B9-%D0%B2%D0%B2%D0%BE%D0%B4-%D0%B2-message", "MC-006")
def test_submitting_long_message(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)

    with allure.step('Нажатие кнопки Contact'):
        driver.contact_btn.click()
        time.sleep(1)


    with (allure.step('Подготовка тестовых данных')):
        email, name, long_message = generate_long_message()


    with allure.step('Заполнение полей email, name и message'):
        driver.contact_email.send_keys(email)
        driver.contact_name.send_keys(name)
        driver.contact_message.send_keys(long_message)


    with allure.step('Нажатие кнопки Send message'):
        driver.contact_send_message.click()
        time.sleep(1)


    with allure.step('Проверка отправки сообщения'):
            alert = web_browser.switch_to.alert
            check.is_in("The message is too long in format.!!", alert.text, "Сообщение имеет другое содержимое!")
            alert.accept()