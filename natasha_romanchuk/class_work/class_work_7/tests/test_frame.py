from nuts_nuts_nuts.page1.base_page import WebPage
from nuts_nuts_nuts.page1.elements import WebElement
from nuts_nuts_nuts.Locators.main_locators import MainPage
from selenium.webdriver.support import expected_conditions as EC

def test_kontakty(web_browser):
    # with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    # with allure.step("Скроллим страницу вниз"):
        driver._web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # with allure.step('Нажимаем на кнопку "Контакты" в футуре'):
        driver.contacty_button.click()
    # with allure.step("Проверяем, что открылась страница Контакты"):
        current_url = "https://emall.by/information/company/contacts"
        # print("Текущий URL:", current_url)
        assert current_url == "https://emall.by/information/company/contacts", \
            f"Ожидали страницу Контакты, а открылась {current_url}"

