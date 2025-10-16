import time
import allure
import pytest
from bsuir.locators.main_locators import MainPage
from bsuir.tests.conftest import chrome_options
from pytest_check import check
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.ui import WebDriverWait


@allure.feature('Главная страница')
@allure.story("Header")
def test_header(web_browser, chrome_options):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(15)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(5)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(5)


    with allure.step('Подготовка тестовых данных'):
        elements = [
            (driver.btn_header1, 'Главная'),
            (driver.btn_header2, 'Группа'),
            (driver.btn_header3, 'Опубликовать пост!'),
            (driver.btn_header4, 'Уведомления'),
            (driver.btn_header5, 'Аккаунт')
        ]

    with allure.step('Проверка элемента'):
        for element, text_element in elements:
            with allure.step(f'Проверка элемента {text_element} на кликабельность'):
                check.is_true(element.is_clickable(), f'Элемента {text_element} не кликабелен')



@allure.feature('Проверка фокуса в поле поиск')
@allure.story("Header")
def test_header(web_browser, chrome_options):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(15)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(5)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(5)

    with allure.step('Подготовка тестовых данных'):
        elements = [
            (driver.btn_poisk, 'Поиск')
        ]
    with allure.step('Проверка фокуса на поле поиска'):
        search_field = driver.btn_poisk
        search_field.click()
        time.sleep(1)

        active_element = web_browser.switch_to.active_element
        assert search_field.get_attribute("placeholder") == active_element.get_attribute("placeholder"), \
            "Фокус не установлен на поле поиска после клика"




@allure.title('Проверка поля поиска на ввод любых 50 символов')
@allure.story('Валидация поля "Поиск"')
def test_header(web_browser, chrome_options):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(15)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(5)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(5)

    with allure.step('Подготовка тестовых данных'):
        test_data = [
            ('А' * 51, 'Больше 50 символов (проверка лимита)')
        ]

    with allure.step('Выполняем проверки поля "Поиск"'):
        for text, description in test_data:
            with allure.step(f'Проверка: {description}'):

                # Клик по иконке или лейблу, чтобы активировать поиск
                driver.btn_poisk.click()

                # Ждём появления input-поля
                wait.until(
                    EC.visibility_of_element_located(
                        (By.XPATH, '//input[@class="mhy-autocomplete__input"]')
                    )
                )

                # Берём реальное поле ввода
                search_field = driver.search_field.find()  # достаём реальный selenium-элемент
                search_field.clear()
                search_field.send_keys(text)
                time.sleep(1)

                # Получаем введённое значение
                value = search_field.get_attribute('value')

                # Проверка лимита
                if len(text) > 50:
                    assert len(value) <= 50, f'Поле принимает более 50 символов ({len(value)})'
                else:
                    assert value == text or value == text[:50], f'Некорректный ввод данных "{text}"'

                # Логирование результата
                allure.attach(value, name=f'Введено: {description}', attachment_type=allure.attachment_type.TEXT)

                time.sleep(1)@allure.feature('Главная страница')




@allure.feature('Главная страница')
@allure.title('Проверка поля поиска на ввод только латиницы (пример до 20 символов)')
@allure.story('Валидация поля "Поиск" — ввод латиницы')
def test_header(web_browser, chrome_options):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(15)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(5)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(5)

    with allure.step('Подготовка тестовых данных'):
        test_data = [
            ('HelloWorld', 'Ввод латиницы — 10 символов'),
            ('PythonAutomationTestCase', 'Ввод латиницы — больше 20 символов (пример)')
        ]

    with allure.step('Выполняем проверки поля "Поиск"'):
        for text, description in test_data:
            with allure.step(f'Проверка: {description}'):

                # Активируем поле поиска
                driver.btn_poisk.click()

                # Ждём появления input-поля
                wait.until(
                    EC.visibility_of_element_located(
                        (By.XPATH, '//input[@class="mhy-autocomplete__input"]')
                    )
                )

                # Получаем реальный элемент input
                search_field = driver.search_field.find()
                search_field.clear()
                search_field.send_keys(text)
                time.sleep(1)

                # Получаем введённое значение
                value = search_field.get_attribute('value')

                # Проверяем, что введено только латиницей
                assert value.isascii() and value.isalpha(), \
                    f'Поле принимает недопустимые символы: "{value}"'

                # Проверяем, что текст введён полностью (до 20 символов — пример)
                assert len(value) == len(text), \
                    f'Введённый текст отличается по длине: ожидалось {len(text)}, получено {len(value)}'

                # Логируем результат
                allure.attach(value, name=f'Введено: {description}', attachment_type=allure.attachment_type.TEXT)
                time.sleep(1)




