import allure
from allure_commons.types import Severity
from allure_commons.types import LabelType

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Valeria_Pavlovich.Home_work.Home_work_7.locators.locators_id import LocatorsWebTables as Cl

def close_modal_if_open(driver, retries: int = 3):
    for _ in range(retries):
        try:
            btn = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, Cl.close_button))
            )
            btn.click()
            WebDriverWait(driver, 2).until(
                EC.invisibility_of_element_located((By.XPATH, Cl.registration_form))
            )
            return
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
            return

def any_row_contains_text(locator, text):
    def _predicate(driver):
        rows = driver.find_elements(*locator)
        return any(text in row.text for row in rows)
    return _predicate

@allure.title("Проверка открытия и закрытия формы регистрации")
@allure.description("Проверка, что при нажатии на кнопку Add открывается форма регистрации, и её можно закрыть.")
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "Python")
@allure.id("ADD-1")
@allure.manual
@allure.link("https://trello.com/b/ggVRZ2Oo/web-tables", name="Тест-кейсы теста")
@allure.epic("UI автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
def test_click_add_button(driver):
    close_modal_if_open(driver)

    with allure.step("Нажимаем на кнопку Add для открытия формы регистрации"):
        driver.find_element(By.XPATH, Cl.add_button).click()

    with allure.step("Ожидаем появления формы регистрации"):
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, Cl.registration_form))
        )

    with allure.step("Закрываем форму регистрации"):
        close = driver.find_element(By.XPATH, Cl.close_button)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", close)
        close.click()

    with allure.step("Проверяем, что форма регистрации закрылась"):
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, Cl.registration_form))
        )

@allure.title("Добавление записи со всеми валидными полями")
@allure.description("Проверка, что пользователь может заполнить все поля формы регистрации валидными данными и добавить запись в таблицу.")
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "Python")
@allure.id("ADD-2")
@allure.manual
@allure.link("https://trello.com/b/ggVRZ2Oo/web-tables", name="Тест-кейсы теста")
@allure.epic("UI автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
def test_fill_all_fields(driver):
    close_modal_if_open(driver)

    with allure.step("Подготавливаем валидные тестовые данные"):
        test_data = {
            Cl.first_name: "Alice",
            Cl.last_name:  "Smith",
            Cl.email:      "rabbit@forest.com",
            Cl.age:        "25",
            Cl.salary:     "5000",
            Cl.dept:       "Customer support"
        }

    with allure.step("Открываем форму регистрации"):
        driver.find_element(By.XPATH, Cl.add_button).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, Cl.registration_form))
        )

    with allure.step("Заполняем форму валидными данными"):
        for locator, value in test_data.items():
            field = driver.find_element(By.XPATH, locator)
            field.clear()
            field.send_keys(value)

    with allure.step("Отправляем форму"):
        submit = driver.find_element(By.XPATH, Cl.submit_button)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit)
        submit.click()

    with allure.step("Проверяем, что запись появилась в таблице"):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//div[@role='row' and contains(., '{test_data[Cl.first_name]}')]")
            )
        )
        rows = driver.find_elements(By.XPATH, "//div[@role='row']")
        texts = [r.text for r in rows]
        assert any(
            test_data[Cl.first_name] in t and
            test_data[Cl.last_name] in t and
            test_data[Cl.email] in t and
            test_data[Cl.age] in t and
            test_data[Cl.salary] in t and
            test_data[Cl.dept]
            for t in texts
        ), f"Не найдена строка с введёнными данными в {texts}"

