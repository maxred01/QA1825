import requests
from Valeria_Pavlovich.Class_work.Class_work_14.class_14.api_client.api_client import APIClient
class BelaviaAPI(APIClient):
    """Specialized client for API Belavia.by"""
    def __init__(self):
        super().__init__('https://webapi.belavia.by/')

    def search_products(self, query, **params):
        """Search"""
        parameters = {'query': query, **params}
        return self.request('GET', 'site', params=parameters)

