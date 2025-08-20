from maksim_tsybulka.class_work.class_work_14.conftest import api_client
import pytest
import json

@pytest.mark.parametrize('query, min_results', [
        ("ноутбук", 10),
        ("телевизор", 4),
        ("смартфон", 15),
                                                ])
def test_product_search(api_client, query, min_results):

    respons = api_client.search_products(query)
    assert 'products' in respons
    assert isinstance(respons['products'], list)
    assert isinstance(respons, dict)
    assert len(respons['products'][0]) >= min_results

    print(respons)
#
#
#
#
#
# class TestClassTests:
#     def test_сложение(self):
#         assert 2 + 2 == 4
#
#
#     def test_деление(self):
#         assert 10/2 == 5
#
#     def test_список(self):
#         слова = ["тест", "код", "pytest"]
#
#         assert "pytest" in слова
#
#
#     @pytest.fixture
#     def список_студентов(self):
#         return ["Аня", "Борис", "Виктор"]
#
#     def test_первый_студент(self, список_студентов):
#         assert список_студентов[0] == 'Аня'
#
#
#     @pytest.mark.parametrize("a, b, ожидаймый", [(1, 1, 2),
#                                                 (0, 5, 5),
#                                                 (-1, 3, 2),
#                                                 ])
#     def test_сложение(self, a, b, ожидаймый):
#         assert a + b == ожидаймый
#


def test_bel(api_client):
    response = api_client.search_products(2427, 1, "one", "226f95dc-1a09-4658-a0c8-7626ad6cd665")

    print(response)