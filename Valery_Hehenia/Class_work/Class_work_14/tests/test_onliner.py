from Valery_Hehenia.Class_work.Class_work_14.conftest import api_client
def test_product_search(api_client):

    respons = api_client.search_products('Ноутбук')

    print(respons)