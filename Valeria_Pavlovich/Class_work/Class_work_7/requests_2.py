import requests
import pytest
def test_find_by_status():
    url = "https://petstore.swagger.io/v2/pet/findByStatus"
    status_pending = "pending"

    response = requests.request("GET", url, params={"status": status_pending})

    results = response.json()
    print(results)
    results_name = results[0]['name']

    assert response.status_code == 200, 'The site is unavailable? expected code 200'

    assert 'name' in results[0], 'the name key is not in the response'

def test_inventory():
    url = "https://petstore.swagger.io/v2/store/inventory"
    response = requests.request("GET", url)
    results = response.json()

    assert results['7000'] == 1

def test_inventory2():
    for i in range(3):
        url = "https://petstore.swagger.io/v2/store/inventory"
        response = requests.request("GET", url)
        results = response.json()

        if '7000' in results:
            assert results["7000"] == 1, f"Attempt {i+1}: result equals {results['7000']}"
            print('Test passed')
            break
        else:
            print(f'Attempt {i+1}: key "7000" not found')
    else:
        assert False, 'Key "7000" not found after 3 attempts'

def test_inventory3():
    for i in range(3):
        url = "https://petstore.swagger.io/v2/store/inventory"
        response = requests.request("GET", url)
        results = response.json()

        
