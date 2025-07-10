import requests
from Valery_Hehenia.Class_work.Class_work_14.api_client.api_client import APIClient

class OnlinerAPI(APIClient):
    """Специализированный клиент для API Onliner.by"""

    def __init__(self):
        #Вызов родительского метода с параметрами
        super().__init__("https://www.onliner.by/sdapi")


    #Метод поиска продукта
    def search_products(self, query, **params):
        """
        Поиск товаров в каталоге
        :param query:
        :param params:
        :return:
        """


        parameters = {'query': query, **params}
        return self.get('catalog.api/search/products', params=parameters)


    #Метод получения актуальных курсов
    def get_currency_rates(self):
        """Получение актуальных курсов валют"""

        return self.get('main.api/currency')



    def get_product_details(self, product_id):
        """Получение детальной информации о товаре"""
        return self.get(f'catalog.api/products/{product_id}')



