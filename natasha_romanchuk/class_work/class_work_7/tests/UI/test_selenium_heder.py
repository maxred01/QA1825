import allure
from selenium.webdriver.common.by import By # стратегии поиска элементов
from natasha_romanchuk.class_work.class_work_7.conftest import web_browser
from natasha_romanchuk.class_work.class_work_7.Locators.locator_button import LocatorButton

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
        search_btn  = driver.find_element(By.XPATH, LocatorButton.search_button)
        assert logo.is_displayed()
