import time
import allure
from bachko_irina.class_work.class_work_12.locators.main_locators import MainPage


@allure.feature("раздел Elements")
@allure.story("Вкладка upload-download")
def test_buttons(web_browser):
    with allure.step('Запуск и настройка браузера'):
        driver = MainPage(web_browser)


    with allure.step('Двойной клик'):
            driver.double_click_btn.double_click()
            time.sleep(2)
            assert not driver.double_click_message.is_visible()


    with allure.step('Клик правой кнопкой мыши'):
            driver.right_click_btn.right_mouse_click()
            time.sleep(2)





