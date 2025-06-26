import requests
import pytest

def test_main_page():
    url= "https://av.by/"
    response = requests.requests("GET", url)
    assert response.status_code == 200, f'Статус код страницы равен не 200 а {response.status_code}'

