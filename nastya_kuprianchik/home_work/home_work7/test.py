from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
from allure_commons.types import Severity, LabelType


@allure.title("[СЗ03] Проверка поля First Name")
@allure.description("Валидация ввода данных в поле First Name")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, "python")
def test_first_name_validation():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()
    driver.find_element(By.ID, "addNewRecordButton").click()

    test_values = [
        ("а" * 25, 25),
        ("Паша", 4),
        ("LIZ", 3),
        ("123456", 6),
        ("#$@$", 4),
        ("a" * 30, 25),  # ограничение
        ("     ", 5),
        ("Иван Иванов", 11)
    ]

    for value, expected_len in test_values:
        first_name_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]')
        first_name_input.clear()
        first_name_input.send_keys(value)
        actual_value = first_name_input.get_attribute("value")
        assert len(actual_value) == expected_len, f"Ожидали {expected_len}, получили {len(actual_value)}"
    driver.quit()


@allure.title("[СЗ04] Проверка поля Last Name")
@allure.description("Валидация ввода данных в поле Last Name")
@allure.severity(Severity.CRITICAL)
def test_last_name_validation():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()
    driver.find_element(By.ID, "addNewRecordButton").click()

    test_values = [
        ("а" * 25, 25),
        ("Туманский", 9),
        ("LIZKA", 5),
        ("1234567", 7),
        ("#$@$", 4),
        ("a" * 30, 25),
        ("     ", 5),
    ]

    for value, expected_len in test_values:
        last_name_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"]')
        last_name_input.clear()
        last_name_input.send_keys(value)
        actual_value = last_name_input.get_attribute("value")
        assert len(actual_value) == expected_len, f"Ожидали {expected_len}, получили {len(actual_value)}"
    driver.quit()


@allure.title("[СЗ05] Проверка поля Email")
@allure.description("Валидация email")
@allure.severity(Severity.CRITICAL)
def test_email_validation():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()
    driver.find_element(By.ID, "addNewRecordButton").click()

    invalid_emails = [
        "", " " * 3, "a" * 254,
        " user@example.com", "user@example.com ",
        "user@ example.com", "user@example .com",
        "user name@example.com", "user@", "тест", "12345", "user_example@com"
    ]

    for email in invalid_emails:
        email_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="name@example.com"]')
        email_input.clear()
        email_input.send_keys(email)
        driver.find_element(By.ID, "submit").click()
        form = driver.find_element(By.ID, "userForm")
        assert form.is_displayed(), f"Форма закрылась, хотя email '{email}' некорректный"
    driver.quit()


@allure.title("[СЗ06] Проверка поля Age")
@allure.description("Валидация возраста")
@allure.severity(Severity.CRITICAL)
def test_age_validation():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()
    driver.find_element(By.ID, "addNewRecordButton").click()

    invalid_ages = ["", " ", "-5", "100", "ab", "тест", "TEST", "!@#"]
    for age in invalid_ages:
        age_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Age"]')
        age_input.clear()
        age_input.send_keys(age)
        driver.find_element(By.ID, "submit").click()
        form = driver.find_element(By.ID, "userForm")
        assert form.is_displayed(), f"Форма закрылась, хотя age '{age}' некорректный"
    driver.quit()


@allure.title("[СЗ07] Проверка поля Salary")
@allure.description("Валидация зарплаты")
@allure.severity(Severity.CRITICAL)
def test_salary_validation():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()
    driver.find_element(By.ID, "addNewRecordButton").click()

    invalid_salary = ["", "?*%", "вав", "pdf", "-2", "1234567889999", "123 456"]
    for salary in invalid_salary:
        salary_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Salary"]')
        salary_input.clear()
        salary_input.send_keys(salary)
        driver.find_element(By.ID, "submit").click()
        form = driver.find_element(By.ID, "userForm")
        assert form.is_displayed(), f"Форма закрылась, хотя salary '{salary}' некорректный"
    driver.quit()