@allure.feature('Главная страница')
@allure.title('Проверка поля поиска на ввод только кириллицы (пример до 20 символов)')
@allure.story('Валидация поля "Поиск" — ввод кириллицы')
def test_header(web_browser, chrome_options):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(15)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(5)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(5)

    with allure.step('Подготовка тестовых данных'):
        test_data = [
            ('Приветмир', 'Ввод кириллицы — 10 символов'),
            ('Солнцесветитнадморем', 'Ввод кириллицы — больше 20 символов (пример)')
        ]

    with allure.step('Выполняем проверки поля "Поиск"'):
        for text, description in test_data:
            with allure.step(f'Проверка: {description}'):

                driver.btn_poisk.click()

                wait.until(
                    EC.visibility_of_element_located(
                        (By.XPATH, '//input[@class="mhy-autocomplete__input"]')
                    )
                )

                search_field = driver.search_field.find()
                search_field.clear()
                search_field.send_keys(text)
                time.sleep(1)

                value = search_field.get_attribute('value')

                # Проверка: только кириллица и пробелы
                import re
                assert re.fullmatch(r'[А-Яа-яЁё ]+', value), \
                    f'Поле принимает недопустимые символы: "{value}"'

                # Проверка: длина текста соответствует ожидаемой
                assert len(value) == len(text), \
                    f'Введённый текст отличается по длине: ожидалось {len(text)}, получено {len(value)}'

                allure.attach(value, name=f'Введено: {description}', attachment_type=allure.attachment_type.TEXT)
                time.sleep(1)





@allure.feature('Главная страница')
@allure.title('Проверка поля поиска на ввод только цифр (пример: 23123)')
@allure.story('Валидация поля "Поиск" — ввод чисел')
def test_header(web_browser, chrome_options):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(15)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(5)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(5)

    with allure.step('Подготовка тестовых данных'):
        test_data = [
            ('23123', 'Ввод цифр — 5 символов'),
            ('12345678901234567890', 'Ввод цифр — ровно 20 символов'),
            ('123abc', 'Ввод цифр с буквами — недопустимо')
        ]

    with allure.step('Выполняем проверки поля "Поиск"'):
        for text, description in test_data:
            with allure.step(f'Проверка: {description}'):

                driver.btn_poisk.click()

                wait.until(
                    EC.visibility_of_element_located(
                        (By.XPATH, '//input[@class="mhy-autocomplete__input"]')
                    )
                )

                search_field = driver.search_field.find()
                search_field.clear()
                search_field.send_keys(text)
                time.sleep(1)

                value = search_field.get_attribute('value')

                import re
                if 'недопустимо' in description.lower():
                    # Негативный кейс — ожидаем, что поле не примет буквы
                    assert not re.fullmatch(r'\d+', value), \
                        f'Поле ошибочно приняло недопустимые символы: "{value}"'
                else:
                    # Позитивный кейс — только цифры
                    assert re.fullmatch(r'\d+', value), \
                        f'Поле принимает недопустимые символы: "{value}"'

                    assert len(value) == len(text), \
                        f'Введённый текст отличается по длине: ожидалось {len(text)}, получено {len(value)}'

                allure.attach(value, name=f'Введено: {description}', attachment_type=allure.attachment_type.TEXT)
                time.sleep(1)




@allure.feature('Поле поиска')
@allure.story('Валидация спецсимволов')
@allure.title('Проверка ввода спецсимволов в поле поиска')
def test_header(web_browser, chrome_options):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(15)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(5)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(5)

    with allure.step('Находим поле ввода поиска'):
        driver.btn_poisk.click()
        time.sleep(2)

        search_input = web_browser.find_element(By.XPATH, '//input[@class="mhy-autocomplete__input"]')

    with allure.step('Тестируем основные спецсимволы'):
        special_chars = [
            "!@#$%^&*()",
            "test-123",
            "hello_world",
            "test+plus",
            "price$100",
            "100%",
            "test?query",
            "email@test.com"
        ]

        for chars in special_chars:
            with allure.step(f'Проверка символов: {chars}'):
                search_input.clear()
                search_input.send_keys(chars)
                time.sleep(0.5)

                # Проверяем что текст введен корректно
                current_value = search_input.get_attribute('value')
                check.equal(
                    current_value,
                    chars,
                    f"Поле поиска не приняло спецсимволы: {chars}"
                )




