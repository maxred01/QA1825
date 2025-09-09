import time
import allure
from Valeria_Pavlovich.Class_work.Class_work_17.locators.search_locators import TicketSearch
import pytest_check as check
from B2_framework.conftest import web_browser
from B2_framework.conftest import chrome_options

@allure.feature('Главная страница')
@allure.story('Поиск билетов')
def test_ticket_search_elements(web_browser):
    with allure.step('Запускаем браузер'):
        driver = TicketSearch(web_browser)

    with allure.step('Подготавливаем тестовые данных'):
        elements = [
            (driver.dest_from, 'Откуда'),
            (driver.dest_to, 'Куда'),
            (driver.search_button, 'Найти'),
        ]
    with allure.step('Проверяем основные элементы поля поиска'):
        for element, text_element in elements:
            with allure.step(f'Проверяем видимость элемента {text_element}'):
                check.is_true(element.is_visible(), f'Элемент {text_element} не отображается на экране')
            with allure.step(f'Проверяем нажатие элемента {text_element}'):
                check.is_true(element.is_clickable(), f'Элемент {text_element} не нажимается')

    with allure.step('Проверяем дополнительные элементы поля поиска'):
        driver.dest_from.click()
        elements = [
            (driver.one_way, 'В одну сторону'),
            (driver.return_way, 'Туда-обратно'),
            (driver.dept_datepicker, 'Дата туда'),
            (driver.return_datepicker, 'Дата обратно'),
            (driver.passengers, 'Пассажиры'),
            (driver.promo, 'Промокод'),
            (driver.point_pay, 'Оплата баллами')

        ]
        for element, text_element in elements:
            with allure.step(f'Проверяем видимость элемента {text_element}'):
                check.is_true(element.is_visible(), f'Элемент {text_element} не отображается на экране')
            with allure.step(f'Проверяем нажатие элемента {text_element}'):
                check.is_true(element.is_clickable(), f'Элемент {text_element} не нажимается')
                time.sleep(1)

