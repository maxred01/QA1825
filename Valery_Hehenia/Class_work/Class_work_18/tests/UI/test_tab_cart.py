import time
import allure
import uuid
import random


from Valery_Hehenia.Class_work.Class_work_18.locators.locators_main_page import MainPage
from das_magaz.conftest import webdriver
from das_magaz.conftest import chrome_options, web_browser
import pytest_check as check
from allure_commons.types import LabelType




def generate_order_data():
    """Генерация случайных данных для формы Place Order."""
    data = {
        "name": f"Name_{uuid.uuid4().hex[:8]}",
        "country": f"Country_{uuid.uuid4().hex[:6]}",
        "city": f"City_{uuid.uuid4().hex[:6]}",
        "credit_card": f"{random.randint(1000_0000_0000_0000, 9999_9999_9999_9999)}",
        "month": f"{random.randint(1, 12)}",
        "year": f"{random.randint(2025, 2035)}"
    }
    return data





@allure.feature("Вкладка Cart")
@allure.story("Проверка отображения пустой корзины")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/XTbalOmx/34-bc-001-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D0%BE%D1%82%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BF%D1%83%D1%81%D1%82%D0%BE%D0%B9-%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D1%8B", "BC-001")
def test_empty_cart(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)

    with allure.step("Открытие страницы корзины"):
        driver.cart_btn.click()
        time.sleep(1)

    with allure.step("Проверить, что корзина пуста"):
        check.equal(len(driver.cart_items), 0, "Корзина не пустая — в ней есть товары")

    with allure.step("Проверить наличие кнопки Place Order"):
        check.is_true(driver.place_order_btn.is_visible(),
                      "Кнопка Place Order не отображается")



@allure.feature("Вкладка Cart")
@allure.story("Добавление товара в корзину")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/HOCnhAUw/35-bc-002-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0-%D0%B2-%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D1%83", "BC-002")
def test_add_product_to_cart(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)


    with allure.step("Выбрать первый товар"):
        first_product = driver.product_items[0]  # ManyWebElements
        first_product.click()
        time.sleep(1)

        with allure.step("Добавить товар в корзину"):
            driver.add_to_cart_btn.click()
            time.sleep(0.5)
            with allure.step("Проверка и подтверждение окна подтверждения"):
                alert = web_browser.switch_to.alert
                alert_text = alert.text
                alert.accept()
                check.is_true("Product added" in alert_text,
                              f"Alert не содержит 'Product added', текст: {alert_text}")

    with allure.step("Перейти в корзину"):
        driver.cart_btn.click()
        time.sleep(0.5)

    with allure.step("Проверить, что товар отображается в корзине"):
        check.is_true(len(driver.cart_items) > 0,
                      "Товар не появился в корзине")

        product_name = driver.cart_items[0].find_element("xpath", ".//td[2]").text
        check.is_true(len(product_name) > 0, "Название товара пустое")




@allure.feature("Вкладка Cart")
@allure.story("Удаление товара из корзины")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/Di1XADTk/36-bc-003-%D1%83%D0%B4%D0%B0%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0-%D0%B8%D0%B7-%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D1%8B", "BC-003")
def test_remove_product_to_cart(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)


    with allure.step("Выбрать первый товар"):
        first_product = driver.product_items[0]
        first_product.click()
        time.sleep(1)

        with allure.step("Добавить товар в корзину"):
            driver.add_to_cart_btn.click()
            time.sleep(0.5)
            with allure.step("Проверка и подтверждение окна подтверждения"):
                alert = web_browser.switch_to.alert
                alert_text = alert.text
                alert.accept()
                check.is_true("Product added" in alert_text,
                              f"Alert не содержит 'Product added', текст: {alert_text}")

    with allure.step("Перейти в корзину"):
        driver.cart_btn.click()
        time.sleep(0.5)

        with allure.step("Проверить, что товар отображается в корзине"):
                initial_count = len(driver.cart_items)
                check.is_true(initial_count > 0, "Корзина пуста, нечего удалять")

    with allure.step("Удалить первый товар из корзины"):
        driver.remove_to_cart_btn.click()
        time.sleep(1)

    with allure.step("Проверить, что товар удалён"):
        new_count = len(driver.cart_items)
        check.is_true(new_count < initial_count, "Товар не был удалён из корзины")





