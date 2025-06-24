# Создайте модуль reports.py с функциями:
#
# generate_text_report(data) - возвращает строку в формате:
# Отчет:
# =======
# Всего записей: 10
# Среднее значение: 25.6
# Максимум: 48
# generate_html_report(data) - возвращает HTML-таблицу
# Пример использования:
#
# from reports import generate_text_report
#
# data = [12, 18, 25, 37, 42]
# print(generate_text_report(data))
# Требования:
#
# Единый обработчик данных для разных форматов
# Поддержка пустых входных данных
