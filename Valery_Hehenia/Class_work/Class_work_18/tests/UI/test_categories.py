import time
import allure
import random

from Valery_Hehenia.Class_work.Class_work_18.locators.locators_main_page import MainPage
from Valery_Hehenia.Class_work.Class_work_18.data.products import phones, laptops, monitors

from das_magaz.conftest import webdriver
from das_magaz.conftest import chrome_options, web_browser
import pytest_check as check
from allure_commons.types import LabelType






@allure.feature("Главная страница")
@allure.story("Товары по категориям")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/jUSUP3aw/41-%D1%82%D0%BA-001-%D0%BF%D0%B5%D1%80%D0%B5%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B9-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%BE%D0%B2",
                 "ТК-001"
)
def test_products_by_category(web_browser):
    with allure.step('Запускаем и настраиваем браузер'):
        driver = MainPage(web_browser)
        time.sleep(1)

    categories = [
        (driver.cat_phones, "Phones", phones),
        (driver.cat_laptops, "Laptops", laptops),
        (driver.cat_monitors, "Monitors", monitors),
    ]

    for cat_element, cat_name, expected_products in categories:
        with allure.step(f'Проверяем категорию {cat_name}'):
            cat_element.click()
            time.sleep(1)

            displayed_products = driver.get_all_products()

            for product in expected_products:
                with allure.step(f'Проверяем, что товар "{product}" отображается'):
                    check.is_true(product in displayed_products,
                                  f"Товар {product} не отображается в категории {cat_name}")



@allure.feature("Главная страница")
@allure.story("Количество товаров в категории")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/BrhdFLLD/42-%D1%82%D0%BA-002-%D0%BA%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%BE%D0%B2-%D0%B2-%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B8",
                 "ТК-002"
)
def test_products_count_by_category(web_browser):
    with allure.step('Запускаем и настраиваем браузер'):
        driver = MainPage(web_browser)
        time.sleep(1)

    categories = [
        (driver.cat_phones, "Phones", phones),
        (driver.cat_laptops, "Laptops", laptops),
        (driver.cat_monitors, "Monitors", monitors),
    ]

    for cat_element, cat_name, expected_products in categories:
        with allure.step(f'Проверяем категорию {cat_name}'):
            cat_element.click()
            time.sleep(1)

            displayed_products = driver.get_all_products()

            with allure.step(f'Проверяем количество товаров в категории {cat_name}'):
                check.equal(len(displayed_products), len(expected_products),
                            f"Количество товаров в категории {cat_name} не соответствует ожидаемому")




@allure.feature("Главная страница")
@allure.story("Переключение между категориями")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/EQH0pyhM/43-%D1%82%D0%BA-003-%D0%BA%D0%BE%D0%BC%D0%B1%D0%B8%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%B0%D1%8F-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B9-%D0%B8-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%BE%D0%B2",
                 "ТК-003"
)
def test_category_switching_chaotic(web_browser):
    with allure.step('Запускаем и настраиваем браузер'):
        driver = MainPage(web_browser)
        time.sleep(1)


    categories = {
        "Phones": (driver.cat_phones, phones),
        "Laptops": (driver.cat_laptops, laptops),
        "Monitors": (driver.cat_monitors, monitors),
    }


    category_names = list(categories.keys())
    random.shuffle(category_names)

    for cat_name in category_names:
        cat_element, expected_products = categories[cat_name]

        with allure.step(f'Нажимаем на категорию {cat_name}'):
            cat_element.click()
            time.sleep(1)

        with allure.step(f'Проверяем товары в категории {cat_name}'):
            displayed_products = driver.get_all_products()


            for product in expected_products:
                with allure.step(f'Проверяем, что товар "{product}" отображается'):
                    check.is_true(product in displayed_products,
                                  f"Товар {product} не отображается в категории {cat_name}")


            with allure.step(f'Проверяем количество товаров в категории {cat_name}'):
                check.equal(len(displayed_products), len(expected_products),
                            f"Количество товаров в категории {cat_name} не соответствует ожидаемому")

@allure.feature("Главная страница")
@allure.story("Проверка кнопок навигации категорий")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/lgellgTt/44-%D1%82%D0%BA-004-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D0%BA%D0%BD%D0%BE%D0%BF%D0%BE%D0%BA-%D0%BD%D0%B0%D0%B2%D0%B8%D0%B3%D0%B0%D1%86%D0%B8%D0%B8-%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B9",
                 "ТК-004"
)
def test_category_navigation_buttons_absence(web_browser):
    with allure.step('Запускаем браузер и открываем главную страницу'):
        driver = MainPage(web_browser)
        time.sleep(1)

    categories = [
        (driver.cat_phones, "Phones"),
        (driver.cat_laptops, "Laptops"),
        (driver.cat_monitors, "Monitors"),
    ]

    for cat_element, cat_name in categories:
        with allure.step(f'Переходим в категорию {cat_name}'):
            cat_element.click()
            time.sleep(1)


        with allure.step('Скролим страницу до блока товаров'):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

        with allure.step(f'Проверяем, что кнопка "Next" отсутствует на странице {cat_name}'):
            check.is_false(driver.btn_next.is_visible(),
                           f"Кнопка 'Next' отображается в категории {cat_name}")

        with allure.step(f'Проверяем, что кнопка "Previous" отсутствует на странице {cat_name}'):
            check.is_false(driver.btn_previous.is_visible(),
                           f"Кнопка 'Previous' отображается в категории {cat_name}")



@allure.feature("Главная страница")
@allure.story("Функциональность кнопок Next и Previous")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/tx7Rgwaj/40-%D1%82%D0%BA-004-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D0%BA%D0%BD%D0%BE%D0%BF%D0%BE%D0%BA-%D0%BD%D0%B0%D0%B2%D0%B8%D0%B3%D0%B0%D1%86%D0%B8%D0%B8-%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B9",
                 "ТК-005"
)
def test_navigation_buttons_with_boundaries(web_browser):
    driver = MainPage(web_browser)
    time.sleep(1)


    with allure.step("Собираем товары на первой странице"):
        first_page_products = driver.get_all_products()


    with allure.step("Переходим на следующую страницу с помощью Next"):
        driver.btn_next.click()
        time.sleep(1)
        next_page_products = driver.get_all_products()
        check.is_false(first_page_products == next_page_products,
                       "Товары не изменились после клика Next")


    with allure.step("Возвращаемся на предыдущую страницу с помощью Previous"):
        driver.btn_previous.click()
        time.sleep(1)
        previous_page_products = driver.get_all_products()
        check.is_false(next_page_products == previous_page_products,
                       "Товары не изменились после клика Previous")
        check.is_true(previous_page_products == first_page_products,
                      "После возврата товары не совпадают с первой страницей")


