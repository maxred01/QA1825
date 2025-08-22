import allure
from selenium.webdriver.common.by import By # стратегии поиска элементов
from natasha_romanchuk.class_work.class_work_7.tests.UI.conftest import web_browser
from natasha_romanchuk.class_work.class_work_7.Locators.locator_button import LocatorButton

@allure.feature("Header Navigation")
@allure.story("Visual Elements Display")
@allure.severity(allure.severity_level.NORMAL)
def test_header_elements_displayed(web_browser):
    driver = web_browser
    driver.get('https://emall.by/')

    elements = [
        ("логотип", LocatorButton.logotip),
        ("строка поиска", LocatorButton.search_input),
        ("иконка поиска", LocatorButton.search_button),
        ("кнопка каталог", LocatorButton.catalog_button),
        ("войти", LocatorButton.action_button_enter),
        ("заказы", LocatorButton.action_button_orders),
        ("избранное", LocatorButton.action_button_favorites),
        ("корзина", LocatorButton.action_button_basket),
        ("акции", LocatorButton.actions_button),
        ("товары-везунчики", LocatorButton.lucky_goods_button),
        ("промокоды", LocatorButton.promocodes_button),
        ("новинки", LocatorButton.new_button),
        ("срочный товар", LocatorButton.urgent_goods_button),
        ("упаковкой выгоднее", LocatorButton.take_more_button),
        ("наушники беспроводные", LocatorButton.naushniki_besprovodnye_button),
        ("школа", LocatorButton.school_button),
        ("детская стирка", LocatorButton.detskaya_stirka_button),

    ]

    for name, locator in elements:
        with allure.step(f"Отображение: {name}"):
            elem = driver.find_element(By.XPATH, locator)
            assert elem.is_displayed(), f"Элемент '{name}' не отображается"




    # with allure.step('Отображение логотипа'):
    #     logo = driver.find_element(By.XPATH, LocatorButton.logotip)
    #     assert logo.is_displayed()
    #
    # with allure.step('Отображение строки поиска'):
    #     search  = driver.find_element(By.XPATH, LocatorButton.search_input)
    #     assert search.is_displayed()
    #
    # with allure.step('Отображение иконки поиска'):
    #     search_btn  = driver.find_element(By.XPATH, LocatorButton.search_button)
    #     assert search_btn.is_displayed()
    #
    # with allure.step('Отображение кнопки каталог'):
    #     catalog_btn  = driver.find_element(By.XPATH, LocatorButton.catalog_button)
    #     assert catalog_btn.is_displayed()