@allure.title("Добавление записи с пустыми полями")
@allure.description("Проверка, что при попытке добавить запись с пустыми полями форма остаётся открытой, а таблица не изменяется.")
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "Python")
@allure.id("ADD-3")
@allure.manual
@allure.link("https://trello.com/b/ggVRZ2Oo/web-tables", name="Тест-кейсы теста")
@allure.epic("UI автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
def test_add_empty_record(driver):
    close_modal_if_open(driver)

    with allure.step("Фиксируем количество строк до добавления"):
        count_before = len(driver.find_elements(By.XPATH, Cl.table_rows))

    with allure.step("Открываем форму регистрации"):
        driver.find_element(By.XPATH, Cl.add_button).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, Cl.registration_form))
        )

    with allure.step("Оставляем все поля пустыми"):
        for locator in (Cl.first_name, Cl.last_name, Cl.email, Cl.age, Cl.salary, Cl.dept):
            driver.find_element(By.XPATH, locator).clear()

    with allure.step("Пытаемся отправить пустую форму"):
        driver.find_element(By.XPATH, Cl.submit_button).click()
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Cl.registration_form))
        )

    with allure.step("Проверяем, что количество строк не изменилось"):
        count_after = len(driver.find_elements(By.XPATH, Cl.table_rows))
        assert count_after == count_before, (
            f"Ожидалось {count_before}, но стало {count_after} — пустая запись добавилась"
        )

@allure.title('Проверка поля First Name')
@allure.description("Проверка граничных значений поля First Name.")
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "Python")
@allure.id("ADD-4")
@allure.manual
@allure.link("https://trello.com/b/ggVRZ2Oo/web-tables", name="Тест-кейсы теста")
@allure.epic("UI автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
@pytest.mark.parametrize(
    "first_name, expected_submit, case_id",
    [
        ("",           False, "empty"),
        ("Алиса",      False, "non_latin"),
        ("12345",      False, "digits"),
        ("!@#$%",      False, "specials"),
        ("a" * 26,     False, "too_long"),
        ("Alice",      True,  "valid"),
    ]
)
def test_first_name_validation(driver, first_name, expected_submit, case_id):
    close_modal_if_open(driver)

    allure.dynamic.title(
        f"[{case_id}] Проверка поля First Name: '{first_name}' → "
        f"{'успешно' if expected_submit else 'ошибка'}"
    )
    allure.dynamic.description(
        f"Проверка валидации поля First Name при вводе '{first_name}'. "
        f"Ожидается {'успешная отправка' if expected_submit else 'ошибка и отсутствие записи'}."
    )
    allure.dynamic.tag("Smoke")
    allure.dynamic.feature("Раздел Elements")
    allure.dynamic.story("Вкладка Web Tables")
    allure.dynamic.label("case_id", case_id)

    with allure.step("Открываем форму регистрации"):
        driver.find_element(By.XPATH, Cl.add_button).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Cl.registration_form))
        )

    test_data = {
        Cl.first_name: first_name,
        Cl.last_name:  "Smith",
        Cl.email:      "rabbit@forest.com",
        Cl.age:        "25",
        Cl.salary:     "5000",
        Cl.dept:       "Customer support",
    }

    for locator, value in test_data.items():
        with allure.step(f"Вводим '{value}' в поле {locator}"):
            el = driver.find_element(By.XPATH, locator)
            el.clear()
            el.send_keys(value)

            if locator == Cl.first_name:
                actual = el.get_attribute("value")
                assert actual == value, (
                    f"[{case_id}] Ожидали '{value}' ({len(value)}), "
                    f"получили '{actual}' ({len(actual)})"
                )

    with allure.step("Отправляем форму"):
        driver.find_element(By.XPATH, Cl.submit_button).click()

    if not expected_submit:
        with allure.step("Проверяем, что форма осталась открытой и запись не добавлена"):
            assert WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Cl.registration_form))
            ), f"[{case_id}] Форма закрылась, хотя ввод невалиден"

            rows = driver.find_elements(By.XPATH, Cl.table_rows_all)
            assert all(first_name not in r.text for r in rows), (
                f"[{case_id}] Некорректная запись появилась в таблице"
            )
    else:
        with allure.step("Проверяем, что запись появилась в таблице"):
            locator = (By.XPATH, Cl.table_rows_all)
            WebDriverWait(driver, 10).until(
                any_row_contains_text(locator, first_name),
                message=f"[{case_id}] Не дождались строки с '{first_name}'"
            )
            rows = driver.find_elements(*locator)
            assert any(first_name in r.text for r in rows), (
                f"[{case_id}] Валидная запись не найдена"
            )

