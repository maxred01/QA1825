import pytest
from natasha_romanchuk.class_work.class_work_11.onliner.api import OnlinerAPI

@pytest.fixture(scope="session")
def api_client():
    """  """
    client = OnlinerAPI()

    yield client