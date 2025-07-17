from polina_shubelko.class_work.class_work_12.conftest import api_client
import pytest
@pytest.mark.parametrize ('query, min_results', [
    ("ноутбук", 10),
    ("телевизор", 4),
    ("смартфон", 15),
])

def test_product_search(api_client, query, min_results):

     respons = api_client.search_products(query)
     assert 'products_count' in respons
     assert isinstance(respons['products_count'], list)
     assert isinstance(respons, dict)
     assert len(respons['products_count'][0]) >= min_results

     print(respons)
