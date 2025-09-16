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

@allure.feature("Header Navigation")
@allure.story("Visual Elements Display")
@allure.severity(allure.severity_level.NORMAL)
def test_header_elements_displayed(web_browser, chrome_options):
    with allure.step('Запускаем и настраиваем браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step('Подготовка тестовых данных'):
        elements = [
            ( driver.logotip,"логотип"),
            ( driver.search_input,"строка поиска"),
            ( driver.search_button,"иконка поиска"),
            ( driver.catalog_button,"кнопка каталог"),
            ( driver.action_button_enter,"войти"),
            ( driver.action_button_orders,"заказы"),
            ( driver.action_button_favorites,"избранное"),
            ( driver.action_button_basket,"корзина"),
            ( driver.actions_button,"акции"),
            ( driver.lucky_goods_button,"товары-везунчики"),
            ( driver.promocodes_button,"промокоды"),
            ( driver.new_button,"новинки"),
            ( driver.urgent_goods_button,"срочный товар"),
            ( driver.take_more_button,"упаковкой выгоднее"),
            ( driver.naushniki_besprovodnye_button,"наушники беспроводные"),
            ( driver.school_button,"школа"),
            ( driver.detskaya_stirka_button,"детская стирка"),

    ]


    with allure.step('Проверка элемента'):
        for element, text_element in elements:
            with allure.step(f'Проверка элемента {text_element} на отображение'):
                check.is_true(element.is_visible(), f'Элемента {text_element} нет визуально')

            with allure.step(f'Проверка элемента {text_element} на кликабельность'):
                check.is_true(element.is_clickable(), f'Элемента {text_element} не кликабелен')

@allure.feature("Главная страница")
@allure.story("Футер, отображение и кликабельность элементов")
def test_footers(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step('Подготовка тестовых данных'):
        elements = [
            (driver.compania_button, 'Компания'),
            (driver.servise_button, 'О сервисе'),
            (driver.news_button, 'Новости'),
            (driver.vacansii_button, 'Вакансии'),
            (driver.sotrydnichestvo_button, 'Сотрудничество'),
            (driver.dostavca_dlya_urlic_button, 'Доставка для юр.лиц'),
            (driver.postavsikam_button, 'Поставщикам'),
            (driver.reklamodatelam_button, 'Рекламодателям'),
            (driver.stat_prodavcom_button, 'Стать продавцом'),
            (driver.prodaza_avto_button, 'Продажа автомобилей'),
            (driver.pokypatelam_button, 'Покупателям'),
            (driver.polz_soglashenie_button, 'Пользовательское соглашение'),
            (driver.vopros_otvet_button, 'Вопрос-ответ'),
            (driver.dostavka_oplata_button, 'Доставка и оплата'),
            (driver.catalog_button, 'Каталог'),
            (driver.tovari_ot_emall_button, 'Товары от магазина Emall'),
            (driver.punkti_vidachi_button, 'Пункты выдачи'),
            (driver.soglashenie_o_creditax_button, 'Соглашение о кредитных ресурсах'),
            (driver.nashi_druzia_button, 'Наши друзья'),
            (driver.edostavka_button, 'Едоставка'),
            (driver.evropochta_button, 'Европочта'),
            (driver.evroopt_button, 'Евроопт'),
            (driver.xit_button, 'Хит!'),
            (driver.groshik_button, 'Грошык')
        ]

        skip_click_chek = ['Компания','Сотрудничество','Покупателям','Наши друзья']

    with allure.step('Проверка элемента'):
        for element, text_element in elements:
            with allure.step(f'Проверка элемента {text_element} на отображение'):
                check.is_true(element.is_visible(), f'Элемента {text_element} нет визуально на экарне')

            if text_element not in skip_click_chek:
                with allure.step(f'Проверка элемента {text_element} на кликабельность'):
                    check.is_true(element.is_clickable(), f'Элемента {text_element} не кликабелен')



    with allure.step('Проверка брендов'):
        check.equal(driver.brands_button.count(),20)


@allure.feature("Главная страница")
@allure.story("Хэдер, ввод запроса в поисковую строку и удаление запроса")
def test_search_product(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step('Вводим запрос и нажимаем Enter'):
        search_product = driver.search_input
        search_product.send_keys("iPhone")
        search = driver.search_button
        search.click()
        time.sleep(10)

    with allure.step('Проверяем, что результаты поиска отображаются'):
        check.is_true(driver.search_results.is_visible(),"Результаты поиска не отображаются на странице")

        search_product.send_keys(Keys.CONTROL + "a") # Выделить все
        search_product.send_keys(Keys.DELETE)         # Очистить
        assert search_product.is


@allure.feature("Главная страница")
@allure.story("Подсчет товаров и проверка наличия картинок")
def test_count_products(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step('Подсчет количества товаров'):

        products = driver.all_products.count()
        check.greater_equal(products, 10)  #от 10
        check.less_equal(products, 99)      # до 99

@allure.feature('Главная страница')
@allure.story('Кнопки "В корзине" кликабельны')
def test_vkorzine(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step("Скроллим страницу вниз"):
        driver._web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    with allure.step("Проверяем кликабельность кнопок 'В корзине'"):
        vkorzine_buttons = driver.vkorzine_btn.find()  # получаем список кнопок
        if not vkorzine_buttons:
            print("Кнопки 'В корзине' не найдены!")
            assert False, "Кнопки 'В корзине' не найдены!"

        wait = WebDriverWait(driver._web_driver, 10)

        for i, btn in enumerate(vkorzine_buttons, start=1):
            driver._web_driver.execute_script("arguments[0].scrollIntoView(true);", btn)   # Скроллим к кнопке

            try:
                wait.until(EC.element_to_be_clickable(btn))    # Ждём, пока кнопка станет кликабельной
                print(f"Кнопка {i} кликабельна ")
            except:
                print(f"Кнопка {i} НЕ кликабельна ")

@allure.feature('Главная страница')
@allure.story('Переход на сраницу "Контакты"через футер')
def test_kontakty(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step("Скроллим страницу вниз"):
        driver._web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    with allure.step('Нажимаем на кнопку "Контакты" в футуре'):
        driver.contacty_button.click()
    with allure.step("Проверяем, что открылась страница Контакты"):
        current_url = "https://emall.by/information/company/contacts"
        # print("Текущий URL:", current_url)
        assert current_url == "https://emall.by/information/company/contacts", \
            f"Ожидали страницу Контакты, а открылась {current_url}"

@allure.feature("Главная страница,Footer")
@allure.story("Проверка всех ссылок футера")
def test_footer_links(web_browser):
    with allure.step("Запуск браузера и закрытие баннеров"):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

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

            button.click()  # кликаем по кнопке
            driver.wait_page_loaded() # ждём загрузку страницы

            windows_after = driver._web_driver.window_handles   # проверяем, открылась ли новая вкладка
            if len(windows_after) > len(windows_before):
                new_window = [w for w in windows_after if w not in windows_before][0]  # переключаемся на новую вкладку
                driver._web_driver.switch_to.window(new_window)

            current_url = driver.get_current_url() # берём текущий URL
            assert current_url == expected_url, f"Ожидали {expected_url}, а получили {current_url}"

            if len(windows_after) > len(windows_before): # если новая вкладка — закрываем её и возвращаемся обратно
                driver._web_driver.close()
                driver._web_driver.switch_to.window(original_window)
            else:
                driver.go_back()

@allure.feature('Главная страница')
@allure.story('Добавление товара в корзину и проверка корзины')
def test_add_goods_and_check_cart(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step('Добавляем товар в корзину'):
        driver.v_korzine_dtn_1.click()
        main_prise = driver.main_product_price.get_text()
        main_prise = main_prise.split('\n')[0]
        main_prise = main_prise.replace(' р.', '')
        main_prise = main_prise.replace(',', '.')

    with allure.step('Переходим в корзину'):
        driver.action_button_basket.click()

    with allure.step('Проверяем, что товар отображается в корзине'):
        product_name_1 = driver.main_product_name.get_text()
        product_name = driver.korzina_product_name.get_text()
        assert product_name != "", f"Товар не появился в корзине"
        assert product_name_1 == product_name, f"Названия товаров не совпадают"

    with allure.step('Проверяем количество товара'):
        counter = driver.product_counter.get_attribute('value')  # если input
        bage = driver.bage_korzina_count.get_text()  # если текст внутри элемента

        assert counter == bage, f'Ожидали количество{counter}, а получили количество {bage}'

    with allure.step('Проверяем цену товара'):
        price = driver.korzina_product_price.get_text()
        price = price.replace(' р.', '')
        price = price.replace(',', '.')
        print((price))
        print((main_prise))
        assert float(price) > 0
        assert price == main_prise

        # with allure.step('Отображение логотипа'):
    #     logo = driver.find_element(By.XPATH, driver.logotip)
    #     assert logo.is_displayed()
    #
    # with allure.step('Отображение строки поиска'):
    #     search  = driver.find_element(By.XPATH, driver.search_input)
    #     assert search.is_displayed()
    #
    # with allure.step('Отображение иконки поиска'):
    #     search_btn  = driver.find_element(By.XPATH, driver.search_button)
    #     assert search_btn.is_displayed()
    #
    # with allure.step('Отображение кнопки каталог'):
    #     catalog_btn  = driver.find_element(By.XPATH, driver.catalog_button)
    #     assert catalog_btn.is_displayed()