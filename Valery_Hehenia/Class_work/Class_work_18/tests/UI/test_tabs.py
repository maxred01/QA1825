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

def generate_random_user():
    username = f"user_{uuid.uuid4().hex[:6]}"
    password = f"pass_{uuid.uuid4().hex[:8]}"
    return username, password


@allure.feature("Пекреходы по вкладкам")
@allure.story("Переход по вкладке Home")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/LaJNdl3q/13-%D0%B2%D0%BD-001-%D0%BF%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4-%D0%BF%D0%BE-%D0%B2%D0%BA%D0%BB%D0%B0%D0%B4%D0%BA%D0%B5-home", "ВН-001")
def test_open_home_tab(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)

    with allure.step('Нажатие кнопки Home'):
        driver.home_btn.click()
        time.sleep(1)
    with allure.step('Проверка отображения элементов вкладки'):
        assert driver.slider_block.is_visible()




@allure.feature("Пекреходы по вкладкам")
@allure.story("Переход по вкладке Contact")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/i677mbhh/15-%D0%B2%D0%BD-002-%D0%BF%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4-%D0%BF%D0%BE-%D0%B2%D0%BA%D0%BB%D0%B0%D0%B4%D0%BA%D0%B5-contact","ВН-002")
def test_open_contact_tab(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)

    with allure.step('Нажатие кнопки Contact'):
        driver.contact_btn.click()
        time.sleep(1)
    with allure.step('Проверка отображения элементов вкладки'):
        assert driver.contact_modal.is_visible()




@allure.feature("Пекреходы по вкладкам")
@allure.story("Переход по вкладке About us")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/5sMkbfAz/16-%D0%B2%D0%BD-003-%D0%BF%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4-%D0%BF%D0%BE-%D0%B2%D0%BA%D0%BB%D0%B0%D0%B4%D0%BA%D0%B5-about-us","ВН-003")
def test_open_about_us_tab(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)

    with allure.step('Нажатие кнопки About us'):
        driver.about_btn.click()
        time.sleep(1)
    with allure.step('Проверка отображения элементов вкладки'):
        assert driver.about_us_modal.is_visible()


@allure.feature("Пекреходы по вкладкам")
@allure.story("Переход по вкладке Cart")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/rUD39COc/17-%D0%B2%D0%BD-004-%D0%BF%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4-%D0%BF%D0%BE-%D0%B2%D0%BA%D0%BB%D0%B0%D0%B4%D0%BA%D0%B5-cart","ВН-004")
def test_open_cart_tab(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)

    with allure.step('Нажатие кнопки Cart'):
        driver.cart_btn.click()
        time.sleep(1)
    with allure.step('Проверка отображения элементов вкладки'):
        assert driver.cart_title.is_visible()



@allure.feature("Пекреходы по вкладкам")
@allure.story("Переход по вкладке Log in")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/FQGCB61g/14-%D0%B2%D0%BD-005-%D0%BF%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4-%D0%BF%D0%BE-%D0%B2%D0%BA%D0%BB%D0%B0%D0%B4%D0%BA%D0%B5-log-in","ВН-005")
def test_open_login_tab(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)

    with allure.step('Нажатие кнопки Log in'):
        driver.login_btn.click()
        time.sleep(1)
    with allure.step('Проверка отображения элементов вкладки'):
        assert driver.login_modal.is_visible()




@allure.feature("Пекреходы по вкладкам")
@allure.story("Переход по вкладке Sign up")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/G5AGzDnP/18-%D0%B2%D0%BD-006-%D0%BF%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4-%D0%BF%D0%BE-%D0%B2%D0%BA%D0%BB%D0%B0%D0%B4%D0%BA%D0%B5-sign-up","ВН-006")
def test_open_signup_tab(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)

    with allure.step('Нажатие кнопки Sign up'):
        driver.sugnup_btn.click()
        time.sleep(1)
    with allure.step('Проверка отображения элементов вкладки'):
        assert driver.signup_modal.is_visible()




