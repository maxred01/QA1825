from Valery_Hehenia.Class_work.Class_work_14.conftest import api_client
import pytest


@pytest.mark.parametrize('query, min_resaults', [
                        ("ноутбук", 10),
                        ('телевизор', 4),
                        ("смартфон", 15),
                                                  ])
def test_product_search(api_client, query, min_resaults):

    respons = api_client.search_products(query)
    assert 'products' in respons
    assert isinstance(respons['products'], list)
    assert isinstance(respons, dict)
    assert len(respons['products'][0]) >= min_resaults

    print(respons)




# def test_slojenie():
#     assert 2 + 2 == 4
#
#
# def test_delenie():
#     assert 10/2 == 5
#
# def test_spisok():
#     slova = ["test","kod", "pytest"]
#     assert "pytest" in slova
#
#
# @pytest.fixture
# def spisok_studentov():
#     return ["Anna","Boris","Viktor"]
#
#
# def test_pervii_student(spisok_studentov):
#     assert spisok_studentov[0] == "Anna"
#
#
# @pytest.mark.parametrize("a,b, ojidanie", [(1, 1, 2),
#                                            (0, 5, 5),
#                                            (-1, 3, 2),
#                                            ])
# def test_slojenie(a, b, ojidanie):
#     assert  a + b == ojidanie
