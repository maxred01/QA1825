import time
import allure
from maksim_tsybulka.class_work.class_work_16.locators.shop_locators import ShopPage
import pytest_check as check
from maksim_tsybulka.class_work.class_work_16.data.constans import ImgConsts as Ic


@allure.feature("Страница 'Shop'")
@allure.story("Проверка наличия картинок")
def test_headers(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = ShopPage(web_browser)

        with allure.step('Проверка наличия картинки'):
            check.equal(driver.btn_header_1.get_attribute('data-srcset'), Ic.STARSHIP_TORCH, 'Картинка изменилась или ее нет на экарне')

        with allure.step('Проверка числа товаров'):
            check.equal(driver.product_item.count(), 23, 'Неверное число товаров на ветрине')

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
