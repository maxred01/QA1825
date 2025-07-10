import requests
import pytest
from pip._internal.cli.cmdoptions import json


def test_main_pame():
    url = "https://you.regettingold.com/"

    response = requests.request("GET", url)
    assert response.status_code == 200 , f'Статус код не равен 200, а {response.status_code}'




def test_autorization():

    day = "22"
    month = "05"
    year = "1996"

    url = f"https://you.regettingold.com/{day}/{month}/{year}/"

    response = requests.request("GET", url)

    assert response.status_code == 200, f'Статус код не равен 200, а {response.status_code}'
    assert "You're getting old!" in response.text, f'Такой фразы не существует!'


def test_main_page():
  urls = [
    ("https://you.regettingold.com/", 'главной you.regettingold'),
      ("https://you.regettingold.com/celebcombos.php", 'Celeb Combos'),
      ("https://you.regettingold.com/press.php", 'Press Information'),
      ("https://you.regettingold.com/ad.php", 'Advertising Information'),
      ("https://you.regettingold.com/privacy.php", 'Privacy'),

  ]
  for url_link, url_name in urls:
    response = requests.request("GET", url_link)
    assert response.status_code == 200, f'Статус код страницы "{url_name}" равен не 200 а {response.status_code}'


def test_edostavka_post():


    url = "https://api2.edostavka.by/api/v2/search/preview/?query=%D0%A1%D0%BE%D1%81%D0%B8%D1%81%D0%BA%D0%B8%20%D1%82%D1%80%D0%BE%D0%B8%D1%86%D0%BA%D0%B8%D0%B5"

    payload = json.dumps({})
    headers = {
        'accept': 'application/json',
        'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
        'apitoken': 'OrTX6q0IK2X71t9gbFhISVe27KqrwNee',
        'content-type': 'application/json',
        'origin': 'https://edostavka.by',
        'priority': 'u=1, i',
        'referer': 'https://edostavka.by/',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'web-user-agent': 'SiteEdostavka/1.0.0'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

