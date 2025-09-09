from nuts_nuts_nuts.page1.base_page import WebPage
from nuts_nuts_nuts.page1.elements import WebElement
import allure
from nuts_nuts_nuts.Locators.main_locators import MainPage
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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


def test_footer_links(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step("Скроллим страницу вниз"):
        driver._web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    with allure.step('Подготовка тестовых данных'):
        footer_links = [
            (driver.servise_button, "https://emall.by/information/company/about-service"),
            (driver.contacty_button, "https://emall.by/information/company/contacts"),
            (driver.news_button, "https://emall.by/news"),
            # (driver.vacansii_button, "https://jobs.e-dostavka.by/"),
            (driver.dostavca_dlya_urlic_button, "https://emall.by/information/delivery/legal"),
            (driver.postavsikam_button, "https://emall.by/information/suppliers"),
            (driver.reklamodatelam_button, "https://emall.by/information/advertisers"),
            (driver.stat_prodavcom_button, "https://emall.by/information/become-seller"),
            (driver.prodaza_avto_button, "https://emall.by/information/cars"),
            (driver.polz_soglashenie_button, "https://emall.by/information/terms"),
            (driver.vopros_otvet_button, "https://emall.by/information/faq"),
            (driver.dostavka_oplata_button, "https://emall.by/information/delivery"),
            # (driver.katalog_button, "https://emall.by/catalog"),
            (driver.tovari_ot_emall_button, "https://emall.by/information/emall-goods"),
            (driver.punkti_vidachi_button, "https://emall.by/information/pickup-points"),
            # (driver.soglashenie_o_creditax_button, "https://emall.by/information/credit"),
            # (driver.edostavca_button, "https://emall.by/information/edostavka"),
            # (driver.evropochta_button, "https://emall.by/information/evropochta"),
            # (driver.evroopt_button, "https://emall.by/information/evroopt"),
            # (driver.xit_button, "https://emall.by/information/hit"),
            # (driver.groshik_button, "https://emall.by/information/groshik"),
            # (driver.my_socsetyax_button, "https://emall.by/information/social"),
            # (driver.sviazatsa_snamy_button, "https://emall.by/information/contacts-form"),
        ]

        for button, expected_url in footer_links:
            with allure.step(f"Кликаем по кнопке и проверяем страницу"):
                button.click()
                WebDriverWait(driver._web_driver,15).until(EC.url_contains(expected_url))
                current_url = driver._web_driver.current_url

                assert current_url == expected_url, f"Ожидали {expected_url}, а получили {current_url}"
                # driver.open("https://emall.by")