import requests

class APIClient:
    """Базовый клиент для работы с API"""

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0',
                                     'Accept': '*/*',
                                     'Content-Type': 'application/json'})

    def request(self, method, endpoint, **kwargs):
        """Универсальный метод для отправки запросов"""

        url = f'{self.base_url}/{endpoint.lstrip("/")}'

        try:
            response = self.session.request(method, url, **kwargs)

            response.raise_for_status()

        except requests.exceptions.HTTPError as e:
            print(f"Request error: {e}")
            raise

        try:
            response.json()
        except ValueError:
            return response.text
        