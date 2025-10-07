from maksim_tsybulka.class_work.class_work_16.locators.locators_eng import EngPage
import pytest_check as check
import allure
from super_puper_frame.conftest import web_browser
from super_puper_frame.conftest import chrome_options


@allure.feature("Главная страница")
@allure.story("Хедер")
def test_headers(web_browser, chrome_options):
    with allure.step('Запускаем и настройка браузер'):
        driver = EngPage(web_browser)
        driver.btn_cooke.click()

        assert driver.btn_news_all_main.count() == 22, 'Число плиток на главной стринице неверное'
