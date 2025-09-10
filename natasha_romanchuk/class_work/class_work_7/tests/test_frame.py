import allure
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from nuts_nuts_nuts.conftest import chrome_options
from natasha_romanchuk.class_work.class_work_7.Locators.main_locators import MainPage
from nuts_nuts_nuts.conftest import web_browser
import pytest_check as check
from nuts_nuts_nuts.page1.base_page import WebPage
from nuts_nuts_nuts.page1.elements import WebElement


# def test_footer_links(web_browser):
#     with allure.step('Запускаем и настройка браузер'):
#         driver = MainPage(web_browser)
#         driver.cookies_button.click()
#         driver.close_button.click()
#         original_window = web_browser.current_window_handle
#
#     with allure.step('Подготовка тестовых данных'):
#         footer_links = [
#             (driver.servise_button, "https://emall.by/information/company/about-service"),
#             (driver.contacty_button, "https://emall.by/information/company/contacts"),
#             (driver.news_button, "https://emall.by/news"),
#             (driver.postavsikam_button, "https://emall.by/information/company/conditions-for-selecting-a-counterparty"),
#             (driver.reklamodatelam_button, "https://emall.by/information/company/advertisement"),
#             (driver.vopros_otvet_button, "https://emall.by/information/help"),
#             (driver.dostavka_oplata_button, "https://emall.by/information/help/132"),
#             (driver.tovari_ot_emall_button, "https://emall.by/shop/1"),
#             (driver.punkti_vidachi_button, "https://emall.by/map"),
#             (driver.vacansii_button,"https://jobs.e-dostavka.by/"),
#             (driver.dostavca_dlya_urlic_button,"https://business.emall.by/catalog/"),
#             (driver.stat_prodavcom_button,"https://seller.emall.by/"),
#             (driver.prodaza_avto_button,"https://emall.by/news/82"),
#             (driver.polz_soglashenie_button,"https://api-preprod.emall.by/649008c9c6277_publichnyj-dogovor-emall.pdf"),
#             (driver.soglashenie_o_creditax_button,"https://api-preprod.emall.by/storage/admin/files/UOEpXjJF8xBxksqpphDwn5HKKr6SizVhijbqxEww.pdf"),
#             (driver.edostavca_button,"https://edostavka.by/#modal-opened"),
#             (driver.evropochta_button,"https://evropochta.by/"),
#             (driver.evroopt_button,"https://evroopt.by/"),
#             (driver.xit_button,"https://hitdiscount.by/"),
#             (driver.groshik_button,"https://groshyk.by/"),
#             (driver.sviazatsa_snamy_button,"https://emall.by/information/company/advertisement?modal_id=feedback_modal&feedback_modal.props=%7B%7D")
#
#         ]
#
#         for button, expected_url in footer_links:
#             with allure.step(f"Проверяем ссылку: {expected_url}"):
#                 button.click()
#
#                 # ждём новую вкладку или переход
#                 WebDriverWait(web_browser, 5).until(lambda d: len(d.window_handles) >= 1)
#                 all_windows = web_browser.window_handles
#
#                 if len(all_windows) > 1:  # открылась новая вкладка
#                     new_window = [w for w in all_windows if w != original_window][0]
#                     web_browser.switch_to.window(new_window)
#
#                 current_url = web_browser.current_url
#                 assert expected_url in current_url, f"Ожидали {expected_url}, но получили {current_url}"
#
#                 # закрываем вкладку, если она новая
#                 if len(all_windows) > 1:
#                     web_browser.close()
#                     web_browser.switch_to.window(original_window)
#                 else:
#                     web_browser.back()




