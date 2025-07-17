from ..clients.api_client import APIClient


class OnlinerAPI(APIClient):
    """Специализированный клиент для API Onliner.by"""

#Наследование от базового класса APIClient
    def __init__(self):
        #Вызов конструктора родительского класса
        super().__init__("https://www.onliner.by/sdapi")

    #Метод для поиска товара
    def search_products(self, query, **params):
        """Поиск товаров в каталоге"""

        #Параметры для поиска товаров
        parameters = {'query': query, **params}
        return self.get('catalog.api/search/products', params=parameters)

    def get_currency_rates(self):
        """Получение актуальных курсов валют"""

        return self.get('main.api/currency')

    def get_product_details(self, product_id):
        """Получение детальной информации о товаре"""
        return self.get(f'catalog.api/products/{product_id}')