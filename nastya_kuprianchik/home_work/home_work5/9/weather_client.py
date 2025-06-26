import requests
import time

# Кэш словарь: ключ = название города, значение = (время, данные)
weather_cache = {}

# Твой API ключ (вставь свой)
API_KEY = "your_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    current_time = time.time()

    # Проверка кэша (если в нём есть данные не старше 10 минут)
    if city in weather_cache:
        cached_time, cached_data = weather_cache[city]
        if current_time - cached_time < 600:  # 600 секунд = 10 минут
            return cached_data

    # Параметры запроса
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',  # Температура в градусах Цельсия
        'lang': 'ru'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        # Формируем словарь с нужной информацией
        weather_data = {
            'temp': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        }

        # Сохраняем в кэш
        weather_cache[city] = (current_time, weather_data)
        return weather_data

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP ошибка: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Ошибка запроса: {req_err}")
    except KeyError:
        print("Ошибка разбора данных. Возможно, неверный формат ответа.")

    return None  # Если что-то пошло не так


# Пример использования
print(get_weather("Moscow"))
