from Valeria_Pavlovich.Class_work.Class_work_14.class_14.clients.api_client import APIClient


class BelaviaAPI(APIClient):
    """Специализированный клиент для API Belavia.by"""

    def __init__(self):
        super().__init__("https://belavia.by/")

    def main_page(self):
        """Стартовая страница"""
        return self.get('/')

    def buy_tickets(self):
        """Купить билеты"""
        return self.get('/#ibe')

    def check_in(self):
        """Регистрация на рейс"""
        return self.get('/#wci')

    def transfer(self):
        """Трансфер"""
        return self.get('/#transfer')

    def hotel(self):
        """Отели"""
        return self.get('/#hotel')

    def tickets_order(self):
        """Заказ билетов"""
        return self.get('/booking/')

    def account(self):
        """Личный кабинет"""
        return self.get('/account/')

    def news(self):
        """Новости"""
        return self.get('/novosti/')

    def offers(self):
        """Предложения"""
        return self.get('/predlozheniya/')