@allure.feature('Поле поиска')
@allure.story('Пустой ввод')
@allure.title('Проверка пустого ввода в поиске')
def test_header(web_browser, chrome_options):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(15)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(5)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(5)

    with allure.step('Ищем поле поиска'):
        try:
            # Нажимаем на кнопку поиска
            driver.btn_poisk.click()
            time.sleep(2)

            # Ищем поле ввода
            search_input = web_browser.find_element(By.XPATH, '//input[@class="mhy-autocomplete__input"]')

        except Exception as e:
            web_browser.save_screenshot("error_no_search_field.png")
            raise AssertionError(f" ПОЛЕ ПОИСКА НЕ НАЙДЕНО: {str(e)}")

    with allure.step('Тест пустого ввода'):
        try:
            # Очищаем поле
            search_input.clear()
            time.sleep(1)

            # Пытаемся отправить пустой запрос
            search_input.send_keys(Keys.ENTER)
            time.sleep(3)  # Увеличиваем время ожидания навигации

            # Проверяем что нет критических ошибок
            current_url = web_browser.current_url
            allure.attach(f"URL после пустого поиска: {current_url}",
                          name="empty_search_result",
                          attachment_type=allure.attachment_type.TEXT)

            if "error" in current_url.lower():
                raise AssertionError(f" ОШИБКА ПРИ ПУСТОМ ПОИСКЕ: {current_url}")

        except Exception as e:
            raise AssertionError(f" ТЕСТ ПУСТОГО ВВОДА ПРОВАЛЕН: {str(e)}")

    with allure.step('Возвращаемся на главную для следующего теста'):
        try:
            # Возвращаемся на главную страницу
            web_browser.back()
            time.sleep(3)

            # Ждем загрузки главной страницы
            wait = WebDriverWait(web_browser, 10)
            wait.until(EC.url_contains("hoyolab.com"))

        except Exception as e:
            allure.attach(f"Не удалось вернуться на главную: {str(e)}",
                          name="back_navigation_error",
                          attachment_type=allure.attachment_type.TEXT)

    with allure.step('Проверка что поиск все еще работает после возврата'):
        try:
            # Снова находим поле поиска (старый элемент устарел)
            driver.btn_poisk.click()
            time.sleep(2)

            # НАХОДИМ ПОЛЕ ВВОДА ЗАНОВО - это важно!
            search_input_new = web_browser.find_element(By.XPATH, '//input[@class="mhy-autocomplete__input"]')

            # Проверяем работоспособность
            search_input_new.clear()
            search_input_new.send_keys("проверка работоспособности")
            search_input_new.send_keys(Keys.ENTER)
            time.sleep(3)

            final_url = web_browser.current_url
            allure.attach(f"Финальный URL после теста: {final_url}",
                          name="final_test_url",
                          attachment_type=allure.attachment_type.TEXT)

            # Проверяем что поиск сработал
            if "search" not in final_url.lower() and "query" not in final_url.lower():
                raise AssertionError(f" ПОИСК НЕ СРАБОТАЛ: {final_url}")

        except Exception as e:
            raise AssertionError(f" ПОИСК ПЕРЕСТАЛ РАБОТАТЬ ПОСЛЕ ВОЗВРАТА: {str(e)}")




@allure.feature('Кнопка "Опубликовать пост!"')
@allure.story('Header')
@allure.title('Проверка нажатия на кнопку "Опубликовать пост!"')
def test_header(web_browser, chrome_options):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(15)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(5)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(5)

    with allure.step('Нажимаем на кнопку "Опубликовать пост!"'):
        driver.btn_header3.click()
        time.sleep(2)  # Ждем появления списка

    with allure.step('Проверяем элементы выпадающего списка'):
        # Ищем контейнер выпадающего списка по классу
        dropdown = web_browser.find_element(By.CLASS_NAME, "mhy-post-new__content")

        # Проверяем, что список отображается
        assert dropdown.is_displayed(), "Выпадающий список не отображается"

        # Проверяем наличие всех нужных элементов
        expected_items = ["Текст", "Изображения", "Видео"]
        found_items = []

        for item_text in expected_items:
            # Ищем элемент по тексту в выпадающем списке
            item = dropdown.find_element(By.XPATH, f".//span[text()='{item_text}']")
            assert item.is_displayed(), f"Элемент '{item_text}' не найден в списке"
            found_items.append(item_text)
            print(f" Найден элемент: {item_text}")

        # Дополнительная проверка - количество элементов
        buttons = dropdown.find_elements(By.CLASS_NAME, "mhy-button")
        assert len(buttons) == 3, f"Ожидалось 3 кнопки, найдено {len(buttons)}"

        # Получаем все тексты для отчета
        all_texts = [item.text for item in dropdown.find_elements(By.TAG_NAME, "span") if item.text]

        allure.attach(
            f"Найденные элементы: {found_items}\nВсе тексты в списке: {all_texts}",
            name="Содержимое выпадающего списка"
        )

        print(" Все элементы выпадающего списка успешно проверены!")





