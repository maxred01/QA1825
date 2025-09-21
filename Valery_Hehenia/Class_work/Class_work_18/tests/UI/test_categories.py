import time
import allure
import random

from Valery_Hehenia.Class_work.Class_work_18.locators.locators_main_page import MainPage
from Valery_Hehenia.Class_work.Class_work_18.data.products import phones, laptops, monitors

from das_magaz.conftest import webdriver
from das_magaz.conftest import chrome_options, web_browser
import pytest_check as check






@allure.feature("Главная страница")
@allure.story("Товары по категориям")
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


        with allure.step('Скроллим страницу до блока товаров'):
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


