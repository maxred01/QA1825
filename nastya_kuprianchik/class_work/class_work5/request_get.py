import requests
import pytest

def test_find_by_status():
    url = "https://petstore.swagger.io/v2/pet/findByStatus"
    status_pending = 'pending'
    response = requests.request("GET", url, params={'status': status_pending})
    results = response.json()
    print(results)
    results_name = results[0]['name']
    assert response.status_code == 200, 'Сайт недоступен? Ожидался статус код 200'
    #assert results_name == status_pending, f'Неверный статус в поле "status", а вывелось {results_name}'
    # assert  'name' in results[0], 'ключ "name нет в ответе'


def test_inventory():

    url = 'https://petstore.swagger.io/v2/store/inventory'
    response = requests.request('GET', url)
    results = response.json()

    assert results["7000"] == 1


def test_inventory2():
    for i in range(3):
        url = 'https://petstore.swagger.io/v2/store/inventory'
        response = requests.request('GET', url)
        results = response.json()

        if '7000' in results:
            assert results["7000"] == 1, f"попытка {i+1}: значение равно {results["7000"]}"
            print('проверка пройдена')
            break
        else:
            print(f'попытка {i+1}: ключ "7000" не найден')
    else:
        assert False , 'ключ "7000" не найден после 3 попыток '

def test_inventory3():
    url = 'https://petstore.swagger.io/v2/store/inventory'
    response = requests.request('GET', url)
    results = response.json()

    for key, value in results.items():
        if key.isdigit():
            print(f'проверка ключа {key} {value}')
            if key == '7000':
                assert value == 1 , f'значение для "7000" равно {value}'