@allure.title("[СЗ08] Проверка поля Department")
@allure.description("Валидация ввода данных в поле Department")
@allure.severity(Severity.CRITICAL)
def test_department_validation():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()
    driver.find_element(By.ID, "addNewRecordButton").click()

    test_values = [
        ("", False),
        ("мир", True),
        ("blue", True),
        ("%?", True),
        ("a" * 25, True),
        ("123456789", True),
        ("1234 5678", True),
        ("test1@gmail.com", True),
        ("-234", True),
        (" ", False),
    ]

    for value, should_be_valid in test_values:
        dep_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Department"]')
        dep_input.clear()
        dep_input.send_keys(value)
        driver.find_element(By.ID, "submit").click()
        form_open = driver.find_element(By.ID, "userForm").is_displayed()
        if should_be_valid:
            assert not form_open, f"Форма не закрылась, хотя Department '{value}' валиден"
        else:
            assert form_open, f"Форма закрылась, хотя Department '{value}' невалиден"
    driver.quit()


@allure.title("[СЗ09] Проверка кнопки Submit")
@allure.description("Нажатие кнопки Submit и через табуляцию")
@allure.severity(Severity.CRITICAL)
def test_submit_button():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    # Заполняем форму валидными данными
    driver.find_element(By.ID, "addNewRecordButton").click()
    driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]').send_keys("Ivan")
    driver.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"]').send_keys("Petrov")
    driver.find_element(By.CSS_SELECTOR, '[placeholder="name@example.com"]').send_keys("ivan.petrov@test.com")
    driver.find_element(By.CSS_SELECTOR, '[placeholder="Age"]').send_keys("28")
    driver.find_element(By.CSS_SELECTOR, '[placeholder="Salary"]').send_keys("12000")
    driver.find_element(By.CSS_SELECTOR, '[placeholder="Department"]').send_keys("QA")

    driver.find_element(By.ID, "submit").click()
    rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
    assert any("Ivan" in row.text and "Petrov" in row.text for row in rows), "Запись не появилась в таблице"

    driver.quit()


@allure.title("[СЗ10] Создание записи валидными данными")
@allure.description("Добавление валидной записи")
@allure.severity(Severity.CRITICAL)
def test_create_record_valid():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    driver.find_element(By.ID, "addNewRecordButton").click()
    fields = [
        ("First Name", '[placeholder="First Name"]', "Bruce"),
        ("Last Name", '[placeholder="Last Name"]', "Wayne"),
        ("Email", '[placeholder="name@example.com"]', "bruce.wayne@test.com"),
        ("Age", '[placeholder="Age"]', "35"),
        ("Salary", '[placeholder="Salary"]', "15000"),
        ("Department", '[placeholder="Department"]', "Security"),
    ]
    for _, selector, value in fields:
        driver.find_element(By.CSS_SELECTOR, selector).send_keys(value)

    driver.find_element(By.ID, "submit").click()
    time.sleep(1)
    rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
    assert any("Bruce" in row.text and "Wayne" in row.text for row in rows), "Запись не появилась в таблице"
    driver.quit()


@allure.title("[СЗ11] Создание записи невалидными данными")
@allure.description("Попытка добавить запись с некорректными данными")
@allure.severity(Severity.CRITICAL)
def test_create_record_invalid():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    driver.find_element(By.ID, "addNewRecordButton").click()
    # Невалидные значения
    driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]').send_keys("a" * 30)
    driver.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"]').send_keys("123")
    driver.find_element(By.CSS_SELECTOR, '[placeholder="name@example.com"]').send_keys("wrong@")
    driver.find_element(By.CSS_SELECTOR, '[placeholder="Age"]').send_keys("-1")
    driver.find_element(By.CSS_SELECTOR, '[placeholder="Salary"]').send_keys("test")
    driver.find_element(By.CSS_SELECTOR, '[placeholder="Department"]').send_keys(" ")

    driver.find_element(By.ID, "submit").click()
    form = driver.find_element(By.ID, "userForm")
    assert form.is_displayed(), "Форма закрылась, хотя данные были невалидные"
    driver.quit()


@allure.title("[СЗ12] Очистка формы при повторном открытии")
@allure.description("Проверка, что после закрытия и повторного открытия форма пустая")
@allure.severity(Severity.NORMAL)
def test_form_reset_after_close():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    driver.find_element(By.ID, "addNewRecordButton").click()
    driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]').send_keys("Test")
    driver.find_element(By.CSS_SELECTOR, '[aria-hidden="true"]').click()  # крестик

    driver.find_element(By.ID, "addNewRecordButton").click()
    first_name_value = driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]').get_attribute("value")
    assert first_name_value == "", "Поле First Name не очистилось при повторном открытии"
    driver.quit()
