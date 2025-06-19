import requests
# import pytest
#
# def test_main_page():
#
#     urls = [
#         ("https://knigogid.ru/", 'главной'),
#         ("https://knigogid.ru/genres" ,'жанры'),
#         ("https://knigogid.ru/books", 'книги'),
#         ("https://knigogid.ru/reviews", 'рецензии'),
#         ("https://knigogid.ru/register", 'регистрация'),
#
#          ]
#     for url_link, url_name in urls:
#
#         response = requests.request("GET", url_link)
#         assert  response.status_code == 200, f'Статус код страницы "{url_name}" равен не 200 а {response.status_code}'
#
#
# def test_register_page():
#     url = "https://knigogid.ru/register"
#
#
#     response = requests.request("POST", url)
#     assert response.status_code == 201, f'Статус код страницы "{url}" равен не 201 а {response.status_code}'






import requests

def test_api():

    url = "https://knigogid.ru/login"

    payload = '_token=XjBav5FjZZ7AFPXAmphff6DOu9CBnfzImTRWvluF&email=nata%40yandex12.ru&password=3x9-EFf-Z75-Fpr'

    response = requests.request("POST", url, data=payload)

    assert response.status_code == 300, f'Статус код страницы "{url}" равен не 300 а {response.status_code}'
