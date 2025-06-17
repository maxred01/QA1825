import requests
import pytest
import json

def test_main_page():
    url = "https://rocketdata.ru/"
    response = requests.request("GET", url)
    assert response.status_code == 200

def test_login_page():
    url = "https://go.rocketdata.io/auth/login"
    response = requests.request("GET", url)
    assert response.status_code == 200

def test_partners_page():
    url = "https://rocketdata.ru/partners"
    response = requests.request("GET", url)
    assert response.status_code == 200

def test_about_page():
    url = "https://rocketdata.ru/about"
    response = requests.request("GET", url)
    assert response.status_code == 200

def test_vacancies_page():
    url = "https://rocketdata.ru/vacancies"
    response = requests.request("GET", url)
    assert response.status_code == 200

def test_register_page():
    url = "https://go.rocketdata.io/auth/register"
    response = requests.request("GET", url)
    assert response.status_code == 200


def test_login_user():
    url = "https://go.rocketdata.io/op/api/user/login/"
    payload = json.dumps({
        "email": "1@gmail.com",
        "password": "Rhghrihehgf11",
        "remember_me": False })
    response = requests.request("POST", url)
    assert response.status_code != 200