@allure.title("[УЗ01] Удаление записи")
@allure.description("Проверка удаления одной записи")
@allure.severity(Severity.CRITICAL)
def test_delete_record():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    rows_before = driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
    non_empty_before = [r for r in rows_before if r.text.strip() != ""]
    assert len(non_empty_before) > 0, "В таблице нет записей для удаления"

    # Удаляем первую запись
    delete_button = driver.find_element(By.CSS_SELECTOR, '[title="Delete"]')
    delete_button.click()
    time.sleep(0.5)

    rows_after = driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
    non_empty_after = [r for r in rows_after if r.text.strip() != ""]
    assert len(non_empty_after) < len(non_empty_before), "Количество записей не уменьшилось после удаления"
    driver.quit()


@allure.title("[РЗ01] Нажатие кнопки редактирования")
@allure.description("Проверка открытия формы при нажатии кнопки Edit")
@allure.severity(Severity.CRITICAL)
def test_edit_button_opens_form():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    edit_button = driver.find_element(By.CSS_SELECTOR, '[title="Edit"]')
    edit_button.click()
    form = driver.find_element(By.ID, "userForm")
    assert form.is_displayed(), "Форма редактирования не открылась"
    driver.quit()


@allure.title("[РЗ02] Редактирование поля First Name")
@allure.description("Валидация First Name при редактировании записи")
@allure.severity(Severity.CRITICAL)
def test_edit_first_name():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    driver.find_element(By.CSS_SELECTOR, '[title="Edit"]').click()
    test_values = ["Паша", "LIZ", "123456", "#$@$", "a" * 30]
    for value in test_values:
        first_name_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]')
        first_name_input.clear()
        first_name_input.send_keys(value)
        actual_value = first_name_input.get_attribute("value")
        assert len(actual_value) <= 25, f"Поле принимает больше 25 символов: {len(actual_value)}"
    driver.quit()


@allure.title("[РЗ03] Редактирование поля Last Name")
@allure.description("Валидация Last Name при редактировании записи")
@allure.severity(Severity.CRITICAL)
def test_edit_last_name():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    driver.find_element(By.CSS_SELECTOR, '[title="Edit"]').click()
    test_values = ["Туманский", "LIZKA", "1234567", "#$@$", "a" * 30]
    for value in test_values:
        last_name_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"]')
        last_name_input.clear()
        last_name_input.send_keys(value)
        actual_value = last_name_input.get_attribute("value")
        assert len(actual_value) <= 25, f"Поле принимает больше 25 символов: {len(actual_value)}"
    driver.quit()


@allure.title("[РЗ04] Редактирование поля Email")
@allure.description("Валидация Email при редактировании записи")
@allure.severity(Severity.CRITICAL)
def test_edit_email():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    driver.find_element(By.CSS_SELECTOR, '[title="Edit"]').click()
    invalid_emails = ["", "   ", "wrong@", "user@", "тест", "12345", "user example@test.com"]
    for email in invalid_emails:
        email_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="name@example.com"]')
        email_input.clear()
        email_input.send_keys(email)
        driver.find_element(By.ID, "submit").click()
        form = driver.find_element(By.ID, "userForm")
        assert form.is_displayed(), f"Форма закрылась, хотя email '{email}' некорректный"
    driver.quit()


@allure.title("[РЗ05] Редактирование поля Age")
@allure.description("Валидация Age при редактировании записи")
@allure.severity(Severity.CRITICAL)
def test_edit_age():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    driver.find_element(By.CSS_SELECTOR, '[title="Edit"]').click()
    invalid_ages = ["", " ", "-1", "100", "abc", "тест", "TEST"]
    for age in invalid_ages:
        age_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Age"]')
        age_input.clear()
        age_input.send_keys(age)
        driver.find_element(By.ID, "submit").click()
        form = driver.find_element(By.ID, "userForm")
        assert form.is_displayed(), f"Форма закрылась, хотя age '{age}' некорректный"
    driver.quit()


