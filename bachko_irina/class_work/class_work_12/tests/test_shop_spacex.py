import time
import allure

from bachko_irina.class_work.class_work_12.locators.spacex_locator import ShopPage
import pytest_check as check
from bachko_irina.class_work.class_work_12.class_work_122.data.constans import ImgConsts as Ic

@allure.feature("Страница 'Shop'")
@allure.story("Проверка наличия картинок")
def test_heders(web_browser):
    with allure.step('Запуск и настройка браузера'):
        driver = ShopPage(web_browser)

        with allure.step('Проверка наличия картинки'):
            check.equal(driver.btn_heder_1.get_attribute('data-srcset'), Ic.STARSHIP_TORCH, 'Картинка изменилась или ее нет на экране')

        with allure.step('Проверка числа товаров'):
            check.equal(driver.product_item.count(), 26, 'Неверное число товаров на витрине')

        with allure.step('Проверка числа товаров'):
            item = (
                {"Name": "STARSHIP TORCH\n$175"},
                {"Name": "UNISEX STARSHIP FLIGHT 10 T-SHIRT\n$35"},
                {"Name": "STARSHIP FLIGHT 10 MISSION PATCH\n$15"},
                    )

            containers = driver.product_item_2.get_text()

            for index, container in enumerate(containers):
                expected = item[index]
                assert container == expected['Name']