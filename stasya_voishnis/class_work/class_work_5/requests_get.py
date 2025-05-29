import requests

url = "https://petstore.swagger.io/v2/pet/findByStatus"
status_pending = "pending"
response = requests.request("GET", url, params={"status": status_pending})

results = response.json()
print(results)
results_name = results[0]['name']

assert response.status_code == 200, 'Сайт недоступен? Ожидался статус код 200' # Проверяем статус код
assert results[0]['status'] == status_pending, 'Неверный статус в поле "status"' # [0] - список; ['status'] - ключ
#assert results_name == status_pending, f'Неверный статус в поле "status", а вывелось {results_name}'


assert 'name' in results[0], 'ключа "name" нет в ответе'