@allure.feature("Вкладка Cart")
@allure.story("Проверка суммы корзины")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/kE7AjLi2/37-bc-004-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D1%81%D1%83%D0%BC%D0%BC%D1%8B-%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D1%8B", "BC-004")
def test_cart_total_sum(web_browser):
    driver = MainPage(web_browser)
    time.sleep(0.5)


    with allure.step("Добавляем товары в корзину"):
        for i in range(3):
            with allure.step(f"Добавляем товар #{i+1}"):
                product = driver.product_items[i]
                product.click()
                time.sleep(0.5)
                driver.add_to_cart_btn.click()
                time.sleep(0.5)

                with allure.step("Проверка и подтверждение окна подтверждения"):
                    alert = web_browser.switch_to.alert
                    alert.accept()
                    time.sleep(1)
                    driver.logo_btn.click()

    with allure.step("Перейти в корзину"):
        driver.cart_btn.click()
        time.sleep(1)

    with allure.step("Считать цены товаров и сумму"):
        total_calculated = 0
        for item in driver.cart_items:
            price_text = item.find_element("xpath", ".//td[3]").text
            price = int(price_text)
            total_calculated += price

    with allure.step("Получаем сумму товаров"):
        total_displayed_text = driver.total_sum.find().text
        total_displayed = int(total_displayed_text)

        with allure.step("Проверяем сумму товаров"):
            check.equal(total_calculated, total_displayed,
                        f"Сумма товаров {total_calculated} не совпадает с отображаемой {total_displayed}")




@allure.feature("Вкладка Cart")
@allure.story("Проверка кнопки Place Order")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase("https://trello.com/c/GaWoLZWQ/38-bc-005-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D0%BA%D0%BD%D0%BE%D0%BF%D0%BA%D0%B8-place-order", "BC-005")
def test_place_order_modal(web_browser):
    driver = MainPage(web_browser)
    time.sleep(0.5)

    with allure.step("Выбрать первый товар"):
        first_product = driver.product_items[0]
        first_product.click()
        time.sleep(1)

        with allure.step("Добавить товар в корзину"):
            driver.add_to_cart_btn.click()
            time.sleep(0.5)

        with allure.step("Проверка и подтверждение окна подтверждения"):
            alert = web_browser.switch_to.alert
            alert.accept()
            time.sleep(1)
            driver.logo_btn.click()


    with allure.step("Переход в корзину"):
        driver.cart_btn.click()
        time.sleep(1)

        with allure.step("Проверка, что в корзине есть товары"):
            check.is_true(len(driver.cart_items) > 0, "Корзина пуста, Place Order недоступен")

    with allure.step("Нажатие кнопки Place Order"):
        driver.place_order_btn.find().click()
        time.sleep(1)

    with allure.step("Проверка, что открылось модальное окно"):
        modal = driver.modal_order_place_order.find()  # локатор модального окна
        check.is_true(modal.is_displayed(), "Модальное окно Place Order не открылось")


@allure.feature("Вкладка Cart")
@allure.story("Проверка оформления заказа c валидными данными")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/XdouruGf/39-bc-006-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D0%BE%D1%84%D0%BE%D1%80%D0%BC%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B7%D0%B0%D0%BA%D0%B0%D0%B7%D0%B0-c-%D0%B2%D0%B0%D0%BB%D0%B8%D0%B4%D0%BD%D1%8B%D0%BC%D0%B8-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%BC%D0%B8",
    "BC-006")
