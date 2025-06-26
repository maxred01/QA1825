#Задача 4: Конвертер валют
# Создайте модуль currency_converter.py, который:
# Содержит словарь курсов валют:
# RATES = {
#     "USD": 1.0,
#     "EUR": 0.93,
#     "GBP": 0.79,
#     "JPY": 148.86
# }
# Реализует функцию convert(amount, from_curr, to_curr)
# Возвращает сумму после конвертации
# Пример использования:
#
# from currency_converter import convert
#
# print(convert(100, "USD", "EUR"))  # 93.0
# print(convert(5000, "JPY", "GBP")) # ≈26.54
# Требования:
#
# Обрабатывать несуществующие коды валют
# Округлять результат до 2 знаков после запятой

from currency_converter import convert
print(convert(100, "USD", "EUR"))
print(convert(5000, "JPY", "GBP"))
print(convert(5000, "JPY", "BYN"))