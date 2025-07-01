import pytest
from maksim_tsybulka.class_work.class_work_14.onliner.api import OnlinerAPI


@pytest.fixture(scope="session")
def api_client():
    """Фикстура для создания API слиента"""

    client = OnlinerAPI()

    yield client