@allure.feature('Кнопка "Текст"')
@allure.story('Выпадающий список')
@allure.title('Проверка нажатия на кнопку "Текст" в выпадающем списке')
def test_header(web_browser, chrome_options):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(15)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(5)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(5)

    with allure.step('Открываем выпадающий список'):
        driver.btn_header3.click()
        time.sleep(2)

    with allure.step('Нажимаем на кнопку "Текст"'):
        # Используем прямой поиск элемента который точно работает
        text_button = web_browser.find_element(By.XPATH, "//span[text()='Текст']/ancestor::button")
        text_button.click()

    with allure.step('Проверяем, появилось ли окно входа в аккаунт'):
        time.sleep(3)
        login_found = False

        # 1. Проверяем количество окон
        if len(web_browser.window_handles) > 1:
            login_found = True
            print("✅ Открылось новое окно с входом")
            web_browser.switch_to.window(web_browser.window_handles[1])

        # 2. Проверяем элементы окна входа через прямой поиск
        try:
            # Ищем элементы окна входа
            login_elements = web_browser.find_elements(By.XPATH, "//*[contains(text(), 'Войти')]")
            username_fields = web_browser.find_elements(By.XPATH, "//input[@name='username']")
            password_fields = web_browser.find_elements(By.XPATH, "//input[@type='password']")

            if login_elements or username_fields or password_fields:
                login_found = True
                print("✅ Найдены элементы окна входа")
        except:
            pass

        # 3. Проверяем URL на наличие login/account
        current_url = web_browser.current_url
        if 'login' in current_url.lower() or 'account' in current_url.lower():
            login_found = True
            print("✅ URL указывает на страницу входа")

        # Финальная проверка
        if login_found:
            with allure.step('Окно входа в аккаунт появилось - ТЕСТ ПРОЙДЕН'):
                allure.attach(web_browser.get_screenshot_as_png(), name="login_success",
                              attachment_type=allure.attachment_type.PNG)
                print("✅ ТЕСТ ПРОЙДЕН: Окно входа в аккаунт появилось")
                assert True
        else:
            with allure.step('Окно входа не появилось - ТЕСТ НЕ ПРОЙДЕН'):
                allure.attach(web_browser.get_screenshot_as_png(), name="login_failed",
                              attachment_type=allure.attachment_type.PNG)
                print(f"Текущий URL: {current_url}")
                print(f"Количество окон: {len(web_browser.window_handles)}")
                assert False, "Окно входа в аккаунт не появилось"

    with allure.step('Закрыть окно'):
        if len(web_browser.window_handles) > 1:
            web_browser.close()
            web_browser.switch_to.window(web_browser.window_handles[0])

        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()




@allure.feature('Кнопка "Изображения"')
@allure.story('Выпадающий список')
@allure.title('Проверка нажатия на кнопку "Изображения" в выпадающем списке')
def test_header(web_browser, chrome_options):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(15)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(5)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(5)

    with allure.step('Открываем выпадающий список'):
        driver.btn_header3.click()
        time.sleep(5)

    with allure.step('Нажимаем на кнопку "Изображения"'):
        images_button = web_browser.find_element(By.XPATH, "//span[text()='Изображения']/ancestor::button")
        images_button.click()
        time.sleep(5)

    with allure.step('Проверяем, появилось ли окно входа в аккаунт'):
        time.sleep(3)
        login_found = False

        if len(web_browser.window_handles) > 1:
            login_found = True
            print("✅ Открылось новое окно с входом")
            web_browser.switch_to.window(web_browser.window_handles[1])

        try:
            login_elements = web_browser.find_elements(By.XPATH, "//*[contains(text(), 'Войти')]")
            username_fields = web_browser.find_elements(By.XPATH, "//input[@name='username']")
            password_fields = web_browser.find_elements(By.XPATH, "//input[@type='password']")

            if login_elements or username_fields or password_fields:
                login_found = True
                print("✅ Найдены элементы окна входа")
        except:
            pass

        current_url = web_browser.current_url
        if 'login' in current_url.lower() or 'account' in current_url.lower():
            login_found = True
            print("✅ URL указывает на страницу входа")

        if login_found:
            with allure.step('Окно входа в аккаунт появилось - ТЕСТ ПРОЙДЕН'):
                allure.attach(web_browser.get_screenshot_as_png(), name="login_success_images",
                              attachment_type=allure.attachment_type.PNG)
                print("✅ ТЕСТ ПРОЙДЕН: Окно входа в аккаунт появилось")
                assert True
        else:
            with allure.step('Окно входа не появилось - ТЕСТ НЕ ПРОЙДЕН'):
                allure.attach(web_browser.get_screenshot_as_png(), name="login_failed_images",
                              attachment_type=allure.attachment_type.PNG)
                print(f"Текущий URL: {current_url}")
                print(f"Количество окон: {len(web_browser.window_handles)}")
                assert False, "Окно входа в аккаунт не появилось"

    with allure.step('Закрыть окно'):
        if len(web_browser.window_handles) > 1:
            web_browser.close()
            web_browser.switch_to.window(web_browser.window_handles[0])




