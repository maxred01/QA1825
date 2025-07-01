import requests
class APIClient:
    """Base client for API"""

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
                                     'Accept':'*/*',
                                     'Content-Type':'application/json'})
    def request(self, method, endpoint, **kwargs):
        """Universal method to send requests"""

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f'Request error: {e}')
            raise

        try:
            response.json()
        except ValueError:
            return response.text

        