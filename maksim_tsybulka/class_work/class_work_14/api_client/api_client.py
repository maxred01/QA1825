import requests


class APIClient:
    """Базовый клиент для работы с API"""

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
                                     'Accept': '*/*',
                                     'Content-Type': 'aplication/json'})

    def request(self, method, endpoint, **kwargs):
        """Уневерсальный метод для отправки запросов"""

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

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


