import time
import allure
from stasya_voishnis.class_work.class_work_16.locators.locators_button import ButtonPage

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
        driver.right_click_bth.right_click()
        time.sleep(2)

#
# @allure.feature("Раздел Elements")
# @allure.story("Вкладка Upload Download")
#
# def test_upload_download(web_browser):
#     with allure.step('Запускаем и настройка браузер'):
#         driver = web_browser
#         driver.get("https://demoqa.com/upload-download")
#
#     with allure.step(''):
#         driver.find_element(By.ID, LocatorsButton.upload_file).send_keys('/Users/maksimvaskevic/Documents/Настя/PycharmProjects/QA1825/README.md')
#         time.sleep(2)
