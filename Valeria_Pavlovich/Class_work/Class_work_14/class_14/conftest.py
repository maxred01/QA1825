import pytest
from Valeria_Pavlovich.Class_work.Class_work_14.class_14.site_belavia.api import BelaviaAPI

@pytest.fixture(scope="session")
def api_client():
    """Фикстура для создания API клиента"""

    client = BelaviaAPI()

    yield client