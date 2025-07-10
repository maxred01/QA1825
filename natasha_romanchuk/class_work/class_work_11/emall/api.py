from ..clients.api_client import APIClient


class OnlinerAPI(APIClient):
    """Специализированный клиент для API Onliner.by"""

# Наследование от базового класса APIClient
    def __init__(self):
        super().__init__("https://emall.by/sdapi") # Вызов конструктора родительского класса

    def search_products(self, query, **params): # Метод для поиска товаров
        """Поиск товаров в каталоге"""
        parameters = {'query': query, **params}
        return self.get('catalog.api/search/products', params=parameters)

    def get_currency_rates(self):
        """Получение актуальных курсов валют"""

        return self.get('main.api/currency')

    def get_product_details(self, product_id):
        """Получение детальной информации о товаре"""
        return self.get(f'catalog.api/products/{product_id}')