@allure.title('Проверка поля Last Name')
@allure.description("Проверка граничных значений поля Last Name.")
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "Python")
@allure.id("ADD-5")
@allure.manual
@allure.link("https://trello.com/b/ggVRZ2Oo/web-tables", name="Тест-кейсы теста")
@allure.epic("UI автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
@pytest.mark.parametrize(
    "last_name, expected_submit, case_id",
    [
        ("",           False, "empty"),
        ("Смит",      False, "non_latin"),
        ("12345",      False, "digits"),
        ("!@#$%",      False, "specials"),
        ("a" * 26,     False, "too_long"),
        ("Smith",      True,  "valid"),
    ]
)
def test_last_name_validation(driver, last_name, expected_submit, case_id):
    close_modal_if_open(driver)

    allure.dynamic.title(
        f"[{case_id}] Проверка поля Last Name: '{last_name}' → "
        f"{'успешно' if expected_submit else 'ошибка'}"
    )
    allure.dynamic.description(
        f"Проверка валидации поля Last Name при вводе '{last_name}'. "
        f"Ожидается {'успешная отправка' if expected_submit else 'ошибка и отсутствие записи'}."
    )
    allure.dynamic.tag("Smoke")
    allure.dynamic.feature("Раздел Elements")
    allure.dynamic.story("Вкладка Web Tables")
    allure.dynamic.label("case_id", case_id)

    with allure.step("Открываем форму регистрации"):
        driver.find_element(By.XPATH, Cl.add_button).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Cl.registration_form))
        )

    test_data = {
        Cl.first_name: "Alice",
        Cl.last_name:  last_name,
        Cl.email:      "rabbit@forest.com",
        Cl.age:        "25",
        Cl.salary:     "5000",
        Cl.dept:       "Customer support",
    }

    for locator, value in test_data.items():
        with allure.step(f"Вводим '{value}' в поле {locator}"):
            el = driver.find_element(By.XPATH, locator)
            el.clear()
            el.send_keys(value)

            if locator == Cl.last_name:
                actual_value = el.get_attribute("value")
                assert actual_value == value, (
                    f"[{case_id}] Ожидали '{value}' ({len(value)}), "
                    f"получили '{actual_value}' ({len(actual_value)})"
                )

    with allure.step("Отправляем форму"):
        driver.find_element(By.XPATH, Cl.submit_button).click()

    if not expected_submit:
        with allure.step("Проверяем, что форма осталась открытой и запись не добавлена"):
            assert WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Cl.registration_form))
            ), f"[{case_id}] Форма закрылась, хотя ввод невалиден"

            rows = driver.find_elements(By.XPATH, Cl.table_rows_all)
            assert all(last_name not in r.text for r in rows), (
                f"[{case_id}] Некорректная запись появилась в таблице"
            )
    else:
        with allure.step("Проверяем, что запись появилась в таблице"):
            locator = (By.XPATH, Cl.table_rows_all)
            WebDriverWait(driver, 10).until(
                any_row_contains_text(locator, last_name),
                message=f"[{case_id}] Не дождались строки с '{last_name}'"
            )
            rows = driver.find_elements(*locator)
            assert any(last_name in r.text for r in rows), (
                f"[{case_id}] Валидная запись не найдена"
            )

