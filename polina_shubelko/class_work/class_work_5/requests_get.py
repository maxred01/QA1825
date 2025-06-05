import requests
import pytest

def test_find_by_status():
    url = "https://petstore.swagger.io/v2/pet/findByStatus?status=pending"
    status_pending = "pending"
    response = requests.request("GET", url, params={"status": status_pending})

    results = response.json()
    print(results)
    results_name = results[0]['name']

    assert response.status_code == 200, 'Сайт недоступен? Ожидался статус код 200'
    # assert results_name == status_pending, f'Неверный статус в поле "status", вывелось {results_name}'
    assert 'name' in results[0], 'Ключа "name" нет в ответе'

def test_inventory():
    url = "https://petstore.swagger.io/v2/store/inventory"
    response = requests.request("GET", url)
    results = response.json()

    assert results['7000'] == 1
    assert results['available'] == 235

def test_inventory2():
    for i in range(3):
        url = "https://petstore.swagger.io/v2/store/inventory"
        response = requests.request("GET", url)
        results = response.json()

        if '7000' in results:
            assert results['7000'] == 1, f'Попытка {i+1} : значение равно {results["7000"]}'
            print('Проверка пройдена')
            break
        else:
            print(f"Попытка{i+1}: ключ '7000' не найден")
    else:
        assert False, 'Ключ "7000" не найден после 3 попыток'

def test_inventory3():
    for i in range(3):
        url = "https://petstore.swagger.io/v2/store/inventory"
        response = requests.request("GET", url)
        results = response.json()

        if 'NOT available' in results:
            assert results['NOT available'] == 1, f'Попытка {i+1} : значение равно {results["NOT available"]}'
            print('Проверка пройдена')
            break
        else:
            print(f"Попытка{i+1}: ключ 'NOT available' не найден")
    else:
        assert False, 'Ключ "NOT available" не найден после 3 попыток'

def test_inventory4():
    url = "https://petstore.swagger.io/v2/store/inventory"
    response = requests.request("GET", url)
    results = response.json()

    for key, value in results.items():
        if key.isdigit():
            print(f'Проверка ключа {key} <UNK> {value} ')
