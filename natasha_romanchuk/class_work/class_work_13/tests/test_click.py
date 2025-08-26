import time
import allure
from natasha_romanchuk.class_work.class_work_13.locators.locators_button import ButtonPage


@allure.feature("Раздел Elements")
@allure.story("Вкладка Button")
def test_button(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = ButtonPage(web_browser)

    with allure.step('Двойной клик'):
        driver.double_click_bth.double_click()
        time.sleep(2)
        assert not driver.double_click_message.is_visible()

    with allure.step('Клик правой кнопкой мыши'):
        driver.right_click_btn.right_mouse_click()
        time.sleep(2)