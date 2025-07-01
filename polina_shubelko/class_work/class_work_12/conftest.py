import pytest
from ..

@pytest.fixture(scope='session')
def api_client():
    """Фикстура для создания API клиента"""

    client = OnlinerAPI()

    yield client