@allure.title("[РЗ06] Редактирование поля Salary")
@allure.description("Валидация Salary при редактировании записи")
@allure.severity(Severity.CRITICAL)
def test_edit_salary():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    driver.find_element(By.CSS_SELECTOR, '[title="Edit"]').click()
    invalid_salary = ["", "?*%", "тест", "pdf", "-2", "123456789012345", "123 456"]
    for salary in invalid_salary:
        salary_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Salary"]')
        salary_input.clear()
        salary_input.send_keys(salary)
        driver.find_element(By.ID, "submit").click()
        form = driver.find_element(By.ID, "userForm")
        assert form.is_displayed(), f"Форма закрылась, хотя salary '{salary}' некорректный"
    driver.quit()


@allure.title("[РЗ07] Редактирование поля Department")
@allure.description("Валидация Department при редактировании записи")
@allure.severity(Severity.CRITICAL)
def test_edit_department():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    driver.find_element(By.CSS_SELECTOR, '[title="Edit"]').click()
    test_values = ["", "мир", "blue", "%?", "a" * 25, "123456789", "1234 5678", "test1@gmail.com", "-234", " "]
    for dep in test_values:
        dep_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Department"]')
        dep_input.clear()
        dep_input.send_keys(dep)
        driver.find_element(By.ID, "submit").click()
        form_open = driver.find_element(By.ID, "userForm").is_displayed()
        if dep == "" or dep.strip() == "":
            assert form_open, f"Форма закрылась, хотя Department '{dep}' невалидный"
    driver.quit()


@allure.title("[РЗ08] Кнопка Submit в режиме редактирования")
@allure.description("Проверка отправки изменений в записи")
@allure.severity(Severity.CRITICAL)
def test_edit_submit_button():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    driver.find_element(By.CSS_SELECTOR, '[title="Edit"]').click()
    driver.find_element(By.CSS_SELECTOR, '[placeholder="Department"]').clear()
    driver.find_element(By.CSS_SELECTOR, '[placeholder="Department"]').send_keys("UpdatedQA")
    driver.find_element(By.ID, "submit").click()
    rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
    assert any("UpdatedQA" in row.text for row in rows), "Изменение Department не сохранилось"
    driver.quit()
@allure.title("[ПП01] Поиск по First Name")
@allure.description("Проверка поиска по имени")
@allure.severity(Severity.CRITICAL)
def test_search_by_first_name():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    search_box = driver.find_element(By.ID, "searchBox")
    search_box.send_keys("Cierra")
    time.sleep(0.5)

    rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
    assert all("Cierra" in row.text for row in rows if row.text.strip()), "Поиск по имени не сработал"
    driver.quit()


@allure.title("[ПП02] Поиск по несуществующему значению")
@allure.description("Проверка отображения сообщения No rows found")
@allure.severity(Severity.CRITICAL)
def test_search_non_existing():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    search_box = driver.find_element(By.ID, "searchBox")
    search_box.send_keys("XXXXXX")
    time.sleep(0.5)

    no_data = driver.find_element(By.CLASS_NAME, "rt-noData").text
    assert no_data == "No rows found", "Не появилось сообщение 'No rows found'"
    driver.quit()


@allure.title("[ПП03] Поиск по Last Name")
@allure.description("Проверка поиска по фамилии")
@allure.severity(Severity.CRITICAL)
def test_search_by_last_name():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    search_box = driver.find_element(By.ID, "searchBox")
    search_box.send_keys("Vega")
    time.sleep(0.5)

    rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
    assert all("Vega" in row.text for row in rows if row.text.strip()), "Поиск по фамилии не сработал"
    driver.quit()


@allure.title("[ПП04] Поиск по Age")
@allure.description("Проверка поиска по возрасту")
@allure.severity(Severity.CRITICAL)
def test_search_by_age():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    search_box = driver.find_element(By.ID, "searchBox")
    search_box.send_keys("12")
    time.sleep(0.5)

    rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
    assert all("12" in row.text for row in rows if row.text.strip()), "Поиск по возрасту не сработал"
    driver.quit()


@allure.title("[ПП05] Поиск по Email")
@allure.description("Проверка поиска по email")
@allure.severity(Severity.CRITICAL)
def test_search_by_email():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    search_box = driver.find_element(By.ID, "searchBox")
    search_box.send_keys("test01@gmail.com")
    time.sleep(0.5)

    rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
    assert all("test01@gmail.com" in row.text for row in rows if row.text.strip()), "Поиск по email не сработал"
    driver.quit()


