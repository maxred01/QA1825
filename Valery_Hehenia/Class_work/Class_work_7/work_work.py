import requests




def test_find_by_status():
    url = "https://petstore.swagger.io/v2/pet/findByStatus?status=pending"

    status_pending = "pending"
    name = "UpdatedPet_690"

    response = requests.request("GET", url, params={"name": name})

    result = response.json()
    print(result)
    result_name = result[0]['name']

    assert response.status_code == 200, 'Сайт недосступен? Ожидался стату код 200.'
    # assert result[0]['status'] == name, 'Неверный статус в поле "status"'
    # assert result[0]['name'] == name, f'Неверный статус в поле "name", а вывелось {result_name}'
    assert 'name' in result[0], 'ключа "name" нет в ответе'

def test_inventory():

    for i in range(3):
        url = "https://petstore.swagger.io/v2/store/inventory"
        response = requests.request("GET", url)
        result = response.json()

        if '7000' in result:
            assert result['7000'] == 1, f'попытка {i+1}: значение равно {result["7000"]}'
            print('Проверка пройдена')
            break
        else:
            print( f'попытка {i+1}: ключ "7000" не найден')
    else:
        assert False, 'Ключ "7000" не найден после 3 попыток'



def test_inventory1():

    for i in range(3):
        url = "https://petstore.swagger.io/v2/store/inventory"
        response = requests.request("GET", url)
        result = response.json()

        if '7000' in result:
            assert result['NOT_avialable'] == 1, f'попытка {i+1}: значение равно {result["NOT avialable"]}'
            print('Проверка пройдена')
            break
        else:
            print( f'попытка {i+1}: ключ "NOT avialable" не найден')
    else:
        assert False, 'Ключ "NOT avialable" не найден после 3 попыток'