@allure.feature("Пекреходы по вкладкам")
@allure.story("Поведение окна Contact после закрытия")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/m5r5uPsD/20-%D0%B2%D0%BD-007-%D0%BF%D0%BE%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BE%D0%BA%D0%BD%D0%B0-contact-%D0%BF%D0%BE%D1%81%D0%BB%D0%B5-%D0%B7%D0%B0%D0%BA%D1%80%D1%8B%D1%82%D0%B8%D1%8F","ВН-007")
def test_contact_modal_clears_after_close(web_browser):
    driver = MainPage(web_browser)
    time.sleep(0.5)

    with allure.step('Подготовка тестовых данных'):
        email, name ,message = generate_random_message()


    with allure.step('Нажатие кнопки Contact'):
        driver.contact_btn.click()
        time.sleep(0.5)


    with allure.step('Заполнение полей email, name и message'):
        driver.contact_email.send_keys(email)
        driver.contact_name.send_keys(name)
        driver.contact_message.send_keys(message)


    with allure.step('Закрыть окно (через кнопку Close)'):
        driver.contact_button_close.click()
        time.sleep(0.5)


    with allure.step('Снова открыть Contact'):
        driver.contact_btn.click()
        time.sleep(1)


    with allure.step('Проверка, что поля пустые'):
        check.equal(driver.contact_email.get_attribute("value"), "", "Поле Email не пустое")
        check.equal(driver.contact_name.get_attribute("value"), "", "Поле Name не пустое")
        check.equal(driver.contact_message.get_attribute("value"), "", "Поле Message не пустое")




@allure.feature("Пекреходы по вкладкам")
@allure.story("Поведение окна Log in после закрытия")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/zByzA3dm/21-%D0%B2%D0%BD-008-%D0%BF%D0%BE%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BE%D0%BA%D0%BD%D0%B0-log-in-%D0%BF%D0%BE%D1%81%D0%BB%D0%B5-%D0%B7%D0%B0%D0%BA%D1%80%D1%8B%D1%82%D0%B8%D1%8F","ВН-008")
def test_login_modal_clears_after_close(web_browser):
    driver = MainPage(web_browser)
    time.sleep(0.5)

    with allure.step('Подготовка тестовых данных'):
        username, password = generate_random_user()


    with allure.step('Нажатие кнопки Log in'):
        driver.login_btn.click()
        time.sleep(0.5)


    with allure.step('Заполнение полей username и password'):
        driver.login_username.send_keys(username)
        driver.login_password.send_keys(password)


    with allure.step('Закрыть окно (через кнопку Close)'):
        driver.login_button_close.click()
        time.sleep(0.5)


    with allure.step('Снова открыть Log in'):
        driver.login_btn.click()
        time.sleep(1)


    with allure.step('Проверка, что поля пустые'):
        check.equal(driver.login_username.get_attribute("value"), "", "Поле Username не пустое")
        check.equal(driver.login_password.get_attribute("value"), "", "Поле Password не пустое")





@allure.feature("Пекреходы по вкладкам")
@allure.story("ППоведение окна Sign up после закрытия")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/a12qjcM3/22-%D0%B2%D0%BD-009-%D0%BF%D0%BE%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BE%D0%BA%D0%BD%D0%B0-sign-up-%D0%BF%D0%BE%D1%81%D0%BB%D0%B5-%D0%B7%D0%B0%D0%BA%D1%80%D1%8B%D1%82%D0%B8%D1%8F","ВН-009")
def test_signup_modal_clears_after_close(web_browser):
    driver = MainPage(web_browser)
    time.sleep(0.5)

    with allure.step('Подготовка тестовых данных'):
        username, password = generate_random_user()


    with allure.step('Нажатие кнопки Sign up'):
        driver.sugnup_btn.click()
        time.sleep(0.5)


    with allure.step('Заполнение полей username и password'):
        driver.signup_username.send_keys(username)
        driver.signup_password.send_keys(password)


    with allure.step('Закрыть окно (через кнопку Close)'):
        driver.signup_button_close.click()
        time.sleep(0.5)


    with allure.step('Снова открыть Sign up'):
        driver.sugnup_btn.click()
        time.sleep(1)


    with allure.step('Проверка, что поля пустые'):
        check.equal(driver.signup_username.get_attribute("value"), "", "Поле Username не пустое")
        check.equal(driver.signup_password.get_attribute("value"), "", "Поле Password не пустое")