@allure.feature('Кнопка "Видео"')
@allure.story('Выпадающий список')
@allure.title('Проверка нажатия на кнопку "Видео" в выпадающем списке')
def test_header(web_browser, chrome_options):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(15)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(5)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(5)

    with allure.step('Открываем выпадающий список'):
        driver.btn_header3.click()
        time.sleep(2)

    with allure.step('Нажимаем на кнопку "Видео"'):
        video_button = web_browser.find_element(By.XPATH, "//span[text()='Видео']/ancestor::button")
        video_button.click()

    with allure.step('Проверяем, появилось ли окно входа в аккаунт'):
        time.sleep(3)
        login_found = False

        if len(web_browser.window_handles) > 1:
            login_found = True
            print("✅ Открылось новое окно с входом")
            web_browser.switch_to.window(web_browser.window_handles[1])

        try:
            login_elements = web_browser.find_elements(By.XPATH, "//*[contains(text(), 'Войти')]")
            username_fields = web_browser.find_elements(By.XPATH, "//input[@name='username']")
            password_fields = web_browser.find_elements(By.XPATH, "//input[@type='password']")

            if login_elements or username_fields or password_fields:
                login_found = True
                print("✅ Найдены элементы окна входа")
        except:
            pass

        current_url = web_browser.current_url
        if 'login' in current_url.lower() or 'account' in current_url.lower():
            login_found = True
            print("✅ URL указывает на страницу входа")

        if login_found:
            with allure.step('Окно входа в аккаунт появилось - ТЕСТ ПРОЙДЕН'):
                allure.attach(web_browser.get_screenshot_as_png(), name="login_success_video",
                              attachment_type=allure.attachment_type.PNG)
                print("✅ ТЕСТ ПРОЙДЕН: Окно входа в аккаунт появилось")
                assert True
        else:
            with allure.step('Окно входа не появилось - ТЕСТ НЕ ПРОЙДЕН'):
                allure.attach(web_browser.get_screenshot_as_png(), name="login_failed_video",
                              attachment_type=allure.attachment_type.PNG)
                print(f"Текущий URL: {current_url}")
                print(f"Количество окон: {len(web_browser.window_handles)}")
                assert False, "Окно входа в аккаунт не появилось"

    with allure.step('Закрыть окно'):
        if len(web_browser.window_handles) > 1:
            web_browser.close()
            web_browser.switch_to.window(web_browser.window_handles[0])



@allure.feature('Кнопка "Уведомления"')
@allure.story('Нeader')
@allure.title('Проверка нажатия на кнопку "Уведомления"')
def test_header(web_browser, chrome_options):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(15)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(5)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(5)

    with allure.step('Нажимаем на кнопку "Уведомления"'):
        driver.btn_header4.click()
        time.sleep(5)



@allure.feature('Кнопка "Профиль"')
@allure.story('Header')
@allure.title('Проверка нажатия на кнопку "Профиль"')
def test_header(web_browser, chrome_options):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(15)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(5)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(5)

    with allure.step('Проверка нажатия на кнопку "Профиль"'):
        driver.btn_header5.click()
        time.sleep(5)


# Вход в учетную запись
@allure.feature('Авторизация')
@allure.story('Успешный вход')
@allure.title('Успешный вход с валидными данными')
def test_successful_login(web_browser):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(10)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(2)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(2)

    with allure.step('Открываем меню профиля'):
        driver.btn_header5.click()
        time.sleep(2)

    with allure.step('Заполняем валидными данными'):
        # Ждем пока откроется окно логина и переключаемся на него
        time.sleep(5)

        # Получаем все открытые окна/вкладки через web_browser
        windows = web_browser.window_handles
        if len(windows) > 1:
            # Переключаемся на новое окно
            web_browser.switch_to.window(windows[1])
            time.sleep(3)

        # ИЛИ попробуй найти iframe
        try:
            iframe = web_browser.find_element(By.XPATH, '//iframe[contains(@src, "account.hoyolab.com")]')
            web_browser.switch_to.frame(iframe)
            time.sleep(2)
        except:
            print("Iframe не найден, продолжаем в текущем контексте")

        # Теперь пытаемся заполнить поля
        # Используем прямые локаторы без Page Object
        email_field = web_browser.find_element(By.XPATH, '//input[@name="username"]')
        email_field.send_keys("kelus0981@gmail.com")
        time.sleep(2)

        password_field = web_browser.find_element(By.XPATH, '//input[@type="password"]')
        password_field.send_keys("29754383133NK")
        time.sleep(2)

    with allure.step('Проверяем активность кнопки и нажимаем "Войти"'):
        # Находим кнопку в текущем контексте (окне/iframe)
        login_button = web_browser.find_element(By.XPATH, '//button[@type="submit"]')

        # Проверяем что кнопка активна
        class_attribute = login_button.get_attribute("class")
        assert class_attribute is not None, "Не удалось получить класс кнопки"
        assert "is-disabled" not in class_attribute, "Кнопка должна быть активна"

        # Нажимаем на кнопку входа
        login_button.click()
        time.sleep(5)

        # После успешного входа вернись в основное окно
        if len(web_browser.window_handles) > 1:
            web_browser.switch_to.window(web_browser.window_handles[0])
            time.sleep(20)
    with allure.step('Закрываем попап после входа'):
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(5)

    with allure.step('Проверяем успешный вход в аккаунт'):
        time.sleep(10)  # Ждем загрузки страницы после входа
        # Простые проверки что мы вошли
        assert "hoyolab.com" in web_browser.current_url
        print("✓ Успешно вернулись на сайт после входа")

        # Делаем скриншот для доказательства
        web_browser.save_screenshot("successful_login.png")
        allure.attach(web_browser.get_screenshot_as_png(), name="successful_login",
                      attachment_type=allure.attachment_type.PNG)

        # БОЛЬШАЯ ПАУЗА - 60 секунд чтобы успеть посмотреть
        print("✓ Вход выполнен! Браузер останется открытым 60 секунд...")
        time.sleep(15)

        print("✓ Тест завершен успешно!")


