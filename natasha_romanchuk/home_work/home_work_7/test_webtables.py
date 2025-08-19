import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_check as check

@allure.title("Тест Web Tables")
@allure.description("Проверка добавления новой записи")
@allure.tag("Regression")
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Elements")
@allure.story("Web Tables")
def test_web_tables():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    with allure.step("Добавляем новую запись"):
        driver.find_element(By.ID, "addNewRecordButton").click()
        driver.find_element(By.ID, "firstName").send_keys("Nata")
        driver.find_element(By.ID, "lastName").send_keys("QA")
        driver.find_element(By.ID, "userEmail").send_keys("nata@test.com")
        driver.find_element(By.ID, "age").send_keys("25")
        driver.find_element(By.ID, "salary").send_keys("1000")
        driver.find_element(By.ID, "department").send_keys("IT")
        driver.find_element(By.ID, "submit").click()


    with allure.step("Проверяем таблицу"):
        table = driver.find_element(By.CLASS_NAME, "rt-table").text
        print(table)
        time.sleep(5)
        check.is_in("Nata", table)

    driver.quit()
@allure.title("Проверка редактирования записи в Web Tables")
@allure.severity(allure.severity_level.CRITICAL)
def test_edit_record():
    with allure.step("Открыть браузер и страницу Web Tables"):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/webtables")
        driver.maximize_window()

    with allure.step("Редактируем запись"):
        driver.find_element(By.ID, "edit-record-2").click()
        first_name_field = driver.find_element(By.ID, "firstName")
        first_name_field.clear()
        first_name_field.send_keys("Natasha")
        driver.find_element(By.ID, "submit").click()

    with allure.step("Проверяем, что имя изменилось"):
        table_text = driver.find_element(By.CLASS_NAME, "rt-table").text
        check.is_true("Natasha" in table_text, "Имя должно быть Natasha")

    driver.quit()

@allure.title("Проверка удаления записи в Web Tables")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_record():
    with allure.step("Открыть браузер и страницу Web Tables"):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/webtables")
        driver.maximize_window()

    with allure.step("Удаляем первую запись"):
        time.sleep(3)
        driver.find_element(By.ID, "delete-record-1").click()


    with allure.step("Проверяем, что запись удалена"):
        table_text = driver.find_element(By.CLASS_NAME, "rt-table").text
        check.is_false("Cierra" in table_text, "Запись Cierra должна быть удалена")

    driver.quit()

@allure.title("Проверка поиска записи в Web Tables")
@allure.severity(allure.severity_level.NORMAL)
def test_search_record():
    with allure.step("Открыть браузер и страницу Web Tables"):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/webtables")
        driver.maximize_window()

    with allure.step("Вводим фамилию в поиск"):
        search_box = driver.find_element(By.ID, "searchBox")
        search_box.send_keys("Vega")
        time.sleep(1)

    with allure.step("Проверяем, что найдена запись Vega"):
        table_text = driver.find_element(By.CLASS_NAME, "rt-table").text
        check.is_true("Vega" in table_text, "Запись Vega должна быть найдена")

    driver.quit()

@allure.title("Проверка пагинации в Web Tables")
@allure.severity(allure.severity_level.MINOR)
def test_pagination():
    with allure.step("Открыть браузер и страницу Web Tables"):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/webtables")
        driver.maximize_window()

    with allure.step("Меняем количество строк на странице"):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        rows_dropdown = driver.find_element(By.CLASS_NAME, "select-wrap")
        rows_dropdown.click()
        driver.find_element(By.XPATH, "//option[@value='10']").click()
        time.sleep(5)

    with allure.step("Проверяем, что количество строк изменилось"):
        rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
        check.greater_equal(len(rows), 4, "Должно быть больше строк на странице")

    driver.quit()




