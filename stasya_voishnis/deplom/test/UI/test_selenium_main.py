import time
import allure

from stasya_voishnis.deplom.locator.main_locators import MainPage
import pytest_check as check

@allure.feature("Главная страница")
@allure.story("Хедер")
def test_headers(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.btn_cookies.click()
        driver.btn_onboarding.click()

    with allure.step('Подготовка тестовых данных'):
        elements = [
            (driver.their_majesties_header_btn, 'Their Majesties'),
            (driver.royal_websites_header_btn, 'Royal websites"'),
            (driver.search_header_btn, 'Search'),
            (driver.logo_header_btn, 'Logo'),
            (driver.the_king_header_btn, 'The King'),
            (driver.the_queen_header_btn, 'The Queen'),
            (driver.the_coronation_header_btn, 'The Coronation'),
            (driver.the_royal_family_header_btn, 'The Royal Family'),
            (driver.queen_elizabeth_2_header_btn, 'Queen Elizabeth II'),
            (driver.royal_residences_header_btn, 'Royal Residences, Art and History'),
            (driver.news_header_btn, 'News'),
        ]

    with allure.step('Проверка элемента'):
        for element, text_element in elements:
            with allure.step(f'Проверка элемента {text_element} на отображение'):
                check.is_true(element.is_visible(), f'Элемента {text_element} нет визуально на экарне')

            with allure.step(f'Проверка элемента {text_element} на кликабельность'):
                check.is_true(element.is_clickable(), f'Элемента {text_element} не кликабелен')


@allure.feature("Главная страница")
@allure.story("Футер")
def test_footers(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.btn_cookies.click()
        driver.btn_onboarding.click()

    with allure.step('Подготовка тестовых данных'):
        elements = [
            (driver.the_king_footer_btn,'The King'),
            (driver.the_queen_footer_btn,'The Queen'),
            (driver.the_coronation_footer_btn,'The Coronation'),
            (driver.the_royal_family_footer_btn,'The Royal Family'),
            (driver.queen_elizabeth_2_footer_btn,'Queen Elizabeth II'),
            (driver.royal_residences_footer_btn,'Royal Residences, Art and History'),
            (driver.news_footer_btn,'News'),
            (driver.about_this_site_footer_btn,'About this site'),
            (driver.contact_us_footer_btn,'Contact us'),
            (driver.media_centre_footer_btn,'Media centre'),
            (driver.privacy_footer_btn,'Privacy'),
            (driver.report_a_vulnerability_footer_btn,'Report a Vulnerability'),
            (driver.social_media_footer_btn,'Social Media Community Guidelines'),
            (driver.working_for_us_footer_btn,'Working for us'),
            (driver.logo_footer_footer_btn,'Logo'),
            (driver.the_royal_household_footer_btn,'The Royal Household © Crown Copyright'),
                    ]

    with (allure.step('Проверка элемента')):
        for element, text_element in elements:
            with allure.step(f'Проверка элемента {text_element} на отображение'):
                check.is_true(element.is_visible(), f'Элемента {text_element} нет визуально на экарне')

            with allure.step(f'Проверка элемента {text_element} на кликабельность'):
                check.is_true(element.is_clickable(), f'Элемента {text_element} не кликабелен')


@allure.feature("Главная страница")
@allure.story("Проверка наличия новостных блоков")
def test_news_main(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.btn_cookies.click()


    with allure.step('Подсчет количества элементов'):
        check.equal(driver.news_blok, 21,'Не найдено нужное количество элементов')
        # check.less_equal(news_blok_element, 21)





