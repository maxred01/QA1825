from Valeria_Pavlovich.Class_work.Class_work_14.class_14.clients.api_client import APIClient


class HotelsB2API(APIClient):
    """Специализированный клиент для API Hotels.belavia.by"""

    def __init__(self):
        super().__init__("https://hotels.belavia.by/api")

    def search(self, query, **params):
        """Поиск отелей"""
        parameters ={'query': query, **params}
        return self.get('site/multicomplete.json', params=parameters)