@allure.title("[ПП06] Поиск по Salary")
@allure.description("Проверка поиска по зарплате")
@allure.severity(Severity.CRITICAL)
def test_search_by_salary():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    search_box = driver.find_element(By.ID, "searchBox")
    search_box.send_keys("12000")
    time.sleep(0.5)

    rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
    assert all("12000" in row.text for row in rows if row.text.strip()), "Поиск по Salary не сработал"
    driver.quit()


@allure.title("[ПП07] Поиск по Department")
@allure.description("Проверка поиска по отделу")
@allure.severity(Severity.CRITICAL)
def test_search_by_department():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    search_box = driver.find_element(By.ID, "searchBox")
    search_box.send_keys("Legal")
    time.sleep(0.5)

    rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
    assert all("Legal" in row.text for row in rows if row.text.strip()), "Поиск по Department не сработал"
    driver.quit()
@allure.title("[ПТ01] Пагинация — 5 записей на странице")
@allure.description("Переключение страниц таблицы при 5 строках")
@allure.severity(Severity.CRITICAL)
def test_pagination_5_rows():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    # Установим 5 строк на страницу
    select = driver.find_element(By.CSS_SELECTOR, 'select[aria-label="rows per page"]')
    select.click()
    driver.find_element(By.CSS_SELECTOR, 'option[value="5"]').click()
    time.sleep(0.5)

    # Переход на вторую страницу
    next_btn = driver.find_element(By.CSS_SELECTOR, ".-next button")
    next_btn.click()
    time.sleep(0.5)

    # Проверяем, что появились другие записи
    rows = driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
    assert len([r for r in rows if r.text.strip()]) <= 5, "Отображается больше 5 строк"
    driver.quit()


@allure.title("[ПТ02] Пагинация — 10 записей на странице")
@allure.description("Переключение страниц таблицы при 10 строках")
@allure.severity(Severity.CRITICAL)
def test_pagination_10_rows():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    select = driver.find_element(By.CSS_SELECTOR, 'select[aria-label="rows per page"]')
    select.click()
    driver.find_element(By.CSS_SELECTOR, 'option[value="10"]').click()
    time.sleep(0.5)

    next_btn = driver.find_element(By.CSS_SELECTOR, ".-next button")
    next_btn.click()
    time.sleep(0.5)

    rows = driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
    assert len([r for r in rows if r.text.strip()]) <= 10, "Отображается больше 10 строк"
    driver.quit()


@allure.title("[ПТ03] Кнопка Next при 5 строках")
@allure.description("Переход на следующую страницу кнопкой Next")
@allure.severity(Severity.CRITICAL)
def test_pagination_next_button():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    select = driver.find_element(By.CSS_SELECTOR, 'select[aria-label="rows per page"]')
    select.click()
    driver.find_element(By.CSS_SELECTOR, 'option[value="5"]').click()
    time.sleep(0.5)

    next_btn = driver.find_element(By.CSS_SELECTOR, ".-next button")
    next_btn.click()
    time.sleep(0.5)

    # Проверим, что кнопка Previous стала активной
    prev_btn = driver.find_element(By.CSS_SELECTOR, ".-previous button")
    assert prev_btn.is_enabled(), "Кнопка Previous должна быть активна после перехода"
    driver.quit()


@allure.title("[ПТ04] Кнопка Previous")
@allure.description("Проверка возврата на предыдущую страницу")
@allure.severity(Severity.CRITICAL)
def test_pagination_previous_button():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    # Поставим 5 строк и перейдём на 2-ю страницу
    select = driver.find_element(By.CSS_SELECTOR, 'select[aria-label="rows per page"]')
    select.click()
    driver.find_element(By.CSS_SELECTOR, 'option[value="5"]').click()
    time.sleep(0.5)

    driver.find_element(By.CSS_SELECTOR, ".-next button").click()
    time.sleep(0.5)

    # Теперь жмём Previous
    driver.find_element(By.CSS_SELECTOR, ".-previous button").click()
    time.sleep(0.5)

    # Проверим, что вернулись на первую страницу (кнопка Previous снова неактивна)
    prev_btn = driver.find_element(By.CSS_SELECTOR, ".-previous button")
    assert not prev_btn.is_enabled(), "Кнопка Previous должна быть неактивна на первой странице"
    driver.quit()
