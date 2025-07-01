from maksim_tsybulka.class_work.class_work_14.conftest import api_client


def test_product_search(api_client):

    respons = api_client.search_products('ноутбук')

    print(respons)