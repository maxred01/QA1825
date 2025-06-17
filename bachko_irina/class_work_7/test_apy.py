import requests
import pytest

def test_main_page():
    urls = [
        ("https://www.spacex.com/vehicles/falcon-9/", "главная страница spacex"),
        ("https://www.spacex.com/vehicles/falcon-heavy/", "spacex_falcon-heavy"),
        ("https://shop.spacex.com/cart", "spacex cart"),
        ("https://www.spacex.com/supplier/", "supplier"),
        ("https://shop.spacex.com/collections/all", "shop spacex" )
    ]
    for url_link, url_name in urls:
        response = requests.request("GET", url_link)
        assert response.status_code == 200, f'статус код страницы "{url_name}" равен не 200 а {response.status_code}'




