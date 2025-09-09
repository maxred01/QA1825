
from bachko_irina.class_work.class_work_12.locators.locators_corz import MainPage
import pytest_check as check
import allure
from tehno.conftest import web_browser
from tehno.conftest import chrome_options

@allure.feature("раздел Elements")
@allure.story("Header")
def test_heders(web_browser, chrome_options):
    with allure.step('Запуск и настройка браузера'):
        driver = MainPage(web_browser)


    with allure.step('Подготовка тестовых данных'):
        elements = [
            (driver.Logo, 'spacex-logo'),
            (driver.Vehicles, 'Vehicles'),
            (driver.Launches,'Launches'),
            (driver.HumanSpaceflight,'Human Spaceflight'),