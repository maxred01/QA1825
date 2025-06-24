
#
# def test_api():
#
#     url = "https://knigogid.ru/login"
#
#     payload = '_token=XjBav5FjZZ7AFPXAmphff6DOu9CBnfzImTRWvluF&email=nata%40yandex12.ru&password=3x9-EFf-Z75-Fpr'
#
#     response = requests.request("POST", url, data=payload)
#
#     assert response.status_code == 300, f'Статус код страницы "{url}" равен не 300 а {response.status_code}'
import requests
import time
import re


def test_run_api_tests() -> str:
    """Запускает тесты и возвращает результаты в виде строки"""
    urls = [
        ("https://knigogid.ru/", 'главной'),
        ("https://knigogid.ru/genres" ,'жанры'),
        ("https://knigogid.ru/books", 'книги'),
        ("https://knigogid.ru/reviews", 'рецензии'),
        ("https://knigogid.ru/register", 'регистрация'),
        ("https://knigogid.ru/blog", 'блоги'),
        ("https://knigogid.ru/quotes", 'цитаты'),
        ("https://knigogid.ru/tests", 'тесты'),
        ("https://knigogid.ru/collections", 'подборки'),
        ("https://knigogid.ru/awards", 'премии'),
        ("https://knigogid.ru/konkursy", 'конкурсы'),                    #провален
        ("https://knigogid.ru/lists", 'мировые рейтинги'),
        ("https://knigogid.ru/authors", 'авторы'),
        ("https://knigogid.ru/bookreadrs", 'популярное'),
        ("https://knigogid.ru/characters", 'персонажи'),
        ("https://knigogid.ru/sequences", 'книжные серии'),
        ("https://knigogid.ru/genres/307-hudozhestvennaya-literatura", 'художественная литература'),
        ("https://knigogid.ru/genres/693-detskaya-literatura", 'детская литература'),
        ("https://knigogid.ru/genres/137-kultura-i-iskusstvo", 'культура и искусство'),
        ("https://knigogid.ru/genres/1338-nauchnaya-literatura", 'научная литература'),
        ("https://knigogid.ru/genres/20-istoriya", 'история'),
        ("https://knigogid.ru/genres/412-biznes", 'бизнес'),
        ("https://knigogid.ru/genres/1340-prikladnaya-literatura", 'прикладная литература'),
        ("https://knigogid.ru/genres/1339-dokumentalnaya-literatura", 'документальная литература'),
        ("https://knigogid.ru/genres/1342-obrazovanie", 'образование'),
        ("https://knigogid.ru/genres/321-periodika", 'периодика'),
        ("https://knigogid.ru/genres/207-dom-i-semya", 'дом и семья'),
        ("https://knigogid.ru/genres/218-fizicheskaya-kultura", 'физическая культура'),
        ("https://knigogid.ru/genres/1345-zdorove", 'здоровье'),
        ("https://knigogid.ru/genres/439-literatura-na-inostrannyh-yazykah", 'литература на разных языках'),

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



def test_register_valid_data():
    url = "https://knigogid.ru/register"
    session = requests.Session()

    # Предварительный GET-запрос, чтобы получить токен
    response = session.get(url)
    assert response.status_code == 200

    # Парсинг CSRF-токена из HTML (упрощённо)
    import re
    match = re.search(r'name="_token"\s+value="([^"]+)"', response.text)
    assert match, "CSRF-токен не найден на странице"
    csrf_token = match.group(1)

    # Payload (валидные данные)
    payload = {
        '_token': csrf_token,
        'name': 'Nats',
        'email': 'nats1234@maby.com',
        'password': 'MyPass123!',
        'password_confirmation': 'MyPass123!',
    }

     # POST-запрос на регистрацию
    post_response = session.post(url, data=payload)

    # Проверка успешного редиректа (после успешной регистрации будет редирект)
    assert post_response.status_code in (200, 302, 303), f"Ожидался 200/302, но получен {post_response.status_code}"
    print("Регистрация прошла успешно или запущен редирект.")



def test_register_login():
    url = "https://knigogid.ru/login"
    session = requests.Session()

    # Предварительный GET-запрос, чтобы получить токен
    response = session.get(url)
    assert response.status_code == 200

    # Парсинг CSRF-токена из HTML (упрощённо)
    import re
    match = re.search(r'name="_token"\s+value="([^"]+)"', response.text)
    assert match, "CSRF-токен не найден на странице"
    csrf_token = match.group(1)

    # Payload (валидные данные)
    payload = {
        '_token': csrf_token,
        'email': 'nats1234@maby.com',
        'password': 'MyPass123!',

    }

     # POST-запрос на вход
    post_response = session.post(url, data=payload)

    # Проверка успешного входа
    assert post_response.status_code in (200), f"Ожидался 200/302, но получен {post_response.status_code}"
