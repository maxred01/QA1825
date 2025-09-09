import time
import allure
from Valeria_Pavlovich.Class_work.Class_work_17.locators.main_locators import MainPage
import pytest_check as check
from B2_framework.conftest import web_browser
from B2_framework.conftest import chrome_options

@allure.feature('Главная страница')
@allure.story('Хэдер')
def test_header_elements(web_browser):
    with allure.step('Запускаем браузер'):
        driver = MainPage(web_browser)

    with allure.step('Подготавливаем тестовые данных'):
        elements = [
            (driver.belavia_logo, 'Логотип Белавиа'),
            (driver.bad_vision_version, 'Версия для слабовидящих'),
            (driver.account_btn, 'Личный аккаунт'),
            (driver.language_btn, 'Язык'),
            (driver.menu_btn, 'Меню'),
        ]
    with allure.step('Проверяем элементы хэдера'):
        for element, text_element in elements:
            with allure.step(f'Проверяем видимость элемента {text_element}'):
                check.is_true(element.is_visible(), f'Элемент {text_element} не отображается на экране')
            with allure.step(f'Проверяем нажатие элемента {text_element}'):
                check.is_true(element.is_clickable(), f'Элемент {text_element} не нажимается')

@allure.feature('Главная страница')
@allure.story('Слайдер')
def test_slider_elements(web_browser):
    with allure.step('Запускаем браузер'):
        driver = MainPage(web_browser)

    with allure.step('Подготавливаем тестовые данных'):
        elements = [
            (driver.slide_00, 'Слайд 1'),
            (driver.slide_01, 'Слайд 2'),
            (driver.slide_02, 'Слайд 3'),
            (driver.slide_03, 'Слайд 4'),
            (driver.slide_04, 'Слайд 5'),
            (driver.slide_05, 'Слайд 6'),
            (driver.slide_06, 'Слайд 7')
        ]
    with allure.step('Проверяем элементы слайдера'):
        for element, text_element in elements:
            with allure.step(f'Проверяем видимость элемента {text_element}'):
                check.is_true(element.is_visible(), f'Элемент {text_element} не отображается на экране')
            with allure.step(f'Проверяем нажатие элемента {text_element}'):
                check.is_true(element.is_clickable(), f'Элемент {text_element} не нажимается')
                time.sleep(5)


@allure.feature('Главная страница')
@allure.story('Футер')
def test_footer_elements(web_browser):
    with allure.step('Запускаем браузер'):
        driver = MainPage(web_browser)

    with allure.step('Подготавливаем тестовые данных'):
        elements = [
            (driver.support_service, 'Справочная служба'),
            (driver.contacts, 'Контакты'),
            (driver.email, 'Электронная почта'),
            (driver.official_name, 'Полное название компании'),
            (driver.address, 'Адрес головного офиса'),
            (driver.sales_office, 'Кассы продаж'),
            (driver.timetable, 'Расписание'),
            (driver.departure_arrival, 'Табло вылета/прилета'),
            (driver.citizen_request, 'Обращения граждан'),
            (driver.cargo_transport, 'Грузовые перевозки'),
            (driver.for_agents, 'Агентам'),
            (driver.on_air_magazine, 'Журнал OnAir'),
            (driver.feedback, 'Обратная связь'),
            (driver.media_contact, 'Для СМИ'),
            (driver.improvement_year, '2025 – Год благоустройства'),
            (driver.facebook, 'Facebook'),
            (driver.twitter, 'Twitter'),
            (driver.instagram, 'Instagram'),
            (driver.youtube, 'Youtube'),
            (driver.vk, 'Вконтакте'),
            (driver.telegram, 'Telegram')
        ]
    with allure.step('Проверяем элементы футера'):
        for element, text_element in elements:
            with allure.step(f'Проверяем видимость элемента {text_element}'):
                check.is_true(element.is_visible(), f'Элемент {text_element} не отображается на экране')
            with allure.step(f'Проверяем нажатие элемента {text_element}'):
                check.is_true(element.is_clickable(), f'Элемент {text_element} не нажимается')