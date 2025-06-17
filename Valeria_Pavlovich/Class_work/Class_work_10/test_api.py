import requests
import pytest

def test_main_page():
    urls = [
        ('https://belavia.by/', 'Belavia main page'),
        ('https://belavia.by/account/', 'Belavia account'),
        ('https://belavia.by/booking/', 'Belavia booking'),]
    for url_link, url_name in urls:
        response = requests.request("GET", url_link)
        assert response.status_code == 200, f'Status code of {url_name} is not 200, but {response.status_code}'

#     url = 'https://belavia.by'
#     response = requests.request ("GET", url)
#     assert response.status_code == 200, f'Status code is equal not 200, but {response.status_code}'
#
# def test_account():
#     url = 'https://belavia.by/account/'
#     response = requests.request("GET", url)
#     assert response.status_code == 200, f'Status code is equal not 200, but {response.status_code}'
#
# def test_booking():
#     url = 'https://belavia.by/booking/'
#     response = requests.request("GET", url)
#     assert response.status_code == 200, f'Status code is equal not 200, but {response.status_code}'