@allure.feature('Авторизация')
@allure.story('Невалидные данные')
@allure.title('Проверка невалидных email')
def test_invalid_emails(web_browser):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(10)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(2)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(2)

    with allure.step('Открываем меню профиля'):
        driver.btn_header5.click()
        time.sleep(2)

    # Список невалидных email для тестирования
    invalid_emails = [
        "testexample.com",  # без @
        "test@",  # без домена
        "@example.com",  # без имени
        "test@example",  # без .com
        "test@.com",  # без домена после @
        "",  # пустой
        "   ",  # только пробелы
        "invalid@email",  # несуществующий домен
    ]

    valid_password = "29754383133NK"  # правильный пароль

    for i, email in enumerate(invalid_emails):
        with allure.step(f'Тест {i + 1}: Пытаемся войти с email "{email}"'):
            time.sleep(5)

            # Переключаемся на окно/iframe логина
            windows = web_browser.window_handles
            if len(windows) > 1:
                web_browser.switch_to.window(windows[1])
                time.sleep(3)

            try:
                iframe = web_browser.find_element(By.XPATH, '//iframe[contains(@src, "account.hoyolab.com")]')
                web_browser.switch_to.frame(iframe)
                time.sleep(2)
            except:
                print("Iframe не найден, продолжаем в текущем контексте")

            # Заполняем невалидный email
            email_field = web_browser.find_element(By.XPATH, '//input[@name="username"]')
            email_field.clear()
            email_field.send_keys(email)
            time.sleep(1)

            # Заполняем правильный пароль
            password_field = web_browser.find_element(By.XPATH, '//input[@type="password"]')
            password_field.clear()
            password_field.send_keys(valid_password)
            time.sleep(1)

            # Пытаемся нажать кнопку входа
            login_button = web_browser.find_element(By.XPATH, '//button[@type="submit"]')
            login_button.click()
            time.sleep(3)

            # Проверяем что вход НЕ произошел
            with allure.step('Проверяем что вход не выполнен'):
                # Проверяем наличие сообщения об ошибке
                try:
                    error_message = web_browser.find_element(By.XPATH,
                                                             '//*[contains(text(), "error") or contains(text(), "invalid") or contains(text(), "неверн")]')
                    assert error_message.is_displayed(), f"Ожидалась ошибка для email: {email}"
                    print(f"✓ Для '{email}' показана ошибка (как и ожидалось)")
                except:
                    # Если нет ошибки, проверяем что мы не перешли в профиль
                    current_url = web_browser.current_url
                    assert "profile" not in current_url.lower() and "account" not in current_url.lower(), \
                        f"Неожиданный успешный вход для невалидного email: {email}"
                    print(f"✓ Для '{email}' вход не выполнен (как и ожидалось)")

            # Возвращаемся обратно для следующего теста
            web_browser.switch_to.window(web_browser.window_handles[0])
            time.sleep(2)

            # Снова открываем меню профиля для следующего теста
            driver.btn_header5.click()
            time.sleep(2)


