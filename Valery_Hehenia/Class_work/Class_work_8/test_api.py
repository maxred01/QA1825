import requests
import pytest



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