def test_purchase_valid_data(web_browser):
    driver = MainPage(web_browser)
    time.sleep(0.5)

    with allure.step("Выбрать первый товар"):
        first_product = driver.product_items[0]
        first_product.click()
        time.sleep(1)

        with allure.step("Добавить товар в корзину"):
            driver.add_to_cart_btn.click()
            time.sleep(0.5)

            with allure.step("Проверка и подтверждение окна подтверждения"):
                alert = web_browser.switch_to.alert
                alert.accept()
                time.sleep(1)
                driver.logo_btn.click()

    with allure.step("Переход в корзину"):
        driver.cart_btn.click()
        time.sleep(1)

        with allure.step("Проверка, что в корзине есть товары"):
            check.is_true(len(driver.cart_items) > 0, "Корзина пуста, Place Order недоступен")

    with allure.step("Нажатие кнопки Place Order"):
        driver.place_order_btn.find().click()
        time.sleep(1)

        with allure.step("Проверка, что открылось модальное окно"):
            modal = driver.modal_order_place_order.find()  # локатор модального окна
            check.is_true(modal.is_displayed(), "Модальное окно Place Order не открылось")

            with allure.step('Заполнение полей'):
                order_data = generate_order_data()
                driver.name_input.send_keys(order_data["name"])
                driver.country_input.send_keys(order_data["country"])
                driver.city_input.send_keys(order_data["city"])
                driver.credit_card_input.send_keys(order_data["credit_card"])
                driver.month_input.send_keys(order_data["month"])
                driver.year_input.send_keys(order_data["year"])


    with allure.step('Нажатие кнопки Purchase'):
        driver.purchase_btn_place_order.click()
        time.sleep(1)

        with allure.step("Проверить сообщение об успешной покупке"):
            message = driver.purchase_success_modal.find().text
            check.is_true(order_data["name"] in message, "Имя не совпадает")
            check.is_true(order_data["credit_card"] in message, "Карта не совпадает")





@allure.feature("Вкладка Cart")
@allure.story("Проверка оформления заказа c пустыми полями")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/MKBcDfGX/33-bc-007-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D0%BE%D1%84%D0%BE%D1%80%D0%BC%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B7%D0%B0%D0%BA%D0%B0%D0%B7%D0%B0-c-%D0%BF%D1%83%D1%81%D1%82%D1%8B%D0%BC%D0%B8-%D0%BF%D0%BE%D0%BB%D1%8F%D0%BC%D0%B8",
    "BC-006")
def test_purchase_empty_data(web_browser):
    driver = MainPage(web_browser)
    time.sleep(0.5)

    with allure.step("Выбрать первый товар"):
        first_product = driver.product_items[0]
        first_product.click()
        time.sleep(1)

        with allure.step("Добавить товар в корзину"):
            driver.add_to_cart_btn.click()
            time.sleep(0.5)

            with allure.step("Проверка и подтверждение окна подтверждения"):
                alert = web_browser.switch_to.alert
                alert.accept()
                time.sleep(1)
                driver.logo_btn.click()

    with allure.step("Переход в корзину"):
        driver.cart_btn.click()
        time.sleep(1)

        with allure.step("Проверка, что в корзине есть товары"):
            check.is_true(len(driver.cart_items) > 0, "Корзина пуста, Place Order недоступен")

    with allure.step("Нажатие кнопки Place Order"):
        driver.place_order_btn.find().click()
        time.sleep(1)

        with allure.step("Проверка, что открылось модальное окно"):
            modal = driver.modal_order_place_order.find()  # локатор модального окна
            check.is_true(modal.is_displayed(), "Модальное окно Place Order не открылось")


    with allure.step('Нажатие кнопки Purchase'):
        driver.purchase_btn_place_order.click()
        time.sleep(1)

        with allure.step("Проверить alert с сообщением об обязательных полях"):
            alert = web_browser.switch_to.alert
            alert_text = alert.text
            alert.accept()  # обязательно закрываем alert
            check.is_true("Please fill out Name and Creditcard" in alert_text,
                          f"Ожидаемый alert не появился, текст: {alert_text}")