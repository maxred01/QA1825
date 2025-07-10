import requests
from Valery_Hehenia.Class_work.Class_work_14.api_client.api_client import APIClient

class OnlinerAPI(APIClient):
    """Специализированный клиент для API Onliner.by"""

    def __init__(self):
        super().__init__('https://www.onliner.by/sdapi')

    def searche_produkts(self, query, **params ):
        """Поиск товаров в каталоге"""

        parametrs = {'query': query, **params}

        return self.request('GET', 'catalog.api/search/schemas', params=parametrs)

    def get_currency_rates(self ):
        """Получение курсов валют"""
        return self.request('GET', 'main.api/currency')



