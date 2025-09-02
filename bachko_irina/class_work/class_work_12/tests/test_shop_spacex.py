import time
import allure
from selenium.webdriver.support.expected_conditions import element_located_selection_state_to_be

from bachko_irina.class_work.class_work_12.locators.spacex_locator import ShopPage
import pytest_check as check
from bachko_irina.class_work.class_work_12.class_work_122.date.constans import ImgConsts as Ic

@allure.feature("Страница 'Shop'")
@allure.story("Проверка наличия картинок")
def test_heders(web_browser):
    with allure.step('Запуск и настройка браузера'):
        driver = ShopPage(web_browser)

        with allure.step('Проверка наличия картинки'):
            check.equal(driver.btn_heder_1.get_attribute('data-srcset'), Ic.STARSHIP_TORCH, 'Картинка изменилась или ее нет на экране')

        with allure.step('Проверка наименования товара'):
            results = driver.btn_heder_1.get_text()('STARSHIP TORCH')
            check.equal(results, Ic.STARSHIP_TORCH, 'Картинка изменилась или ее нет на экране')

        with allure.step('Проверка наименования товаров'):
            check.equal(driver.text_price_1.get_text(),'175', 'Цена отличается')

        with allure.step('Проверка числа товаров'):
            check.equal(driver.product_item.count(), 23, 'Неверное число товаров на витрине')


#     with allure.step('Подготовка тестовых данных'):
#         elements = [
#             (driver.Logo, 'spacex-logo'),
#             (driver.Vehicles, 'Vehicles'),
#             (driver.Launches,'Launches'),
#             (driver.HumanSpaceflight,'Human Spaceflight'),
#             (driver.Rideshare,'Rideshare'),
#             (driver.Starlink,'Starlink'),
#             (driver.Starshield,'Starshield'),
#             (driver.Company,'Company'),
#             (driver.Shop,'Shop'),
#
#             ]
#
#     with allure.step('Проверка элемента'):
#         for element, text_element in elements:
#             with allure.step(f'Проверка элемента {text_element} на отображение'):
#                 check.is_true(element.is_visible(), f'Элемента {text_element} нет визуально на экарне')
#
#             with allure.step(f'Проверка элемента {text_element} на кликабельность'):
#                 check.is_true(element.is_clickable(), f'Элемента {text_element} не кликабелен')
#
# @allure.feature("Главная страница")
# @allure.story("Footer")
# def test_footers(web_browser):
#     with allure.step('Запускаем и настройка браузер'):
#             driver = MainPage(web_browser)
#
#     with allure.step('Подготовка тестовых данных'):
#             elements = [
#                 (driver.Vehicles, 'Vehicles'),
#                 (driver.Careers, 'Careers'),
#                 (driver.Updates, 'Updates'),
#                 (driver.Privacy, 'Privacy'),
#                 (driver.Policy, 'Policy'),
#                 (driver.Suppliers, 'Suppliers'),
#             ]
#
#     with allure.step('Проверка элемента'):
#         for element, text_element in elements:
#             with allure.step(f'Проверка элемента {text_element} на отображение'):
#                     check.is_true(element.is_visible(), f'Элемента {text_element} нет визуально на экарне')
#
#             with allure.step(f'Проверка элемента {text_element} на кликабельность'):
#                     check.is_true(element.is_clickable(), f'Элемента {text_element} не кликабелен')
#
#
#
