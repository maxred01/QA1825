import requests
from natasha_romanchuk.class_work_11.api_client.api_client import APIClient

class OnlinerAPI(APIClient):
    def __init__(self):
        super().__init__('https://www.onliner.by/sdap')

    def searche_products(self, query, **params):
        """Поиск товаров в каталоге"""

        parametrs = {'query': query, **params}

        return self.request('GET', 'catalog.api/search/schemas', params=parametrs)

    def get_currency_rates(self):
        """Получение курсов валют"""
        
        return self.request('GET', 'main.api/currency')

if __name__ == '__main__':