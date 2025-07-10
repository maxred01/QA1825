import pytest
from polina_shubelko.class_work.class_work_12.rocketdata.api import OnlinerAPI


@pytest.fixture(scope="session")
def api_client():
    """Фикстура для создания API слиента"""

    client = OnlinerAPI()

    yield client