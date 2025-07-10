import requests
import time
import re
import json


class TestCase:
    def __init__(self, name, url, method="GET", headers=None, data=None, expected_status=200, check_field=None,
                 expected_value=None):
        self.name = name
        self.url = url
        self.method = method
        self.headers = headers or {}
        self.data = data
        self.expected_status = expected_status
        self.check_field = check_field
        self.expected_value = expected_value

    def run(self):
        try:
            start_time = time.time()
            response = requests.request(
                method=self.method,
                url=self.url,
                headers=self.headers,
                data=self.data,
                timeout=10
            )
            response_time = round((time.time() - start_time) * 1000)

            # Проверка статуса
            if response.status_code != self.expected_status:
                return False, f"❌ Статус: {response.status_code} (ожидался {self.expected_status}), Время: {response_time}мс"

            # Проверка поля JSON (если указано)
            if self.check_field:
                try:
                    json_data = response.json()
                    actual_value = json_data.get(self.check_field)
                    if actual_value != self.expected_value:
                        return False, f"❌ Поле '{self.check_field}': {actual_value} (ожидалось {self.expected_value}), Время: {response_time}мс"
                except Exception as e:
                    return False, f"⚠️ Ошибка парсинга JSON: {str(e)}"

            return True, f"✅ Успешно! Статус: {response.status_code}, Время: {response_time}мс"
        except Exception as e:
            return False, f"⚠️ Критическая ошибка: {str(e)}"


# Реестр тестов (легко добавлять новые)
TEST_CASES = [
    TestCase(
        name="Главная emall",
        url="https://emall.by/",
        method = "GET"
),
TestCase(
    name="Хэдер акции",
    url="https://emall.by/_next/data/h-Fm_R5z61oKMzymYTz9B/actions.json",
    method="GET"
),
TestCase(
    name="Продукты",
    url="https://emall.by/_next/data/h-Fm_R5z61oKMzymYTz9B/category/4220.json?id=4220",
    method="GET"
),
TestCase(
    name="Корзина Edostavka",
    url="https://api2.edostavka.by/api/v2/basket",
    method="POST",
    headers={
        'sec-ch-ua-platform': '"Windows"',
        'Referer': 'https://edostavka.by/',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'Web-User-Agent': 'SiteEdostavka/1.0.0',
        'sec-ch-ua-mobile': '?0',
        'apiToken': 'Fek5TJRyidOSSzB1dGqxkxqX7zBccNMv',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Cookie': 'hg-client-security=2yxsLGA5e6LHVvE1scgoJYwYVah'
    },
    data=json.dumps({
        "productId": 770036,
        "quantityInBasket": 190,
        "gtmItemListId": "",
        "gtmItemListName": ""
    }),
    check_field="expressDeliveryPrice",
    expected_value=5.99
),
]

def test_run_api_tests() -> str:
    results = []
    passed_count = 0
    failed_count = 0

    for test in TEST_CASES:
        success, message = test.run()
        result_line = f"{test.name} ({test.url}): {message}"
        results.append(result_line)

        if success:
            passed_count += 1
        else:
            failed_count += 1

    total_tests = len(TEST_CASES)
    success_rate = round(passed_count / total_tests * 100) if total_tests else 0

    summary = (
        f"\n\n📊 ИТОГИ ТЕСТИРОВАНИЯ:\n"
        f"✅ Успешных тестов: {passed_count}\n"
        f"❌ Проваленных тестов: {failed_count}\n"
        f"🔢 Всего тестов: {total_tests}\n"
        f"🏁 Процент успеха: {success_rate}%"
    )

    return "\n".join(results) + summary

