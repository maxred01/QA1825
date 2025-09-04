import requests
import pytest
import json

def test_get():
    urls_get = [
        ('https://belavia.by/', 'Belavia main page'),
        ('https://belavia.by/#ibe', 'Belavia Buy'),
        ('https://belavia.by/#wci', 'Belavia Check-in'),
        ('https://belavia.by/#trip-case', 'Belavia Status'),
        ('https://belavia.by/#transfer', 'Belavia Transfer'),
        ('https://belavia.by/#hotel', 'Belavia Hotel'),
        ('https://belavia.by/account/', 'Belavia account'),
        ('https://belavia.by/booking/', 'Belavia booking'),]
    for url_link, url_name in urls_get:
        response = requests.request("GET", url_link)
        assert response.status_code == 200, f'Status code of {url_name} is not 200, but {response.status_code}'

def test_post():
    url = "https://webapi.belavia.by/graphql/query/nemo"

    payload = "{\"query\":\"mutation RunSearch($params: AviaSearchParameters!) {\\n  RunGeneralSearch(parameters: $params) {\\n    id\\n    __typename\\n  }\\n}\\n\",\"variables\":{\"params\":{\"segments\":[{\"arrival\":{\"iata\":\"MOW\"},\"departure\":{\"iata\":\"MSQ\"},\"data\":\"2025-07-11\"}],\"passengers\":[{\"passengerType\":\"ADT\",\"extendedPassengerType\":null,\"count\":1},{\"passengerType\":\"CLD\",\"extendedPassengerType\":null,\"count\":0},{\"passengerType\":\"INF\",\"extendedPassengerType\":null,\"count\":0}],\"ffpMode\":false,\"currency\":\"BYN\"}}}"
    headers = {
        'accept': '*/*',
        'accept-language': 'ru',
        'content-type': 'application/json',
        'origin': 'https://belavia.by',
        'priority': 'u=1, i',
        'referer': 'https://belavia.by/',
        'requestuid': '98943327438220',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'x-eventid': '44940776-c496-43da-90c2-a6bdae17ffc5',
        'Cookie': '__ddg9_=212.98.190.37; __ddg1_=1l7LeyrGLgpQXFNVZxyK; _ym_uid=1750787751184600749; _ym_d=1750787751; _ym_isad=2; _ym_visorc=b; __ddg10_=1750787822; __ddg8_=nLJIOsNxhEaQxpYv; __ddg10_=1750787970; __ddg8_=BMB3wvfpXpDPca8G; __ddg9_=54.86.50.139; user_unique_id=9713ae8ad36ef8fc8fb4b4de60b3df03; _8c201=f2c423ee5b208b67; hashed_value=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC93ZWJhcGkuYmVsYXZpYS5ieVwvZ3JhcGhxbFwvcXVlcnlcL25lbW8iLCJpYXQiOjE3NTA3ODc5NzAsImV4cCI6MTc1ODU2Mzk3MCwibmJmIjoxNzUwNzg3OTcwLCJqdGkiOiJDUElOZHVxeE1COU9pWmZzIiwic3ViIjo0ODI0LCJwcnYiOiJkZjhmOTg0YTA0ZTBiNzc3NzBiMGIzNmY2NDA5YWFlNWMzMmU4OTVhIiwibngxIjoibEp0V3htclo3UHRWZHJYY2pSTXVjSkpBNUhmbTNLZ2RTNDVrc29aQ21xM3VCTkF3bHVwTnhuZGhvaXozTnRVSDBCbm1Da0dmSXR1RnQxUDVpR2ZZdFU1OTlvaXo2QTdMS1lQTXBkR3o1RWdnc283cTNqZHVZUEdNVEJJcUhIaXYiLCJueDMiOltdLCJueDQiOmZhbHNlfQ.XujZm54Z9R2KcIW4pzXWwp2oXBsSwBqdXGaj-Kzj_sE; nemo_currency=RUB; nemo_lang=ru; session_id=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC93ZWJhcGkuYmVsYXZpYS5ieVwvZ3JhcGhxbFwvcXVlcnlcL25lbW8iLCJpYXQiOjE3NTA3ODc5NzAsImV4cCI6MTc1ODU2Mzk3MCwibmJmIjoxNzUwNzg3OTcwLCJqdGkiOiJDUElOZHVxeE1COU9pWmZzIiwic3ViIjo0ODI0LCJwcnYiOiJkZjhmOTg0YTA0ZTBiNzc3NzBiMGIzNmY2NDA5YWFlNWMzMmU4OTVhIiwibngxIjoibEp0V3htclo3UHRWZHJYY2pSTXVjSkpBNUhmbTNLZ2RTNDVrc29aQ21xM3VCTkF3bHVwTnhuZGhvaXozTnRVSDBCbm1Da0dmSXR1RnQxUDVpR2ZZdFU1OTlvaXo2QTdMS1lQTXBkR3o1RWdnc283cTNqZHVZUEdNVEJJcUhIaXYiLCJueDMiOltdLCJueDQiOmZhbHNlfQ.XujZm54Z9R2KcIW4pzXWwp2oXBsSwBqdXGaj-Kzj_sE'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

def test_post_tutu():
    url = "https://offers-api.tutu.ru/avia/offers"

    payload = json.dumps({
        "passengers": {
            "child": 0,
            "infant": 0,
            "full": 1
        },
        "serviceClass": "Y",
        "routes": [
            {
                "departureCityId": 75,
                "arrivalCityId": 491,
                "departureDate": "2025-07-02"
            }
        ],
        "searchId": "64a9d5a1-0a85-4f98-b317-8ad5dcf8f9b2",
        "sessionId": "41240625-c654-44a3-ab34-fe43ff736821",
        "pageId": "6e5lCJ-J8HD",
        "userData": {
            "screenSize": "sm"
        },
        "source": "offers"
    })
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://avia.tutu.ru',
        'priority': 'u=1, i',
        'referer': 'https://avia.tutu.ru/',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'Cookie': 'tutuid_access_token=a28da3b72debd40c7b696750bbb1176101f5f3ae698343a94ba410f2b1cc7a25; SESSIONID=41240625-c654-44a3-ab34-fe43ff736821; tutuid_csrf=p4EHw7DBiHY6VM5_-LFvXKXw; _gcl_au=1.1.1943430684.1750789290; tmr_lvid=5c216b2c43801848430357028b65da4b; tmr_lvidTS=1750789290305; mindboxDeviceUUID=be3d021d-efa5-4e45-9d76-616c5ffae6f7; directCrm-session=%7B%22deviceGuid%22%3A%22be3d021d-efa5-4e45-9d76-616c5ffae6f7%22%7D; servercookie3__cross_domain_secured=dc965cf5f56b577ea1614867c6f71ca2; servercookie3__cross_domain=986deb5c27bc1b45de2a41cb839dd69d; need_propagation=%7B%22servercookie3__cross_domain_secured%22%3A%7B%22value%22%3A%22dc965cf5f56b577ea1614867c6f71ca2%22%2C%22expire%22%3A%22126144000%22%2C%22secure%22%3Atrue%2C%22httpOnly%22%3Atrue%2C%22check_hash%22%3A%2221e817499cbf3cd5e79c355271d9889e%22%7D%2C%22servercookie3__cross_domain%22%3A%7B%22value%22%3A%22986deb5c27bc1b45de2a41cb839dd69d%22%2C%22expire%22%3A%22126144000%22%2C%22secure%22%3Atrue%2C%22httpOnly%22%3Atrue%2C%22check_hash%22%3A%22c754c37ca83b5a03c46b3d7c11d6a2b6%22%7D%7D; _ym_uid=1750789290640944283; _ym_d=1750789290; advcake_track_id=d1c4bb4d-5e5a-c430-12af-e7e40bdff4d8; advcake_session_id=974b682f-c82e-ec98-577f-be508fd39334; _ym_isad=2; adrdel=1750789290423; adrcid=AHWIZ8jgdJ-50Vw7VfWajdA; acs_3=%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1750875690448%2C%22sl%22%3A%7B%22224%22%3A1750789290448%2C%221228%22%3A1750789290448%7D%7D; uxs_uid=0e131a40-5128-11f0-a048-61ec54d50ae9; ptt_ad_banner_hidden=1; PAGEID=6e5lCJZ-MCR'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


