import requests
from requests.exceptions import RequestException


class APIClient:
    """Базовый клиент для работы с API"""

    def __init__(self, base_url):
        self.base_url = base_url             # сохранение base_url для всех обьектов
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 YaBrowser/25.6.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru,en;q=0.9'
        })

    def _request(self, method, endpoint, **kwargs):
        """Внутренний метод для выполнения HTTP-запросов"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response
        except RequestException as e:
            print(f"Request failed: {method} {url} - {e}")
            raise

    def get(self, endpoint, params=None, **kwargs):
        """Метод для GET-запросов"""
        response = self._request('GET', endpoint, params=params, **kwargs)
        try:
            return response.json()
        except ValueError:
            return response.text

    def post(self, endpoint, data=None, json=None, **kwargs):
        """Метод для POST-запросов"""
        response = self._request('POST', endpoint, data=data, json=json, **kwargs)
        try:
            return response.json()
        except ValueError:
            return response.text


