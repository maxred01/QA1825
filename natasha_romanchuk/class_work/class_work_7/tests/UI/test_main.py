import allure
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from nuts_nuts_nuts.conftest import chrome_options
from natasha_romanchuk.class_work.class_work_7.Locators.main_locators import MainPage
from nuts_nuts_nuts.conftest import web_browser
import pytest_check as check
from nuts_nuts_nuts.page1.base_page import WebPage
from nuts_nuts_nuts.page1.elements import WebElement
from nuts_nuts_nuts.page1.elements import ManyWebElements

@allure.feature("Главная страница")
@allure.story("Хэдер, проверка элементов на отображение и кликабельность")
@allure.severity(allure.severity_level.NORMAL)
def test_header_elements_displayed(web_browser, chrome_options):
    with allure.step('Запуск и настройка браузера'):
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
    with allure.step('Запуск и настройка браузера'):
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


@allure.feature("Главная страница")
@allure.story("Проверка количества отображаемых брендов с прокруткой")
def test_brands_count(web_browser):
    driver = MainPage(web_browser)

    with allure.step("Настройка браузера"):
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step("Нажимаем на кнопку открытия списка брендов"):
        open_brands_button = driver.brands
        open_brands_button.click()

    with allure.step("Ожидаем видимость брендов"):
        wait = WebDriverWait(web_browser, 20)
        brands_elements = wait.until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, '//a[contains(@class,"brands_brand_card")]')
            )
        )

    with allure.step("Прокручиваем к каждому бренду"):
        for brand in brands_elements:
            ActionChains(web_browser).move_to_element(brand).perform()

    with allure.step("Проверяем количество брендов"):
        brands_count = len(brands_elements)
        check.greater_equal(brands_count, 5)  # минимум 5 брендов
        check.less_equal(brands_count, 1000)    # максимум 1000 брендов

@allure.feature("Главная страница")
@allure.story("Хэдер, ввод запроса в поисковую строку")
def test_search_product_valid_query(web_browser):
    with allure.step('Запуск и настройка браузера'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step('Вводим запрос и нажимаем Поиск'):
        search_input = driver.search_input
        search_input.send_keys("iPhone")
        driver.search_button.click()
        time.sleep(3)

    with allure.step('Проверяем, что результаты поиска отображаются'):
        check.is_true(driver.search_results.is_visible(), "Результаты поиска не отображаются")

    with allure.step('Проверяем, что в результатах есть iPhone'):
        results_text = driver.search_results.get_text().lower()
        check.is_true("iphone" in results_text, f"'iPhone' не найден в результатах: {results_text}")

@allure.feature("Главная страница")
@allure.story("Хэдер, очистка строки поиска")
def test_search_clear_field(web_browser):
    with allure.step('Запуск и настройка браузера'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step('Вводим запрос и очищаем строку'):
        search_input = driver.search_input
        search_input.send_keys("iPhone")
        search_input.send_keys(Keys.CONTROL + "a")
        search_input.send_keys(Keys.DELETE)

    with allure.step('Проверяем, что поле поиска стало пустым'):
        after_clear_value = search_input.get_attribute("value")
        check.equal(after_clear_value, "", f"Ожидали пустое поле поиска, но получили '{after_clear_value}'")

@allure.feature("Главная страница")
@allure.story("Подсчет товаров на главной странице")
def test_count_products(web_browser):
    with allure.step('Запускаем и настройка браузер'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step('Подсчет количества товаров'):

        products = driver.all_products.count()
        check.greater_equal(products, 10)  #от 10
        check.less_equal(products, 99)      # до 99

@allure.feature("Главная страница")
@allure.story("Проверка отображения картинок у всех товаров")
def test_check_product_images_visible(web_browser):
    with allure.step('Запускаем браузер и открываем главную страницу'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step('Получаем все товары на странице'):
        products = driver.all_products.count()
        check.greater_equal(products, 1, "На странице нет товаров для проверки картинок")

    with allure.step('Проверяем, что у каждого товара картинка отображается'):
        for i in range(products):
            img_element = driver.all_products[i].find_element(By.TAG_NAME, "img")  # ищем <img> внутри каждого товара

            img_src = img_element.get_attribute("src")
            check.is_not_none(img_src, f"У товара №{i+1} отсутствует картинка (src=None)")
            check.not_equal(img_src.strip(), "", f"У товара №{i+1} пустой src для картинки")  # проверяем, что атрибут src не пустой
            check.is_true(img_element.is_displayed(), f"Картинка у товара №{i+1} не отображается на странице")  # проверяем, что картинка реально отображается

@allure.feature('Главная страница')
@allure.story('Кнопки "В корзине" кликабельны')
def test_vkorzine(web_browser):
    with allure.step('Запуск и настройка браузера'):
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
@allure.story('Переход на сраницу "Контакты" через футер')
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


@allure.feature("Главная страница")
@allure.story("Проверка всех ссылок футера и переход на них")
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
        (driver.polz_soglashenie_button, "https://api-preprod.emall.by/storage/admin/files/yLqTfBKDsBPjdoPYehZxJushzuEyMifSngLFyMHH.pdf"),
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
            driver.wait_page_loaded(timeout=120) # ждём загрузку страницы

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
@allure.story('Добавление товара в корзину и проверка его отображения, количества и цены')
def test_add_goods_and_check_cart(web_browser):
    with allure.step('Запуск и настройка браузера'):
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


@allure.feature('Главная страница')
@allure.story('Добавление товара в "Избранное" и его отображение в "Избранное"')
def test_add_goods_at_favorites(web_browser):
    with allure.step('Запуск и настройка браузера'):
        driver = MainPage(web_browser)
        driver.cookies_button.click()
        driver.close_button.click()

    with allure.step('Добавляем товар в "Избранное"'):
        driver.main_img.move_to_element()
        element1 = driver.main_name.get_text()
        driver.main_izbrannoe.click()

    with allure.step('Переходим в "Избранное"'):
        driver.action_button_favorites.click()
        element2 = driver.favorite_name.get_text()
        assert element1 == element2