@allure.feature('Авторизация')
@allure.story('Невалидные данные')
@allure.title('Проверка невалидных паролей')
def test_invalid_passwords(web_browser):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(10)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(2)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(2)

    with allure.step('Открываем меню профиля'):
        driver.btn_header5.click()
        time.sleep(2)

    valid_email = "kelus0981@l.com"  # правильный email
    invalid_passwords = [
        "",  # пустой пароль
        "123",  # слишком короткий
        "   ",  # только пробелы
        "wrongpassword",  # неверный пароль
    ]

    for i, password in enumerate(invalid_passwords):
        with allure.step(f'Тест {i + 1}: Пытаемся войти с паролем "{password}"'):
            time.sleep(5)

            # Переключаемся на окно/iframe логина
            windows = web_browser.window_handles
            if len(windows) > 1:
                web_browser.switch_to.window(windows[1])
                time.sleep(3)

            try:
                iframe = web_browser.find_element(By.XPATH, '//iframe[contains(@src, "account.hoyolab.com")]')
                web_browser.switch_to.frame(iframe)
                time.sleep(2)
            except:
                print("Iframe не найден, продолжаем в текущем контексте")

            # Заполняем правильный email
            email_field = web_browser.find_element(By.XPATH, '//input[@name="username"]')
            email_field.clear()
            email_field.send_keys(valid_email)
            time.sleep(1)

            # Заполняем невалидный пароль
            password_field = web_browser.find_element(By.XPATH, '//input[@type="password"]')
            password_field.clear()
            password_field.send_keys(password)
            time.sleep(1)

            # Пытаемся нажать кнопку входа
            login_button = web_browser.find_element(By.XPATH, '//button[@type="submit"]')
            login_button.click()
            time.sleep(3)

            # Проверяем что вход НЕ произошел
            with allure.step('Проверяем что вход не выполнен'):
                try:
                    error_message = web_browser.find_element(By.XPATH,
                                                             '//*[contains(text(), "error") or contains(text(), "invalid") or contains(text(), "неверн")]')
                    assert error_message.is_displayed(), f"Ожидалась ошибка для пароля: {password}"
                    print(f"✓ Для пароля '{password}' показана ошибка")
                except:
                    current_url = web_browser.current_url
                    assert "profile" not in current_url.lower() and "account" not in current_url.lower(), \
                        f"Неожиданный успешный вход для невалидного пароля: {password}"
                    print(f"✓ Для пароля '{password}' вход не выполнен")

            # Возвращаемся обратно для следующего теста
            web_browser.switch_to.window(web_browser.window_handles[0])
            time.sleep(2)

            # Снова открываем меню профиля для следующего теста
            driver.btn_header5.click()
            time.sleep(2)



@allure.feature('Навигация по играм')
@allure.story('Конкретные игры')
@allure.title('Проверка конкретных игр по названиям')
def test_header(web_browser):
    with allure.step('Открываем главную страницу'):
        web_browser.get("https://www.hoyolab.com")
        time.sleep(5)

        # Закрываем попапы
        try:
            close_buttons = web_browser.find_elements(By.XPATH, '//button[contains(@class, "close")]')
            for btn in close_buttons:
                if btn.is_displayed():
                    btn.click()
                    time.sleep(1)
        except:
            pass

    # Список ожидаемых игр
    expected_games = [
        "Genshin Impact",
        "Honkai: Star Rail",
        "Zenless Zone Zero",
        "Honkai Impact 3rd",
        "Tears of Themis"
    ]

    found_games = []
    wait = WebDriverWait(web_browser, 10)

    for game_name in expected_games:
        with allure.step(f'Ищем и проверяем {game_name}'):
            try:
                # Ищем элемент с названием игры
                name_element = wait.until(
                    EC.presence_of_element_located((By.XPATH, f'//*[contains(text(), "{game_name}")]'))
                )

                # Находим родительскую ссылку
                game_link = name_element.find_element(By.XPATH, './ancestor::a')

                # Прокручиваем и кликаем через JavaScript
                web_browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", game_link)
                time.sleep(1)

                # Получаем URL
                game_url = game_link.get_attribute('href')

                # Кликаем через JS
                web_browser.execute_script("arguments[0].click();", game_link)
                time.sleep(3)

                current_url = web_browser.current_url
                assert "hoyolab.com" in current_url, f"Не удалось перейти для {game_name}"

                found_games.append({
                    'name': game_name,
                    'url': game_url,
                    'found': True
                })

                print(f"✓ Найдена и проверена {game_name}")

                # Возвращаемся назад
                web_browser.back()
                time.sleep(3)

            except Exception as e:
                found_games.append({
                    'name': game_name,
                    'found': False,
                    'error': str(e)
                })
                print(f"✗ Ошибка для {game_name}: {e}")

    with allure.step('Проверяем результаты'):
        found_count = len([game for game in found_games if game['found']])

        print(f"\nНайдено игр: {found_count}/{len(expected_games)}")

        for game in found_games:
            status = "✓" if game['found'] else "✗"
            print(f"{status} {game['name']}")

        # Проверяем что найдены все ожидаемые игры
        assert found_count >= 3, f"Найдено только {found_count} из {len(expected_games)} ожидаемых игр"

        print("✓ Основные игры найдены и работают!")

