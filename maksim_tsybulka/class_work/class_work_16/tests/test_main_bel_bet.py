import random
import time
import allure
from maksim_tsybulka.class_work.class_work_16.locators.main_belbeat import MainPage
import pytest_check as check
from super_puper_frame.conftest import web_browser
from super_puper_frame.conftest import chrome_options
from selenium.webdriver.common.keys import Keys


@allure.feature("Главная страница")
@allure.story("Хедер")
def test_headers(web_browser, chrome_options):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        text = [
            'АУ!',
            'Тут есть кто?',
            'Как играть?',
            'Где ваша лицензия?',
            'Ты тут?',
            'Какой вейджер?',
            'В какую игру лучше играть?',
            'В какой игре я выиграю точно?',
                ]
        driver.btn_header_4.click()
        driver.btn_header_1.click()
        driver.btn_header_2.click()
        time.sleep(3)
        while True:
            random_text = random.choice(text)
            driver.btn_header_3.send_keys(random_text)
            driver.btn_header_3.send_keys(Keys.ENTER)
            time.sleep(5)


@allure.feature("Главная страница")
@allure.story("Хедер")
def test_headers(web_browser, chrome_options):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.btn_header_4.click()
        driver.btn_header_5.click()
        time.sleep(60)
        driver.move_to_element_and_click(411, 370)
        time.sleep(3)
