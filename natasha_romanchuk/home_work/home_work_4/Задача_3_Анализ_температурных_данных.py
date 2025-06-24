#Задача:
# Напишите функцию analyze_temps(temps), которая:
#
# Принимает список температур в формате [22.1, 18.5, 25.3, ...]
# Возвращает словарь с:
# Средней температурой
# Максимальной температурой
# Минимальной температурой
# Количеством аномалий (температура > 30 или < -10)
# Пример вызова:
#
# print(analyze_temps([22.1, 18.5, 31.2, -5.4]))
# # {'avg': 16.6, 'max': 31.2, 'min': -5.4, 'anomalies': 2}
# Требования:
#
# Использовать встроенные функции sum, min, max
# Реализовать подсчёт аномалий через генератор списка

def analyze_temps(temps):
    average = sum(temps) / len(temps)
    maximum = max(temps)
    minimum = min(temps)
    anamaliz = len([temp for temp in temps if temp > 30 or temp < -10]) # генератор списка, подсчет аномалий
    return {'average': round(average,1), 'maximum': maximum, 'minimum': minimum, 'anamaliz': anamaliz}
print(analyze_temps([12.8,35,22,-8]))
