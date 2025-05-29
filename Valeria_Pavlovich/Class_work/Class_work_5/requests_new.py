#postman - code справа - code snippet - выпадающий список python-requests
import requests
url = "https://petstore.swagger.io/v2/pet/findByStatus?status=pending"
status_pending = "pending"
# response = requests.request("GET", url)
response = requests.request("GET", url, params={"status": status_pending})
results = response.json()
print(results)
results_name = results[0]['name']
# print(response.text)
# print(response.status_code)
assert response.status_code == 200, 'The site is unavailable? expected code 200'
# assert response.status_code == 300, 'The site is unavailable? expected code 200'
# assert results[0]['status'] == status_pending, 'Wrong status in the "Status" field'
# assert results_name == status_pending, f'Wrong status in the "Status" field: {results_name} is shown'
assert 'name' in results[0], 'the name key is not in the response'