@allure.title('Проверка поля Email')
@allure.description("Проверка граничных значений поля Email.")
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "Python")
@allure.id("ADD-6")
@allure.manual
@allure.link("https://trello.com/b/ggVRZ2Oo/web-tables", name="Тест-кейсы теста")
@allure.epic("UI автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
@pytest.mark.parametrize(
    "email, expected_submit, case_id",
    [
        ("",                          False, "empty"),
        ("rabbitforest.com",            False, "no_at"),
        ("rabbit@forest",               False, "no_tld"),
        ("rabbit@forest.c",             False, "one_char_tld"),
        ("кролик@forest.com",           False, "non_latin_local"),
        ("rabbit@лес.com",            False, "non_latin_domain"),
        ("rabbit@forest.co",            True,  "valid_two_letter_tld"),
    ]
)
def test_email_validation(driver, email, expected_submit, case_id):
    rows_before = driver.find_elements(By.XPATH, Cl.table_rows_all)

    close_modal_if_open(driver)
    allure.dynamic.title(
        f"[{case_id}] Проверка Email: '{email}' → "
        f"{'успех' if expected_submit else 'ошибка'}"
    )
    allure.dynamic.description(
        f"При вводе '{email}' в поле Email ожидается "
        f"{'успешная отправка' if expected_submit else 'ошибка и отсутствие записи'}."
    )
    allure.dynamic.tag("Smoke")
    allure.dynamic.feature("Раздел Elements")
    allure.dynamic.story("Вкладка Web Tables")
    allure.dynamic.label("case_id", case_id)

    with allure.step("Открываем форму регистрации"):
        driver.find_element(By.XPATH, Cl.add_button).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Cl.registration_form))
        )

    test_data = {
        Cl.first_name: "Alice",
        Cl.last_name:  "Smith",
        Cl.email:      email,
        Cl.age:        "25",
        Cl.salary:     "5000",
        Cl.dept:       "Customer support",
    }

    for locator, value in test_data.items():
        with allure.step(f"Вводим '{value}' в поле {locator}"):
            el = driver.find_element(By.XPATH, locator)
            el.clear()
            el.send_keys(value)
            if locator == Cl.email:
                actual = el.get_attribute("value")
                assert actual == value, (
                    f"[{case_id}] Поле Email ожидает '{value}', получили '{actual}'"
                )

    with allure.step("Отправляем форму"):
        driver.find_element(By.XPATH, Cl.submit_button).click()

    if not expected_submit:
        with allure.step("Проверяем, что форма осталась открытой"):
            assert WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Cl.registration_form))
            ), f"[{case_id}] Форма закрылась при невалидном Email"

        with allure.step("Проверяем, что строк не добавилось"):
            rows_after = driver.find_elements(By.XPATH, Cl.table_rows_all)
            assert len(rows_after) == len(rows_before), (
                f"[{case_id}] Ожидали {len(rows_before)} строк, получили {len(rows_after)}"
            )
    else:
        with allure.step("Проверяем, что запись с правильным Email добавлена"):
            locator = (By.XPATH, Cl.table_rows_all)
            WebDriverWait(driver, 10).until(
                any_row_contains_text(locator, email),
                message=f"[{case_id}] Не дождались строки с Email '{email}'"
            )
            rows = driver.find_elements(*locator)
            assert any(email in r.text for r in rows), (
                f"[{case_id}] Валидная запись с Email '{email}' не найдена"
            )

@allure.title('Проверка поля Age')
@allure.description("Проверка граничных значений поля Age.")
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "Python")
@allure.id("ADD-7")
@allure.manual
@allure.link("https://trello.com/b/ggVRZ2Oo/web-tables", name="Тест-кейсы теста")
@allure.epic("UI автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
@pytest.mark.parametrize(
    "age, expected_submit, case_id",
    [
        ("",      False, "empty"),
        ("abc",   False, "letters"),
        ("!@#$%", False, "specials"),
        ("1234",  False, "too_long"),
        ("25",    True,  "valid_two_digits"),
        ("100",   True,  "valid_three_digits"),
    ]
)
def test_age_validation(driver, age, expected_submit, case_id):
    close_modal_if_open(driver)

    allure.dynamic.title(
        f"[{case_id}] Проверка поля Age: '{age}' → "
        f"{'успешно' if expected_submit else 'ошибка'}"
    )
    allure.dynamic.description(
        f"Проверка валидации поля Age при вводе '{age}'. "
        f"Ожидается {'успешная отправка' if expected_submit else 'ошибка и отсутствие записи'}."
    )
    allure.dynamic.tag("Smoke")
    allure.dynamic.feature("Раздел Elements")
    allure.dynamic.story("Вкладка Web Tables")
    allure.dynamic.label("case_id", case_id)

    with allure.step("Открываем форму регистрации"):
        driver.find_element(By.XPATH, Cl.add_button).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Cl.registration_form))
        )

    test_data = {
        Cl.first_name: "Alice",
        Cl.last_name:  "Smith",
        Cl.email:      "rabbit@forest.com",
        Cl.age:        age,
        Cl.salary:     "5000",
        Cl.dept:       "Customer support",
    }

    for locator, value in test_data.items():
        with allure.step(f"Вводим '{value}' в поле {locator}"):
            el = driver.find_element(By.XPATH, locator)
            el.clear()
            el.send_keys(value)

            if locator == Cl.age:
                actual = el.get_attribute("value")
                assert actual == value, (
                    f"[{case_id}] Ожидали '{value}' ({len(value)}), "
                    f"получили '{actual}' ({len(actual)})"
                )

    with allure.step("Отправляем форму"):
        driver.find_element(By.XPATH, Cl.submit_button).click()

    if not expected_submit:
        with allure.step("Проверяем, что форма осталась открытой и запись не добавлена"):
            assert WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Cl.registration_form))
            ), f"[{case_id}] Форма закрылась, хотя ввод невалиден"

            rows = driver.find_elements(By.XPATH, Cl.table_rows_all)
            assert all(age not in r.text for r in rows), (
                f"[{case_id}] Некорректная запись появилась в таблице"
            )
    else:
        with allure.step("Проверяем, что запись появилась в таблице"):
            locator = (By.XPATH, Cl.table_rows_all)
            WebDriverWait(driver, 10).until(
                any_row_contains_text(locator, age),
                message=f"[{case_id}] Не дождались строки с '{age}'"
            )
            rows = driver.find_elements(*locator)
            assert any(age in r.text for r in rows), (
                f"[{case_id}] Валидная запись не найдена"
            )
