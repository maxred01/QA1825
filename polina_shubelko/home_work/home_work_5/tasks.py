# Задача 1: Проверка чётности числа

def is_even(n): return n % 2 == 0

# Задача 2: Генератор безопасного пароля

import random
import string

def generate_password(length):
    if length < 8:
        raise ValueError("Длина пароля должна быть не менее 8 символов")
    num_digits = max(1, int(length * 0.2))
    num_upper = int(length * 0.4)
    num_lower = length - num_digits - num_upper

    password_chars = (
            random.choices(string.ascii_uppercase, k=num_upper) +
            random.choices(string.ascii_lowercase, k=num_lower) +
            random.choices(string.digits, k=num_digits)
    )

    random.shuffle(password_chars)
    password = ''.join(password_chars)
    return password

print(generate_password(10))

# Задача 3: Анализ температурных данных

def analyze_temps(temps):
    avg_temp = sum(temps) / len(temps)
    max_temp = max(temps)
    min_temp = min(temps)
    anomalies = sum(1 for t in temps if t > 30 or t < -10)
    return {
        'avg': avg_temp,
        'max': max_temp,
        'min': min_temp,
        'anomalies': anomalies
    }

print(analyze_temps([22.1, 18.5, 31.2, -5.4]))

# Задача 4: Конвертер валют

RATES = {
    "USD": 1.0,
    "EUR": 0.93,
    "GBP": 0.79,
    "JPY": 148.86
}

def convert(amount, from_curr, to_curr):
    if from_curr not in RATES:
        raise ValueError(f"Неизвестный код валюты: {from_curr}")
    if to_curr not in RATES:
        raise ValueError(f"Неизвестный код валюты: {to_curr}")

    amount_in_usd = amount / RATES[from_curr]
    result = amount_in_usd * RATES[to_curr]

    return round(result, 2)

# Задача 5: Шифр Цезаря

import string

def caesar_cipher(text, shift):
    result = []

    for char in text:
        if char in string.ascii_lowercase:
            index = (string.ascii_lowercase.index(char) + shift) % 26
            result.append(string.ascii_lowercase[index])
        elif char in string.ascii_uppercase:
            index = (string.ascii_uppercase.index(char) + shift) % 26
            result.append(string.ascii_uppercase[index])
        else:
            result.append(char)
    return ''.join(result)

print(caesar_cipher("Hello, World!", 3))
print(caesar_cipher("XYZ", 4))

# Задача 6: Валидатор пароля

import string

def validate_password(password):
    length_ok = len(password) >= 8
    digit_ok = any(char.isdigit() for char in password)
    uppercase_ok = any(char.isupper() for char in password)
    special_chars = "!@#$%^&*"
    special_ok = any(char in special_chars for char in password)

    return {
        "length": length_ok,
        "digit": digit_ok,
        "uppercase": uppercase_ok,
        "special": special_ok
    }

print(validate_password("Weak"))
print(validate_password("Strong1@"))

# Задача 7: Статистика файла

from collections import Counter

def file_stats(filename):
    lines_count = 0
    words_count = 0
    chars_count = 0
    letter_counter = Counter()

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            lines_count += 1
            chars_in_line = len(line)
            chars_count += chars_in_line
            words = line.split()
            words_count += len(words)

            for ch in line:
                if ch.isalpha():
                    letter_counter[ch.lower()] += 1

    most_common_letter = letter_counter.most_common(1)
    most_common_char = most_common_letter[0][0] if most_common_letter else None

    return {
        'lines': lines_count,
        'words': words_count,
        'chars': chars_count,
        'most_common': most_common_char
    }

# Задача 8: Генератор отчетов

def generate_text_report(data):
    """
    Генерирует текстовый отчет по данным.
    Формат:
    Отчет:
    =======
    Всего записей: <число>
    Среднее значение: <число>
    Максимум: <число>
    """
    total_records = len(data)
    if total_records == 0:
        avg_value = 0
        max_value = 0
    else:
        avg_value = sum(data) / total_records
        max_value = max(data)

    report_lines = [
        "Отчет:",
        "=======",
        f"Всего записей: {total_records}",
        f"Среднее значение: {avg_value:.2f}",
        f"Максимум: {max_value}"
    ]

    return "\n".join(report_lines)


def generate_html_report(data):
    """
    Генерирует HTML-таблицу по данным.
    """
    total_records = len(data)
    if total_records == 0:
        avg_value = 0
        max_value = 0
        data_rows = ""
    else:
        avg_value = sum(data) / total_records
        max_value = max(data)
        data_rows = "".join(f"<tr><td>{value}</td></tr>" for value in data)

    html = f"""
<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Значение</th>
    </tr>
  </thead>
  <tbody>
    {data_rows}
  </tbody>
</table>
<p>Всего записей: {total_records}</p>
<p>Среднее значение: {avg_value:.2f}</p>
<p>Максимум: {max_value}</p>
"""
    return html.strip()