@allure.feature("Переходы по вкладкам")
@allure.story("Проверка закрытия всех модальных окон через крестик")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/8YQCTBJP/25-%D0%B2%D0%BD-011-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D0%B7%D0%B0%D0%BA%D1%80%D1%8B%D1%82%D0%B8%D1%8F-%D0%B2%D1%81%D0%B5%D1%85-%D0%BC%D0%BE%D0%B4%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D1%85-%D0%BE%D0%BA%D0%BE%D0%BD-%D1%87%D0%B5%D1%80%D0%B5%D0%B7-%D0%BA%D1%80%D0%B5%D1%81%D1%82%D0%B8%D0%BA","ВН-011")
def test_closing_modal_close(web_browser):
    driver = MainPage(web_browser)
    time.sleep(0.5)


    with allure.step('Нажатие кнопки Contact '):
        driver.contact_btn.click()
        time.sleep(0.5)
        with allure.step('Закрыть окно (через кнопку Close)'):
            driver.contact_button_close.click()
            time.sleep(0.5)


    with allure.step('Нажатие кнопки About Us'):
        driver.about_btn.click()
        time.sleep(0.5)
        with allure.step('Закрыть окно (через кнопку Close)'):
            driver.aboutus_button_close.click()
            time.sleep(0.5)


    with allure.step('Нажатие кнопки Log in '):
        driver.login_btn.click()
        time.sleep(0.5)
        with allure.step('Закрыть окно (через кнопку Close)'):
            driver.login_button_close.click()
            time.sleep(0.5)


    with allure.step('Нажатие кнопки ASign Up'):
        driver.sugnup_btn.click()
        time.sleep(0.5)
        with allure.step('Закрыть окно (через кнопку Close)'):
            driver.signup_button_close.click()
            time.sleep(0.5)



@allure.feature("Переходы по вкладкам")
@allure.story("Проверка закрытия всех модальных окон через кнопку Close")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/RhfDgfC3/24-%D0%B2%D0%BD-011-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D0%B7%D0%B0%D0%BA%D1%80%D1%8B%D1%82%D0%B8%D1%8F-%D0%B2%D1%81%D0%B5%D1%85-%D0%BC%D0%BE%D0%B4%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D1%85-%D0%BE%D0%BA%D0%BE%D0%BD-%D1%87%D0%B5%D1%80%D0%B5%D0%B7-%D0%BA%D0%BD%D0%BE%D0%BF%D0%BA%D1%83-close","ВН-012")
def test_closing_modal_x(web_browser):
    driver = MainPage(web_browser)
    time.sleep(0.5)


    with allure.step('Нажатие кнопки Contact '):
        driver.contact_btn.click()
        time.sleep(0.5)
        with allure.step('Закрыть окно (через x)'):
            driver.contact_button_x.click()
            time.sleep(0.5)


    with allure.step('Нажатие кнопки About Us'):
        driver.about_btn.click()
        time.sleep(0.5)
        with allure.step('Закрыть окно (через x)'):
            driver.aboutus_button_x.click()
            time.sleep(0.5)


    with allure.step('Нажатие кнопки Log in '):
        driver.login_btn.click()
        time.sleep(0.5)
        with allure.step('Закрыть окно (через x)'):
            driver.login_button_x.click()
            time.sleep(0.5)


    with allure.step('Нажатие кнопки ASign Up'):
        driver.sugnup_btn.click()
        time.sleep(0.5)
        with allure.step('Закрыть окно (через x)'):
            driver.signup_button_x.click()
            time.sleep(0.5)