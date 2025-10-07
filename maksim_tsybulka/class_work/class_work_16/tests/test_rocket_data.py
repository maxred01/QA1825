import time

from maksim_tsybulka.class_work.class_work_16.locators.locators_rocket_data import RocketDataPage
import pytest_check as check
import allure
from super_puper_frame.conftest import web_browser
from super_puper_frame.conftest import chrome_options
from pyzbar import pyzbar
import cv2


@allure.feature("Главная страница")
@allure.story("Хедер")
def test_headers(web_browser, chrome_options):
    with allure.step('Запускаем и настройка браузер'):
        driver = RocketDataPage(web_browser)
        driver.btn_cookies.click()
        driver.resheniiya_btn.click()
        driver.upravlenie_dannymi_btn.move_to_element()
        driver.btn_header_3.move_to_element()
        time.sleep(3)


@allure.feature("Главная страница")
@allure.story("Чат")
def test_chat(web_browser, chrome_options):
    with allure.step('Запускаем и настройка браузер'):
        driver = RocketDataPage(web_browser)
        driver.btn_cookies.click()
        driver.btn_header_7.click(15)
        driver.btn_header_4.click()
        time.sleep(10)
        driver.btn_header_5.send_keys('ау, тут есть кто?')
        driver.btn_header_6.click()
        time.sleep(3)


@allure.feature("Главная страница")
@allure.story("Чат")
def test_qr(web_browser, chrome_options):
    with allure.step('Запускаем и настройка браузер'):
        driver = RocketDataPage(web_browser)
        driver.btn_cookies.click()
        driver.btn_header_8.click()
        time.sleep(3)
        driver.screenshot()
        filename = 'screenshot.png'  # Укажите путь к вашему QR-коду
        img = cv2.imread(filename)
        qrcodes = pyzbar.decode(img)
        for qrcode in qrcodes:
            # Данные, закодированные в QR-коде (в байтах)
            data = qrcode.data.decode('utf-8')

        assert data == 'tel:+79311065015'



