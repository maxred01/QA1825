import allure
from tehno.page.base_page import WebPage
from tehno.page.elements import WebElement
from tehno.locators.main_locators import MainPage
from selenium.webdriver.support import expected_conditions as EC

def test_shop(web_browser):
    with allure.step('Запуск и настройка браузера'):
        driver = MainPage(web_browser)

    # with allure.step('Скроллим страницу'):
    #     driver._web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    with allure.step('Нажать на кнопку "Shop"'):
        driver.Shop.click()

    with allure.step('Проверяем, что открылась страница "Shop"'):
        current_url = "https://shop.spacex.com/"
        print("Текущий URL:", current_url)
        assert current_url == "https://shop.spacex.com/", \
        f"Ожидали страницу 'Shop', а открылась {current_url}"