def test_product_search(api_client):

    response = api_client.search_products('ноутбук')

    print(response)
