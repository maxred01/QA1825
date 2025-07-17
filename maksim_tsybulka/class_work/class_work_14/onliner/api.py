from ..clients.api_client import APIClient


class OnlinerAPI(APIClient):
    """Специализированный клиент для API Onliner.by"""

    # Наследование от базового класса APIClient
    def __init__(self):

        # Вызов конструктора родителського класс
        super().__init__("https://hotels.belavia.by")

    # Метод для поиска товара
    def search_products(self, q, guests,  price,  sid):
        """Поиск товаров в каталоге"""

        # параметры для поиска товара
        parameters = {
            'q': q,
            'guests': guests,
            'price': price,
            'sid': sid,
                      }
        return self.get('hotel/belarus/minsk', params=parameters)

    def get_currency_rates(self):
        """Получение актуальных курсов валют"""

        return self.get('main.api/currency')

    def get_product_details(self, product_id):
        """Получение детальной информации о товаре"""
        return self.get(f'catalog.api/products/{product_id}')

