import requests
import pytest



def test_main_pame():
    url = "https://you.regettingold.com/"

    response = requests.request("GET", url)
    assert response.status_code == 200 , f'Статус код не равен 200, а {response.status_code}'


def test_autorization():
    import requests

    url = "https://you.regettingold.com/?dd=22&mm=05&yy=1996&submitButton1=&name="

    payload = {}

    response = requests.request("GET", url)
    print(response.text)

    assert response.status_code == 200, f'Статус код не равен 200, а {response.status_code}'


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


