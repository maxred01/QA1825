from datetime import datetime

date_str = input("Введите дату (ДД.ММ.ГГГГ или ДД/ММ/ГГГГ): ")

# Список допустимых форматов
formats = ["%d.%m.%Y", "%d/%m/%Y"]

date_obj = None
for fmt in formats:
    try:
        date_obj = datetime.strptime(date_str, fmt)
        break  # Если разобрали успешно, выходим из цикла
    except ValueError:
        continue

if date_obj is None:
    print("Неверный формат даты или некорректная дата!")
else:
    # Преобразуем дату в ISO-формат (ГГГГ-ММ-ДД)
    iso_date = date_obj.strftime("%Y-%m-%d")

    # Определяем день недели (0 - понедельник, 6 - воскресенье)
    week_days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    day_of_week = week_days[date_obj.weekday()]

    print("Дата в ISO-формате:", iso_date)
    print("День недели:", day_of_week)
