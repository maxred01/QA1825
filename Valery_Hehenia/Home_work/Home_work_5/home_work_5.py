# Задача 1: Проверка чётности числа
import string


# def is_even(n):
#     return n % 2 == 0
# print(is_even(4))



# Задача 2: Генератор безопасного пароля

# import random
# import string
# def generate_password(length):
#     if length < 8:
#         raise ValueError("Длина пароля должна быть не менее 8 символов.")
#
#     num_digits = max(1, round(length * 0.2))
#     num_upper = round(length * 0.4)
#     num_lower = length - num_upper - num_digits
#
#     password_chars = (
#         random.choices(string.ascii_uppercase, k=num_upper) +
#         random.choices(string.ascii_lowercase, k=num_lower) +
#         random.choices(string.digits, k=num_digits)
#     )
#
#     random.shuffle(password_chars)
#     return ''.join(password_chars)
#
# print(generate_password(9))



# Задача 3: Анализ температурных данных

# def analyze_temps(temps):
#     avg_temp = round((sum(temps)/len(temps)),2)
#     max_temp = max(temps)
#     min_temp = min(temps)
#
#     anomalies = [n for n in temps if n>30 or n<-10 ]
#     return avg_temp, min_temp,max_temp, len(anomalies)
#
# print(analyze_temps([22.1, 18.5, 31.2, -11.4 ,2 , 1, -17]))



# Задача 4: Конвертер валют

# RATES = {
#     "USD": 1.0,
#     "EUR": 0.93,
#     "GBP": 0.79,
#     "JPY": 148.86
# }
# def convert(amount, from_curr, to_curr):
#     if from_curr not in RATES or to_curr not in RATES:
#         raise ValueError('Не существует такой валюты')
#
#     amount_in_valuta = amount / RATES[from_curr]
#     result = round((amount_in_valuta * RATES[to_curr]),2)
#     return result
#
# print(convert(1.3, "GBP", "JPY"))
# print(convert(100, "USD", "EUR"))
# print(convert(5000, "JPY", "GBP"))




# Задача 5: Шифр Цезаря

# import string
#
# def caesar_cipher(text, shift):
#     result = ''
#     lowercase = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
#     uppercase = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
#     for char in text:
#         if char in lowercase:
#             index = lowercase.index(char)
#             shifted_index = (index + shift) % 26
#             result += lowercase[shifted_index]
#         elif char in uppercase:
#             index = uppercase.index(char)
#             shifted_index = (index + shift) % 26
#             result += uppercase[shifted_index]
#         else:
#             result += char  # оставляем символ без изменений
#
#     return result
#
# print(caesar_cipher("Hello, World!", 3))
# print(caesar_cipher("XYZ", 4))




# Задача 6: Валидатор пароля

# def validate_password(password):
#
#     check_password = {
#         'lenght': len(password) >= 8,
#         'digit': any(char.isdigit() for char in password),
#         'upper': any(char.isupper() for char in password),
#         'punctuation': any(char in string.punctuation for char in password),
#     }
#     return check_password
#
# print(validate_password("Strong1@"))
# print(validate_password("Strong"))




# Задача 7: Статистика файла

# from collections import Counter
# import string
#
# def file_stats(filename):
#     with open(filename, "r",encoding="utf-8-sig" ) as file:
#         content = file.read()
#
#         lines = content.splitlines()
#         count_lines = len(lines)
#
#         words = content.split()
#         chars = content.replace("\n","")
#
#         word_count = len(words)
#         char_count = len(chars)
#
#         letters_only = [char.lower() for char in content if char.lower() in string.ascii_lowercase]
#         letter_counts = Counter(letters_only)
#         most_common = letter_counts.most_common(1)
#         letter, count = most_common[0]
#
#         stats = {
#             'lines': count_lines,
#             'chars': char_count,
#             'words': word_count,
#             'most_common': letter
#         }
#
#         return  stats
#
# print(file_stats("file.txt"))




# Задача 8: Генератор отчетов

import reports
# def prepare_report_data(data):
#     if not data:
#         return {
#             "total": 0,
#             "average": None,
#             "maximum": None
#         }
#     total = len(data)
#     average = sum(data) / total
#     maximum = max(data)
#     return {
#         "total": total,
#         "average": average,
#         "maximum": maximum
#     }
#
# def generate_text_report(data):
#     stats = prepare_report_data(data)
#
#     if stats["total"] == 0:
#         return "Отчет:\n=======\nНет данных для анализа"
#
#     return (
#         "Отчет:\n"
#         "=======\n"
#         f"Всего записей: {stats['total']}\n"
#         f"Среднее значение: {stats['average']:.1f}\n"
#         f"Максимум: {stats['maximum']}"
#     )
#
# def generate_html_report(data):
#     stats = prepare_report_data(data)
#
#     if stats["total"] == 0:
#         return "<p>Нет данных для анализа</p>"
#
#     html = f"""
#     <table border="1" cellpadding="5" cellspacing="0">
#         <thead>
#             <tr>
#                 <th>Показатель</th>
#                 <th>Значение</th>
#             </tr>
#         </thead>
#         <tbody>
#             <tr>
#                 <td>Всего записей</td>
#                 <td>{stats['total']}</td>
#             </tr>
#             <tr>
#                 <td>Среднее значение</td>
#                 <td>{stats['average']:.1f}</td>
#             </tr>
#             <tr>
#                 <td>Максимум</td>
#                 <td>{stats['maximum']}</td>
#             </tr>
#         </tbody>
#     </table>
#     """
#     return html.strip()
#
#
# data=[12, 18, 25, 37, 42]
# print(generate_text_report(data))
# print(generate_html_report(data))




# Задача 10: Калькулятор времени выполнения


import time
from functools import wraps

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = round(end - start, 3)

        message = f"Функция {func.__name__} выполнилась за {duration} секунд"
        print(message)

        with open("timings.log", "a", encoding="utf-8") as log_file:
            log_file.write(message + "\n")

        return result
    return wrapper




# Задача 9: API-клиент для погоды


import requests
import time

API_KEY = "16094d7e111a7f966fa0f00c8647659e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
_cache = {}
@timed
def get_weather(city):
    city = city.lower()
    now = time.time()

    # Кэш: 10 минут
    if city in _cache:
        cached_data, timestamp = _cache[city]
        if now - timestamp < 600:
            return cached_data

    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric",
            "lang": "ru"
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        result = {
            "temp": round(data["main"]["temp"], 1),
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }

        _cache[city] = (result, now)
        return result

    except requests.RequestException as e:
        return {"error": f"Ошибка соединения: {e}"}
    except (KeyError, IndexError):
        return {"error": "Ошибка обработки ответа API"}

print(get_weather("Minsk"))