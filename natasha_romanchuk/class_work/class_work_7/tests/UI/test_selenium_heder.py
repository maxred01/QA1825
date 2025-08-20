import time
import allure
from allure_commons.types import LabelType # импорт специального перечисления из allure(epic,feature,story,severity...)
from selenium import webdriver
from selenium.webdriver.common.by import By # стратегии поиска элементов
from selenium.webdriver.common.keys import Keys # виртуальное представление клавиш клавиатуры
from selenium.webdriver.common.action_chains import ActionChains # двойной клик,выпадающие меню, перетаскиваемые элементы, элементы с hover-эффектами и других
import pytest_check as check # предоставляет функционал "мягких assertions" (soft assertions) для тестирования в Python
from natasha_romanchuk.class_work.class_work_7.conftest import web_browser
from natasha_romanchuk.class_work.class_work_7.tests.Locators.locator_button import LocatorButton

@allure.feature("Header Navigation")
@allure.story("Visual Elements Display")
@allure.severity(allure.severity_level.NORMAL)
def test_header_logo_displayed(web_browser):
    driver = web_browser
    driver.get('https://emall.by/')

    with allure.step('Отображение логотипа'):
        logo = driver.find_element(By.XPATH, LocatorButton.logotip)
        assert logo.is_displayed()

    with allure.step('Отображение строки поиска'):
        search  = driver.find_element(By.XPATH, LocatorButton.search_input)
        assert logo.is_displayed()

    with allure.step('Отображение иконки поиска'):
        search  = driver.find_element(By.XPATH, LocatorButton.search_button)
        assert logo.is_displayed()