def test_footer_links(web_browser):
    with allure.step("Запуск браузера и закрытие баннеров"):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    # список кнопок и ожидаемых ссылок
    footer_links = [
        (driver.servise_button, "https://emall.by/information/company/about-service"),
        (driver.contacty_button, "https://emall.by/information/company/contacts"),
        (driver.news_button, "https://emall.by/news"),
        (driver.postavsikam_button, "https://emall.by/information/company/conditions-for-selecting-a-counterparty"),
        (driver.reklamodatelam_button, "https://emall.by/information/company/advertisement"),
        (driver.vopros_otvet_button, "https://emall.by/information/help"),
        (driver.dostavka_oplata_button, "https://emall.by/information/help/132"),
        (driver.tovari_ot_emall_button, "https://emall.by/shop/1"),
        (driver.punkti_vidachi_button, "https://emall.by/map"),
        (driver.vacansii_button, "https://jobs.e-dostavka.by/"),
        (driver.dostavca_dlya_urlic_button, "https://business.emall.by/catalog/"),
        (driver.stat_prodavcom_button, "https://seller.emall.by/"),
        (driver.prodaza_avto_button, "https://emall.by/news/82"),
        (driver.polz_soglashenie_button, "https://api-preprod.emall.by/649008c9c6277_publichnyj-dogovor-emall.pdf"),
        (driver.soglashenie_o_creditax_button, "https://api-preprod.emall.by/storage/admin/files/UOEpXjJF8xBxksqpphDwn5HKKr6SizVhijbqxEww.pdf"),
        (driver.edostavca_button, "https://edostavka.by/#modal-opened"),
        (driver.evropochta_button, "https://evropochta.by/"),
        (driver.evroopt_button, "https://evroopt.by/"),
        (driver.xit_button, "https://hitdiscount.by/"),
        (driver.groshik_button, "https://groshyk.by/"),
        (driver.sviazatsa_snamy_button, "https://emall.by/?modal_id=feedback_modal&feedback_modal.props=%7B%7D"),
    ]

    for button, expected_url in footer_links:
        with allure.step(f"Проверяем кнопку → {expected_url}"):
            original_window = driver._web_driver.current_window_handle
            windows_before = driver._web_driver.window_handles

            # кликаем по кнопке
            button.click()

            # ждём загрузку страницы
            driver.wait_page_loaded()

            # проверяем, открылась ли новая вкладка
            windows_after = driver._web_driver.window_handles
            if len(windows_after) > len(windows_before):
                # переключаемся на новую вкладку
                new_window = [w for w in windows_after if w not in windows_before][0]
                driver._web_driver.switch_to.window(new_window)

            # берём текущий URL
            current_url = driver.get_current_url()
            assert current_url == expected_url, f"Ожидали {expected_url}, а получили {current_url}"

            # если новая вкладка — закрываем её и возвращаемся обратно
            if len(windows_after) > len(windows_before):
                driver._web_driver.close()
                driver._web_driver.switch_to.window(original_window)
            else:
                driver.go_back()













# def test_kontakty(web_browser):
#     with allure.step('Запускаем и настройка браузер'):
#         driver = MainPage(web_browser)
#         driver.cookies_button.click()
#         driver.close_button.click()
#
#     with allure.step("Скроллим страницу вниз"):
#         driver._web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#     with allure.step('Нажимаем на кнопку "Контакты" в футере'):
#         driver.contacty_button.click()
#     with allure.step("Проверяем, что открылась страница Контакты"):
#         current_url = "https://emall.by/information/company/contacts"
#         print("Текущий URL:", current_url)
#         assert current_url == "https://emall.by/information/company/contacts", \
#             f"Ожидали страницу Контакты, а открылась {current_url}"

@allure.feature('Главная страница')
@allure.story('Добавление товара в корзину и проверка корзины')
def test_add_goods_and_check_cart(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step('Добавляем товар в корзину'):
        driver.v_korzine_dtn_1.click()

    with allure.step('Переходим в корзину'):
        driver.action_button_basket.click()

    with allure.step('Проверяем, что товар отображается в корзине'):
        product_name = driver.korzina_product_name.get_text()
        assert product_name != "", f"Товар не появился в корзине"

    with allure.step('Проверяем количество товара'):

        counter = driver.product_counter.get_attribute('value')   # если input
        bage = driver.bage_korzina_count.get_text()               # если текст внутри элемента

        assert counter == bage, f'Ожидали количество{counter}, а получили количество {bage}'

    with allure.step('Проверяем цену товара'):
        price = driver.korzina_product_price.get_text()
        assert price != "", "Цена товара не отображается"