@allure.title('Проверка поля Salary')
@allure.description("Проверка валидации поля Salary: буквы и спецсимволы не вводятся, более 11 цифр отбрасывается.")
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "Python")
@allure.id("ADD-8")
@allure.manual
@allure.link("https://trello.com/b/ggVRZ2Oo/web-tables", name="Тест-кейсы теста")
@allure.epic("UI автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
@pytest.mark.parametrize(
    "salary, expected_submit, case_id",
    [
        ("",                False, "empty"),
        ("abc",             False, "letters"),
        ("!@#$%",           False, "specials"),
        ("123456789012",    False, "too_long"),
        ("5000",            True,  "valid_four_digits"),
        ("12345678901",     True,  "valid_eleven_digits"),
    ]
)
def test_salary_validation(driver, salary, expected_submit, case_id):
    close_modal_if_open(driver)

    allure.dynamic.title(
        f"[{case_id}] Проверка Salary: '{salary}' → "
        f"{'успешно' if expected_submit else 'ошибка'}"
    )
    allure.dynamic.description(
        f"При вводе '{salary}' в поле Salary ожидается "
        f"{'успешная отправка' if expected_submit else 'ошибка и отсутствие записи'}."
    )
    allure.dynamic.tag("Smoke")
    allure.dynamic.feature("Раздел Elements")
    allure.dynamic.story("Вкладка Web Tables")
    allure.dynamic.label("case_id", case_id)

    with allure.step("Открываем форму регистрации"):
        driver.find_element(By.XPATH, Cl.add_button).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Cl.registration_form))
        )

    test_data = {
        Cl.first_name: "Alice",
        Cl.last_name:  "Smith",
        Cl.email:      "rabbit@forest.com",
        Cl.age:        "25",
        Cl.salary:     salary,
        Cl.dept:       "Customer support",
    }

    for locator, value in test_data.items():
        with allure.step(f"Вводим '{value}' в поле {locator}"):
            el = driver.find_element(By.XPATH, locator)
            el.clear()
            el.send_keys(value)

            if locator == Cl.salary:
                actual = el.get_attribute("value")
                filtered = "".join(filter(str.isdigit, value))[:11]
                assert actual == filtered, (
                    f"[{case_id}] Ожидали '{filtered}' ({len(filtered)}), "
                    f"получили '{actual}' ({len(actual)})"
                )

    with allure.step("Отправляем форму"):
        driver.find_element(By.XPATH, Cl.submit_button).click()

    if not expected_submit:
        with allure.step("Проверяем, что форма осталась открытой и запись не добавлена"):
            assert WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Cl.registration_form))
            ), f"[{case_id}] Форма закрылась, хотя Salary невалиден"
            rows = driver.find_elements(By.XPATH, Cl.table_rows_all)
            assert all(salary not in r.text for r in rows), (
                f"[{case_id}] Некорректная запись появилась в таблице"
            )
    else:
        with allure.step("Проверяем, что запись появилась в таблице"):
            filtered = "".join(filter(str.isdigit, salary))[:11]
            locator = (By.XPATH, Cl.table_rows_all)
            WebDriverWait(driver, 10).until(
                any_row_contains_text(locator, filtered),
                message=f"[{case_id}] Не дождались строки с '{filtered}'"
            )
            rows = driver.find_elements(*locator)
            assert any(filtered in r.text for r in rows), (
                f"[{case_id}] Валидная запись не найдена"
            )