# def test_register_valid_data():
#     url = "https://knigogid.ru/register"
#     session = requests.Session()
#
#     # Предварительный GET-запрос, чтобы получить токен
#     response = session.get(url)
#     assert response.status_code == 200
#
#     # Парсинг CSRF-токена из HTML (упрощённо)
#     match = re.search(r'name="_token"\s+value="([^"]+)"', response.text)
#     assert match, "CSRF-токен не найден на странице"
#     csrf_token = match.group(1)
#
#     # Payload (валидные данные)
#     payload = {
#         '_token': csrf_token,
#         'name': 'Nats',
#         'email': 'nats1234@maby.com',
#         'password': 'MyPass123!',
#         'password_confirmation': 'MyPass123!',
#     }
#
#      # POST-запрос на регистрацию
#     post_response = session.post(url, data=payload)
#
#     # Проверка успешного редиректа (после успешной регистрации будет редирект)
#     assert post_response.status_code in (200, 302, 303), f"Ожидался 200/302, но получен {post_response.status_code}"
#     print("Регистрация прошла успешно или запущен редирект.")
#
#
#
# def test_register_login():
#     url = "https://knigogid.ru/login"
#     session = requests.Session()
#
#     # Предварительный GET-запрос, чтобы получить токен
#     response = session.get(url)
#     assert response.status_code == 200
#
#     # Парсинг CSRF-токена из HTML (упрощённо)
#     match = re.search(r'name="_token"\s+value="([^"]+)"', response.text)
#     assert match, "CSRF-токен не найден на странице"
#     csrf_token = match.group(1)
#
#     # Payload (валидные данные)
#     payload = {
#         '_token': csrf_token,
#         'email': 'nats1234@maby.com',
#         'password': 'MyPass123!',
#
#     }
#
#      # POST-запрос на вход
#     post_response = session.post(url, data=payload)
#
#     # Проверка успешного входа
#     assert post_response.status_code in (200), f"Ожидался 200/302, но получен {post_response.status_code}"
#
#
#
# def test_poisk_bulgakov_post():
#     import requests
#
#     url = "https://knigogid.ru/ajax/search_main"
#     session = requests.Session()
#
#     # Предварительный GET-запрос, чтобы получить токен
#     response = session.get(url)
#     assert response.status_code == 200
#
#     # Парсинг CSRF-токена из HTML (упрощённо)
#     import re
#     match = re.search(r'name="_token"\s+value="([^"]+)"', response.text)
#     assert match, "CSRF-токен не найден на странице"
#     csrf_token = match.group(1)
#     import requests
#
#
#     payload = "query=%D0%B1%D1%83%D0%BB%D0%B3%D0%B0%D0%BA%D0%BE%D0%B2&sort=relevance&where%5Bbook%5D=1&where%5Bauthor%5D=1"
#     headers = {
#         'Accept': 'application/json, text/javascript, */*; q=0.01',
#         'Accept-Language': 'ru,en;q=0.9',
#         'Connection': 'keep-alive',
#         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         'Origin': 'https://knigogid.ru',
#         'Referer': 'https://knigogid.ru/',
#         'Sec-Fetch-Dest': 'empty',
#         'Sec-Fetch-Mode': 'cors',
#         'Sec-Fetch-Site': 'same-origin',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 YaBrowser/25.4.0.0 Safari/537.36',
#         'X-CSRF-TOKEN': 'AAitqajCizG3KgeKoH8o0XdO25kY8IynPkpUKRk8',
#         'X-Requested-With': 'XMLHttpRequest',
#         'X-Socket-Id': '980266953.780988023',
#         'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "YaBrowser";v="25.4", "Yowser";v="2.5"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'Cookie': '_ym_uid=1749580710981224948; _ym_d=1749580710; _ym_isad=2; _ym_visorc=w; XSRF-TOKEN=eyJpdiI6IkUyK1NaQktNL2s2WFdtSXV4VWtjb3c9PSIsInZhbHVlIjoiL05uMGRTVng2SE1kZlJOUFRnYVFBR1VxVXVZeTdESnp3a3RISXF1TTRDZjFpVTRNV3YzaHFPcDRrdm4rVnBScGxSam5nYkpBSTlyL2haMHh1bXNUZzlQZU5yVVEvdUdvOFlQWTFyN0RnNWVoeWpaeW5OeWpEZ1plZjd4aTBjZEsiLCJtYWMiOiI4ZjVlMWQyYmY0ZDU0YmVhMDc3NjE5NzFjYTY4YWUwOGU0OTQzZjgzNGVjNzA4NGU5Yjg3NTAzZTA4YWZhNmRjIiwidGFnIjoiIn0%3D; knigogid_session=eyJpdiI6IlRjOXdTQVZwai9OMUJjZWRVcEJrcFE9PSIsInZhbHVlIjoiTkdFaWxLQnE1cCtkL3pta3R2dGhiVnVnVVRscEFVS0pkNXgxeWV3RXJXL3FXSGNCMktRS0x2TFdpL2VoTlFEelcyZ2V0UldiMjVXMFVTc2lmeE5qTTdoSFJybHh4Y1cvVlo2WGxmVmtqTWVsUWNOQkYwUzhodUJmbVU2b1BnU2kiLCJtYWMiOiJlNjQ4NzE3ZmNmOGQzYjU5OTFjMzA3ZGFlZmNmMzYwOGRkNDhlMzUyMjhiNWQ5N2I2ZGI1NWNhNzFjNDMxOWQ2IiwidGFnIjoiIn0%3D; XSRF-TOKEN=eyJpdiI6ImlaNnpWelFwdzBYdDBqQ2tCTHFYM3c9PSIsInZhbHVlIjoiR1h4cFBrWGlSOFI1WHlBZjNxTXkwVWh5cHR5ckVOWncvdVI2Qk8wVGRaSDBJZ1EySy9oTVNmandMU2tDSEdTdVZxNHlEU1ZUS2grSnZ3UXRkWFV6V0R2ZXBvWTFUdE9NRXdRbkZuSll2WExDaU8waUxTRnYyMjdqQlF5OTVMR0wiLCJtYWMiOiIzZGQ3ZmFlY2E3YzMzNzI1ZjQ5YmY2YTgwNmY3NDZhZDZhMGY2MWM1M2I2N2U0ZjMyNzUxYjZlOWMyYzlhMDY5IiwidGFnIjoiIn0%3D; knigogid_session=eyJpdiI6IkFvQzlRUm0vZXY4N1BSTHBwbi9lSmc9PSIsInZhbHVlIjoiS2RnSXJiLzd3bzdIMmR1TkNCaCtlY1J6ai8rWjg5MHBFR0RobHkrTmRoMEdvUWZRU2djaHNiYUVEa2dzVWNwR0VtVVplVmhqZDZuOHkxTWlLVm45S2dGbU9jVFFnMTA2dFR6TnJKVHlxRmxvekEzMjhGcTgvblFzQlc3RFh3aisiLCJtYWMiOiJjN2ViYzA2ZDRkMzlhNzdjZmU0NmZmY2QzNTc2M2Q1NDdjNzQ2ZjE0ZmQ2MTI4NThhNzRhY2YyMjdlOGIzYjI1IiwidGFnIjoiIn0%3D'
#     }
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#
#     print(response.text)
#
#     assert post_response.status_code in (200), f"Ожидался 200, но получен {post_response.status_code}"



