import datetime
date = input("Enter the date (dd.mm.yyyy or dd/mm/yyyy): ")
try:
    date_decode = datetime.datetime.strptime(date, "%d.%m.%Y")
except ValueError:
    try:
        date_decode = datetime.datetime.strptime(date, "%d/%m/%Y")
    except ValueError:
        print("Invalid date")
        exit()
date_format = date_decode.strftime("%Y.%m.%d")
weekday = date_decode.strftime("%A")
print(date_format)
print(weekday)
