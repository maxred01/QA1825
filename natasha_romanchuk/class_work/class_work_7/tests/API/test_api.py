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

