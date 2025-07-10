import requests


class ApiClient:
    """Базовый клиент для работы с API"""

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({'user-agent': '',
                                    'Accept': '*/*',
                                    'Content-Type': 'application/json'})

    def request(self, method, endpoint, **kwargs):
        """Универсальный метод для отправки запросов"""

        url = f'{self.base_url}/{endpoint.lstrip("/")}'

        try:
            respons = self.session.request(method, url, **kwargs)

            respons.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            raise

        try:
            respons.json()
        except ValueError:
            return respons.text


