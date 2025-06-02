import requests
from httplib2.auth import params

url = "https://petstore.swagger.io/v2/pet/findByStatus?status=pending"
status_pending = "pending"
name= "UpdatedPet_690"

response = requests.request("GET",url, params={"name": name})

result = response.json()
print(result)
result_name = result[0]['name']


assert response.status_code == 200, 'Сайт недосступен? Ожидался стату код 200.'
#assert result[0]['status'] == name, 'Неверный статус в поле "status"'
#assert result[0]['name'] == name, f'Неверный статус в поле "name", а вывелось {result_name}'
assert 'name' in result[0], 'ключа "name" нет в ответе'