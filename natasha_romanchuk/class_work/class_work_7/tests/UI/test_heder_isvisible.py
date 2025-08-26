import time
import allure
from selenium.webdriver.common.by import By

from natasha_romanchuk.class_work.class_work_7.Locators.main_locators import MainPage


@allure.feature("Раздел Elements")
@allure.story("Вкладка Heder")
def test_button(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)

    with allure.step('Отображение элементов хэдэра'):
        elements = [
            ("строка поиска", driver.search_input),
            ("строка поиска", driver.search_input),
            ("иконка поиска", driver.search_button),
            ("кнопка каталог", driver.catalog_button),
            ("войти", driver.action_button_enter),
            ("заказы", driver.action_button_orders),
            ("избранное", driver.action_button_favorites),
            ("корзина", driver.action_button_basket),
            ("акции", driver.actions_button),
            ("товары-везунчики", driver.lucky_goods_button),
            ("промокоды", driver.promocodes_button),
            ("новинки", driver.new_button),
            ("срочный товар", driver.urgent_goods_button),
            ("упаковкой выгоднее", driver.take_more_button),
            ("наушники беспроводные", driver.naushniki_besprovodnye_button),
            ("школа", driver.school_button),
            ("детская стирка", driver.detskaya_stirka_button),

        ]

        for name, locator in elements:
            with allure.step(f"Отображение: {name}"):
                assert locator.is_visible(), f"Элемент '{name}' не отображается"
