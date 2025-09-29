import pytest
import pytest_check as check
import allure
from Valery_Hehenia.Class_work.Class_work_18.data.api_client import APIClient
from allure_commons.types import LabelType
BASE_URL = "https://api.demoblaze.com"



@pytest.fixture(scope="session")
def client():
    return APIClient(BASE_URL)


@allure.feature("API тесты")
@allure.story("Получение списка товаров")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/1EnRI1sA/51-api-01%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B0-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%BE%D0%B2",
                 "API-01"
)
def test_get_entries(client):
    status, response = client.get("/entries")
    print("\nСтатус:", status)
    print("Ответ API /entries:", response)

    check.equal(status, 200, "Статус не 200")
    check.is_true("Items" in response, "В ответе нет ключа 'Items'")
    check.greater(len(response["Items"]), 0, "Список товаров пустой")

@allure.feature("API тесты")
@allure.story("Проверка структуры товара")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/j4knzEDZ/52-api-02-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D1%8B-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0",
                 "API-02"
)
def test_entries_structure(client):
    status, response = client.get("/entries")
    first_item = response["Items"][0]

    check.equal(status, 200, "Статус не 200")
    check.is_true("id" in first_item, "Нет id у товара")
    check.is_true("title" in first_item, "Нет title у товара")
    check.is_true("price" in first_item, "Нет price у товара")
    check.is_true("img" in first_item, "Нет img у товара")  # вместо description

@allure.feature("API тесты")
@allure.story("Получение конкретного товара")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/PW1KRxwt/53-api-03-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BA%D0%BE%D0%BD%D0%BA%D1%80%D0%B5%D1%82%D0%BD%D0%BE%D0%B3%D0%BE-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0",
                 "API-03"
)
def test_view_product(client):
    data = {"id": "1"}
    status, response = client.post("/view", json=data)
    print("\nСтатус:", status)
    print("Ответ API /view:", response)

    check.equal(status, 200, "Статус не 200")
    check.is_true("title" in response, "Нет поля title у товара")
    check.equal(response["id"], 1, "ID товара не совпадает")
    check.is_true("price" in response, "Нет поля price у товара")

@allure.feature("API тесты")
@allure.story("Регистрация существующего пользователя")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/z9GVoy5N/54-api-04-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D1%83%D1%8E%D1%89%D0%B5%D0%B3%D0%BE-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F",
                 "API-04"
)
def test_signup_existing_user(client):
    data = {"username": "test_user123", "password": "123456"}
    status, response = client.post("/signup", json=data)
    print("\nСтатус:", status)
    print("Ответ API /signup:", response)

    check.equal(status, 200, "Статус не 200")
    check.is_true("errorMessage" in response, "Нет сообщения об ошибке")
    check.equal(response["errorMessage"], "This user already exist.", "Некорректное сообщение")

@allure.feature("API тесты")
@allure.story("Логин с неверным паролем")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/UjhnjNPX/55-api-05-%D0%BB%D0%BE%D0%B3%D0%B8%D0%BD-%D1%81-%D0%BD%D0%B5%D0%B2%D0%B5%D1%80%D0%BD%D1%8B%D0%BC-%D0%BF%D0%B0%D1%80%D0%BE%D0%BB%D0%B5%D0%BC",
                 "API-05"
)
def test_login_wrong_password(client):
    data = {"username": "test_user123", "password": "wrong_pass"}
    status, response = client.post("/login", json=data)
    print("\nСтатус:", status)
    print("Ответ API /login:", response)

    check.equal(status, 200, "Статус не 200")
    check.is_true("errorMessage" in response, "Нет сообщения об ошибке")
    check.equal(response["errorMessage"], "Wrong password.", "Некорректное сообщение")

@allure.feature("API тесты")
@allure.story("Логин с пустыми полями")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/FimPVebi/56-api-06-%D0%BB%D0%BE%D0%B3%D0%B8%D0%BD-%D1%81-%D0%BF%D1%83%D1%81%D1%82%D1%8B%D0%BC%D0%B8-%D0%BF%D0%BE%D0%BB%D1%8F%D0%BC%D0%B8",
                 "API-06"
)
def test_login_empty_fields(client):
    data = {"username": "", "password": ""}
    status, response = client.post("/login", json=data)
    print("\nСтатус:", status)
    print("Ответ API /login (empty fields):", response)

    check.is_false(status == 200, "Сервер вернул 200 на пустые поля")


@allure.feature("API тесты")
@allure.story("Добавление товара в корзину без cookie")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/WttqrP3d/57-api-07-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0-%D0%B2-%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D1%83-%D0%B1%D0%B5%D0%B7-cookie",
                 "API-07"
)
def test_add_to_cart_without_cookie(client):
    data = {"id": "test-uuid", "cookie": "", "prod_id": 1, "flag": True}
    status, response = client.post("/addtocart", json=data)
    print("\nСтатус:", status)
    print("Ответ API /addtocart:", response)

    check.is_false(status == 200, "Сервер вернул 200 при добавлении без cookie")


@allure.feature("API тесты")
@allure.story("Удаление несуществующего товара")
@allure.label(LabelType.LANGUAGE, "python")
@allure.testcase(
    "https://trello.com/c/fOUTuO2p/50-api-07-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0-%D0%B2-%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D1%83-%D0%B1%D0%B5%D0%B7-cookie",
                 "API-08"
)
def test_delete_item_invalid_id(client):
    data = {"id": "fake-id-12345"}
    status, response = client.post("/deleteitem", json=data)
    print("\nСтатус:", status)
    print("Ответ API /deleteitem:", response)

    check.equal(status, 200, "Статус не 200")
    check.is_true("errorMessage" in response or response == {}, "Неожиданный ответ при удалении несуществующего товара")
