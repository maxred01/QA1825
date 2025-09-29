import requests
from requests.exceptions import RequestException


class APIClient:
    """Базовый клиент для работы с API"""

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'OnlinerAPITestSuite/1.0',
            'Accept': 'application/json',
            'Accept-Language': 'ru-RU'
        })

    def _request(self, method, endpoint, **kwargs):
        """Внутренний метод для выполнения HTTP-запросов"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        try:
            response = self.session.request(method, url, **kwargs)
            # убираем response.raise_for_status(), чтобы 200/400/500 не кидали исключение
            return response
        except RequestException as e:
            print(f"Request failed: {method} {url} - {e}")
            raise

    def get(self, endpoint, params=None, **kwargs):
        """Метод для GET-запросов"""
        response = self._request('GET', endpoint, params=params, **kwargs)
        try:
            return response.status_code, response.json()
        except ValueError:
            return response.status_code, response.text

    def post(self, endpoint, data=None, json=None, **kwargs):
        """Метод для POST-запросов"""
        response = self._request('POST', endpoint, data=data, json=json, **kwargs)
        try:
            return response.status_code, response.json()
        except ValueError:
            return response.status_code, response.text
