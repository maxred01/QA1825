date_str = "15.07.2023"

if "." in date_str:
    parts = date_str.split(".")
elif "/" in date_str:
    parts = date_str.split("/")
else:
    print("Неверный формат")
    exit()

if len(parts) != 3:
    print("Ошибка: должно быть 3 компонента")
else:
    day, month, year = parts
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        print("Ошибка: все части должны быть числами")
    else:
        iso_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
        print(f"ISO-формат: {iso_date}")