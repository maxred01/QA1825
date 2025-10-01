import time
import allure
import pytest_check as check

from Valery_Hehenia.Class_work.Class_work_18.locators.locators_main_page import MainPage
from das_magaz.conftest import webdriver
from das_magaz.conftest import chrome_options, web_browser
from allure_commons.types import LabelType


@allure.feature("Главная страница")
@allure.story("Хедер")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/42sS4Esu/46-%D0%B3%D1%81-001-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D1%85%D0%B5%D0%B4%D0%B5%D1%80%D0%B0",
                 "ГС-001"
)
def test_headers(web_browser, chrome_options):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)


    with allure.step('Подготовка тестовых данных'):
        elements = [
            (driver.logo_btn, 'Лого'),
             (driver.home_btn, 'Home'),
             (driver.contact_btn, 'Contact'),
             (driver.about_btn, 'About'),
             (driver.cart_btn, 'Cart'),
             (driver.login_btn, 'Log in'),
             (driver.sugnup_btn, 'Sign un'),
                    ]

    with allure.step('Проверка элемента'):
        for element, text_element in elements:
            with allure.step(f'Проверка элемента {text_element} на отображение'):
                check.is_true(element.is_visible(), f'Элемента {text_element} нет визуально на экарне')

            with allure.step(f'Проверка элемента {text_element} на кликабельность'):
                check.is_true(element.is_clickable(), f'Элемента {text_element} не кликабелен')


@allure.feature("Главная страница")
@allure.story("Футер")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/Vb9yHM3L/47-%D0%B3%D1%81-002-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D1%84%D1%83%D1%82%D0%B5%D1%80%D0%B0",
                 "ГС-002"
)
def test_footers(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)


    with allure.step('Подготовка тестовых данных'):
        elements = [
             (driver.about_text, 'About US'),
             (driver.text_text, 'Текст'),
             (driver.get_intouch_text, 'Get in Touch'),
             (driver.address_text, 'Address'),
             (driver.phone_text, 'Phone'),
             (driver.email_text, 'Email'),
             (driver.product_text, 'PRODUCT STORE'),
                    ]

    with allure.step('Проверка элемента'):
        for element, text_element in elements:
            with allure.step(f'Проверка элемента {text_element} на отображение'):
                check.is_true(element.is_visible(), f'Элемента {text_element} нет визуально на экарне')

            with allure.step(f'Проверка элемента {text_element} на кликабельность'):
                check.is_true(element.is_clickable(), f'Элемента {text_element} не кликабелен')



@allure.feature("Главная страница")
@allure.story("Категории")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/wwhfdi0s/48-%D0%B3%D1%81-003-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D0%B1%D0%BB%D0%BE%D0%BA%D0%B0-%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B9",
                 "ГС-003"
)
def test_categories(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        time.sleep(1)


    with allure.step('Подготовка тестовых данных'):
        elements = [
             (driver.cat_block, 'Блок Categories'),
             (driver.cat_phones, 'Phones'),
             (driver.cat_laptops, 'Laptops'),
             (driver.cat_monitors, 'Monitors'),
                    ]

    with allure.step('Проверка элемента'):
        for element, text_element in elements:
            with allure.step(f'Проверка элемента {text_element} на отображение'):
                check.is_true(element.is_visible(), f'Элемента {text_element} нет визуально на экарне')

            with allure.step(f'Проверка элемента {text_element} на кликабельность'):
                check.is_true(element.is_clickable(), f'Элемента {text_element} не кликабелен')



@allure.feature("Главная страница")
@allure.story("Карусель")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/9Lre6icM/49-%D0%B3%D1%81-004-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D0%BA%D0%B0%D1%80%D1%83%D1%81%D0%B5%D0%BB%D0%B8",
                 "ГС-004"
)
def test_carusel_click(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        time.sleep(1)


    with allure.step('Подготовка тестовых данных'):
        elements = [
             (driver.carusel_block, 'Блок Карусели'),
             (driver.carusel_btn_next, 'Кнопка вперед'),
             (driver.carusel_btn_previous, 'Кнопка назад'),
                    ]

    with allure.step('Проверка элемента'):
        for element, text_element in elements:
            with allure.step(f'Проверка элемента {text_element} на отображение'):
                check.is_true(element.is_visible(), f'Элемента {text_element} нет визуально на экарне')

            with allure.step(f'Проверка элемента {text_element} на кликабельность'):
                check.is_true(element.is_clickable(), f'Элемента {text_element} не кликабелен')



@allure.feature("Главная страница")
@allure.story("Карусель")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/lckYdPiu/45-%D0%B3%D1%81-004-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D0%BA%D0%B0%D1%80%D1%83%D1%81%D0%B5%D0%BB%D0%B8",
                 "ГС-005"
)
def test_carusel_slide(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)

    with allure.step('Подготовка тестовых данных'):
        slides = [driver.carusel_img_samsung,
                  driver.carusel_img_nexus,
                  driver.carusel_img_iphone,
                  ]

    with allure.step('Проверка слайда по стрелке вправо'):
        assert driver.carusel_img_samsung.is_visible(), f"Слайд 1 не отображается!"
        print(f"Слайд 1 отображается")

        for i, slide in enumerate(slides):
            assert slide.is_visible(), f"Слайд {i + 1} не отображается!"
            print(f"Слайд {i + 1} отображается")

            if i < len(slides) - 1:
                driver.carusel_btn_next.click()
                time.sleep(0.5)


    with allure.step('Проверка слайда по стрелке влево'):
        for i in range(len(slides) - 1, -1, -1):  # Индексы: 2, 1, 0
            current_slide = slides[i]
            assert current_slide.is_visible(), f"Слайд {i + 1} не отображается!"
            print(f"Слайд {i + 1} отображается")

            if i > 0:
                driver.carusel_btn_previous.click()
                time.sleep(0.5)