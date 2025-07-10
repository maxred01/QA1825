import pytest
from ..Class_work_14.onliner_api.onliner_api import OnlinerAPI

@pytest.fixture(scope='session')
def api_client():
    """Фикстура для создания API клиента"""

    client = OnlinerAPI()

    yield client
