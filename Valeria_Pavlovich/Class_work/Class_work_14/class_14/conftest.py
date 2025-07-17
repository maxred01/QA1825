import pytest
from Valeria_Pavlovich.Class_work.Class_work_14.class_14.site_belavia.api import HotelsB2API

@pytest.fixture(scope="session")
def api_client():
    """Фикстура для создания API клиента"""

    client = HotelsB2API()

    yield client