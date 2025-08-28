import time
import allure
from Valeria_Pavlovich.Class_work.Class_work_17.locators.main_locators import MainPage
import pytest_check as check

@allure.feature('Main page')
@allure.story('Header')
def test_buttons(web_browser):
    with allure.step('Browser start'):
        driver = MainPage(web_browser)

    with allure.step('Test data preparation'):
        elements = [
            (driver.menu_btn, 'Menu'),
            (driver.language_btn, 'Language'),
            (driver.account_btn, 'Account'),
            (driver.bad_vision_version, 'Bad vision'),
            (driver.belavia_logo, 'Logo'),
        ]
    with allure.step('Element test'):
        for element, text_element in elements:
            with allure.step(f'Element {text_element} visibility test'):
                check.is_true(element.is_visible(), f'Element {text_element} is not visible')
            with allure.step(f'Element {text_element} clickability test'):
                check.is_true(element.is_clickable(), f'Element {text_element} is not clickable')

@allure.feature('Main page')
@allure.story('Footer')
def test_buttons(web_browser):
    with allure.step('Browser start'):
        driver = MainPage(web_browser)

    with allure.step('Test data preparation'):
        elements = [
            (driver.support_service, 'Support service'),
            (driver.sales_office, 'Sales office'),
            (driver.timetable, 'Timetable'),
            (driver.departure_arrival, 'Departure'),
            (driver.citizen_request, 'Citizen request'),
            (driver.cargo_transport, 'Cargo transportation'),
            (driver.for_agents, 'For agents'),
            (driver.on_air_magazine, 'OnAir magazine'),
            (driver.feedback, 'Feedback'),
            (driver.media_contact, 'Media contact'),
            (driver.improvement_year, 'Improvement year'),
            (driver.facebook, 'Facebook'),
            (driver.twitter, 'Twitter'),
            (driver.instagram, 'Instagram'),
            (driver.youtube, 'Youtube'),
            (driver.vk, 'VKontakte'),
            (driver.telegram, 'Telegram')
        ]
    with allure.step('Element test'):
        for element, text_element in elements:
            with allure.step(f'Element {text_element} visibility test'):
                assert element.is_visible(), f'Element {text_element} is not visible'
            with allure.step(f'Element {text_element} clickability test'):
                assert element.is_clickable(), f'Element {text_element} is not clickable'