@allure.title('Проверка поля Department')
@allure.description("Проверка граничных значений поля Department.")
@allure.tag("Smoke")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "Python")
@allure.id("ADD-9")
@allure.manual
@allure.link("https://trello.com/b/ggVRZ2Oo/web-tables", name="Тест-кейсы теста")
@allure.epic("UI автотесты")
@allure.feature("Раздел Elements")
@allure.story("Вкладка Web Tables")
@pytest.mark.parametrize(
    "department, expected_submit, case_id",
    [
        ("",                   False, "empty"),
        ("Поддержка",          False, "non_latin"),
        ("12345",              False, "digits"),
        ("!@#$%",              False, "specials"),
        ("a" * 26,             False, "too_long"),
        ("Customer support",   True,  "valid"),
    ]
)
def test_department_validation(driver, department, expected_submit, case_id):
    close_modal_if_open(driver)

    allure.dynamic.title(
        f"[{case_id}] Проверка поля Department: '{department}' → "
        f"{'успешно' if expected_submit else 'ошибка'}"
    )
    allure.dynamic.description(
        f"Проверка валидации поля Department при вводе '{department}'. "
        f"Ожидается {'успешная отправка' if expected_submit else 'ошибка и отсутствие записи'}."
    )
    allure.dynamic.tag("Smoke")
    allure.dynamic.feature("Раздел Elements")
    allure.dynamic.story("Вкладка Web Tables")
    allure.dynamic.label("case_id", case_id)

    with allure.step("Открываем форму регистрации"):
        driver.find_element(By.XPATH, Cl.add_button).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Cl.registration_form))
        )

    test_data = {
        Cl.first_name: "Alice",
        Cl.last_name:  "Smith",
        Cl.email:      "rabbit@forest.com",
        Cl.age:        "25",
        Cl.salary:     "5000",
        Cl.dept:       department,
    }

    for locator, value in test_data.items():
        with allure.step(f"Вводим '{value}' в поле {locator}"):
            el = driver.find_element(By.XPATH, locator)
            el.clear()
            el.send_keys(value)

            if locator == Cl.dept:
                actual_value = el.get_attribute("value")
                assert actual_value == value, (
                    f"[{case_id}] Ожидали '{value}' ({len(value)}), "
                    f"получили '{actual_value}' ({len(actual_value)})"
                )

    with allure.step("Отправляем форму"):
        driver.find_element(By.XPATH, Cl.submit_button).click()

    if not expected_submit:
        with allure.step("Проверяем, что форма осталась открытой и запись не добавлена"):
            assert WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Cl.registration_form))
            ), f"[{case_id}] Форма закрылась, хотя ввод невалиден"

            rows = driver.find_elements(By.XPATH, Cl.table_rows_all)
            assert all(department not in r.text for r in rows), (
                f"[{case_id}] Некорректная запись появилась в таблице"
            )
    else:
        with allure.step("Проверяем, что запись появилась в таблице"):
            locator = (By.XPATH, Cl.table_rows_all)
            WebDriverWait(driver, 10).until(
                any_row_contains_text(locator, department),
                message=f"[{case_id}] Не дождались строки с '{department}'"
            )
            rows = driver.find_elements(*locator)
            assert any(department in r.text for r in rows), (
                f"[{case_id}] Валидная запись не найдена"
            )
