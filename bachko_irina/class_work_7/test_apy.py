import requests
import time


def test_run_api_tests() -> str:
    """Запускает тесты и возвращает результаты в виде строки"""
    urls = [
        ("https://www.spacex.com/vehicles/falcon-9/", "главная страница spacex"),
        ("https://www.spacex.com/vehicles/starship/", "spacex_starship"),
        ("https://www.spacex.com/vehicles/falcon-heavy/", "spacex_falcon-heavy"),
        ("https://shop.spacex.com/cart", "spacex cart"),
        ("https://www.spacex.com/supplier/", "supplier"),
        ("https://shop.spacex.com/collections/all", "shop spacex" ),
        ("https://www.spacex.com/humanspaceflight/", "spacex_human spaceflight" )


    ]

    results = []
    passed_count = 0
    failed_count = 0

    for url, name in urls:
        try:
            start_time = time.time()
            response = requests.get(url, timeout=10)
            response_time = round((time.time() - start_time) * 1000)
            status = response.status_code

            if status == 200:
                result = f"✅ {name} ({url}) - Успешно! Статус: {status}, Время: {response_time}мс"
                passed_count += 1
            else:
                result = f"❌ {name} ({url}) - Ошибка! Статус: {status} (ожидался 200), Время: {response_time}мс"
                failed_count += 1

        except Exception as e:
            result = f"⚠️ {name} ({url}) - Критическая ошибка: {str(e)}"
            failed_count += 1

        results.append(result)

    # Итоговая статистика
    total_tests = len(urls)
    success_rate = round(passed_count / total_tests * 100) if total_tests else 0

    summary = (
        f"\n\n📊 ИТОГИ ТЕСТИРОВАНИЯ:\n"
        f"✅ Успешных тестов: {passed_count}\n"
        f"❌ Проваленных тестов: {failed_count}\n"
        f"🔢 Всего тестов: {total_tests}\n"
        f"🏁 Процент успеха: {success_rate}%"
    )

    return "\n".join(results) + summary

