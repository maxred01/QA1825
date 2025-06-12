import requests


def test_inventory2():
    for i in range(3):
        url = "https://petstore.swagger.io/v2/store/inventory"
        response = requests.request("GET", url)
        results = response.json()

        if '7000' in results:
            assert results["7000"] == 1, f"Попытка {i+1}: значение равно {results['7000']}"
            print('Проверка пройдена')
            break
        else:
            print(f"Попытка {i+1}: ключ '7000' не найден")
    else:
        assert False, 'Ключ "7000" не найден после 3 попыток'