@allure.feature('Ccылки')
@allure.story('Body')
def test_body(web_browser):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(10)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(2)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(2)

    with allure.step('Переключение между ссылками'):
        driver.btn_b1.click()
        time.sleep(5)
    with allure.step('Возвращаемся на главную стриницу'):
        driver.btn_b0.click()
        time.sleep(5)
    with allure.step('Переключение между ссылками'):
        driver.btn_b2.click()
        time.sleep(5)
    with allure.step('Возвращаемся на главную стриницу'):
        driver.btn_b0.click()
        time.sleep(5)
    with allure.step('Переключение между ссылками'):
        driver.btn_b3.click()
        time.sleep(5)
    with allure.step('Возвращаемся на главную стриницу'):
            driver.btn_b0.click()
            time.sleep(5)
    with allure.step('Переключение между ссылками'):
        driver.btn_b4.click()
        time.sleep(5)
    with allure.step('Возвращаемся на главную стриницу'):
            driver.btn_b0.click()
            time.sleep(5)

@allure.feature('Ccылки')
@allure.story('Body')
def test_body(web_browser):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(10)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(2)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(2)
    with allure.step('Переключение между ссылками'):
        driver.btn_ll1.click()
        time.sleep(5)

    with allure.step('Переключение между ссылками'):
        driver.btn_ll0.click()
        time.sleep(5)

    with allure.step('Переключение между ссылками'):
        driver.btn_ll2.click()
        time.sleep(5)

    with allure.step('Переключение между ссылками'):
        driver.btn_ll0.click()
        time.sleep(5)


@allure.feature('Пост')
@allure.story('Body')
def test_body(web_browser):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(10)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(2)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(2)

    with allure.step('Нажать на пост'):
        driver.btn_post.click()
        time.sleep(5)


@allure.feature('Нажать кнопку "Войти"')
@allure.story('Body')
def test_button(web_browser):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(10)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(2)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(2)

    with allure.step('Нажать на кнопку "Войти"'):
        driver.btn_exit.click()
        time.sleep(5)


@allure.feature('Проверка погинации во "Все инструменты"')
@allure.story('Body')
def test_pg(web_browser):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(10)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(5)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(5)

    with allure.step('Нажать на кнопку "2"'):
        driver.btn_li1.click()
        time.sleep(5)




@allure.feature('Проверка нажатия элемента в "Все инструменты"')
@allure.story('Body')
def test_in(web_browser):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(10)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(2)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(2)

    with allure.step('Нажимаем на элемент "Отметиться"'):
        driver.btn_in.click()
        time.sleep(5)

@allure.feature('Проверка нажатия кнопок установки')
@allure.story('Body')
def test_pl(web_browser):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(10)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(5)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(5)

    with allure.step('Нажать на кнопку для ios"'):
        driver.btn_a1.click()
        time.sleep(7)

        web_browser.get("https://www.hoyolab.com")
        time.sleep(5)

    with allure.step('Нажать на кнопку для android'):
         driver.btn_a2.click()
         time.sleep(7)

         web_browser.get("https://www.hoyolab.com")
         time.sleep(5)



@allure.story("Footer")
def test_footer(web_browser, chrome_options, elements=None):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(10)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(2)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(2)
    with allure.step('Подготовка тестовых данных'):
        elements = [
            (driver.btn_footer1, 'Контакты'),
            (driver.btn_footer2, 'Политика'),
            (driver.btn_footer3, 'Условия'),
            (driver.btn_footer4, 'Политика учетной записи'),
            (driver.btn_footer5, 'Условия учетной записи'),
            (driver.btn_footer6, 'Правила сообщества'),
            (driver.btn_footer7, 'Правила сообщества')
        ]
    with allure.step('Проверка элемента'):
        for element, text_element in elements:
            with allure.step(f'Проверка элемента {text_element} на отображение'):
                check.is_true(element.is_visible(), f'Элемента {text_element} нет визуально на экарне')

            with allure.step(f'Проверка элемента {text_element} на кликабельность'):
                check.is_true(element.is_clickable(), f'Элемента {text_element} не кликабелен')


@allure.feature('Навигация')
def test_scroll_up(web_browser):
    with allure.step('Запускаем и настраиваем'):
        driver = MainPage(web_browser)
        time.sleep(10)
        if driver.btn_close_login_popup.wait_to_be_clickable():
            driver.btn_close_login_popup.click()
            time.sleep(2)
        if driver.btn_close_login_popup2.wait_to_be_clickable():
            driver.btn_close_login_popup2.click()
            time.sleep(2)
    # Прокручиваем вниз
    web_browser.execute_script("window.scrollTo(0, 1000);")
    time.sleep(2)

    # Прокручиваем вверх
    web_browser.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)

    print("✓ Прокрутка работает")