import requests
import  pytest

def test_main_page():
    urls = [
        ("https://www.hoyolab.com/", 'главная'),
        ("https://www.hoyolab.com/circles/6/42/feed?page_type=42&page_sort=hot", 'hsr'),
        ("https://www.hoyolab.com/circles/8/46/feed?page_type=46&page_sort=hot", 'zzz'),
        ("https://www.hoyolab.com/search?keyword=%D0%B3%D0%B5%D1%80%D1%82%D0%B0", 'poisk'),
        ("https://www.hoyolab.com/home/events", 'ивенты'),
           ]
    for url_link, url_name in urls:
        response = requests.request("GET", urls)
        assert response.status_code == 200, f'error {response.status_code}'
def test_registration():
    url = "https://www.hoyolab.com/circles/2/30/feed?page_type=30&page_sort=hot"
    response = requests.request("Post", url)
    assert response.status_code == 200, f'error {response.status_code}'


def test_api():
    return None