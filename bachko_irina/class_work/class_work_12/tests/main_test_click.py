import time
import allure
from bachko_irina.class_work.class_work_12.locators.main_locators import MainPage


@allure.feature("раздел Elements")
@allure.story("Вкладка Header")
def test_button_main(web_browser):
    with allure.step('Запуск и настройка браузера'):
        driver = MainPage(web_browser)


        with allure.step('Отображение элементов header'):
            elements = [
                ("button vehicles ", driver.vehicles),
                ("button launches", driver.launches),
                ("button humanspaceflight", driver.humanspaceflight),
                ("button rideshare", driver.rideshare),
                ("button starlink", driver.starlink),
                ("button starshield", driver.starshield),


            ]

            for name, locator in elements:
                with allure.step(f"Отображение: {name}"):
                    assert locator.is_visible(), f"Элемент '{name}' не отображается"
            time.sleep(2)





