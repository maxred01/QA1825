# #Задача 1 Система безопасности банка

pin = input("Введите PIN (4 цифры): ")
balance = 50000
limit = 100000
amount = int(input("Сколько хотите снять? "))

if not (pin.isdigit() and len(pin) == 4):
    print("Ошибка: PIN должен содержать 4 цифры.")
elif amount > balance:
    print("Ошибка: Недостаточно средств.")
elif amount > limit:
    print("Ошибка: Превышен дневной лимит.")
else:
    print("Операция одобрена. Заберите деньги.")


# #Задача 2 Умный термостат

time = int(input("Введите час (0-23): "))
weather = input("На улице холодно или тепло?(холодно/тепло) ").lower()
people_home = input("Люди дома? (да/нет): ").lower()

if 0 <= time <= 5:
    temp = 18
elif people_home == "нет":
    temp = 16
elif weather == "холодно":
    temp = 22
else:
    temp = 20

print(f"Температура установлена на {temp}°C")


#Задача 3 Валидатор пароля

password = input("Введите пароль: ")

if len(password) < 8:
    print("Пароль слишком короткий.")
if not any(char.isdigit() for char in password):
    print("Нет ни одной цифры.")
if not any(char.isupper() for char in password):
    print("Нет заглавной буквы.")
if not any(char in "!@#$%^&*" for char in password):
    print("Нет специального символа.")

else:
    print("Пароль принят.")

# Задача 4 Конвертер дат

# date = input('Введите дату (ДД.ММ.ГГ или ДД/ММ/ГГ):')
# date = date.replace('/','.')
#
# convert_data = date.split('-')
# print(convert_data)


# Задача 5 Калькулятор налогов

income = float(input("Введите доход: "))

if income <= 20000:
    tax = income * 0.10
elif income <= 50000:
    tax = (income - 20000) * 0.20
else:
    tax = 5000 + (income - 50000) * 0.30

print(f"Налог к оплате: {tax} рублей")


# Задача 6 Система рекомендаций фильмов

age = int(input('Введите Ваш возраст: '))
genre = (input('Любимый жанр (комедия, фантастика, ужасы): ')).lower()
time = (input('Время суток(утро,вечер): ')).lower()

if age < 12 :
    print('Рекомендуем мультфильм')
elif time == 'утро':
    print('Рекомендуем комедию или фантастику')
else:
    print('Рекомендуем ужасы')


# Задача 7 Анализатор здоровья

age = int(input('Введите Ваш возраст: '))
weight = int(input('Введите Ваш вес: '))
height = int(input('Введите Ваш рост: '))
smoking = (input('Курение (да,нет): ')).lower()

bmi = weight / (height ** 2)
if bmi > 30:
    print('Высокий риск для здоровья')
if smoking == 'да' and age >= 40:
    print('Высокий риск для здоровья')
else:
    print('Умеренный риск для здоровья')


# Задача 8 Конвертер валют с комиссиями

summ = float(input("Введите сумму в рублях: "))
currency = input("Целевая валюта (USD/EUR): ").upper()
operation = input("Операция (покупка/продажа): ").lower()

USD_buying = 90
USD_selling = 88
tax_1 = 0.015

EUR_buying = 100
EUR_selling = 98
tax_2 = 0.01

if currency == 'USD' and operation == 'покупка':
    summ_1 = float(summ / USD_buying)
    print(f'Вы пролучите {summ_1-(summ_1*tax_1):.2f} USD, Комиссия {tax_1*100}%')
elif currency == 'USD' and operation == 'продажа':
    summ_1 = float(summ / USD_selling)
    print(f'Вы пролучите  {summ_1 - (summ_1 * tax_1):.2f} USD, Комиссия {tax_1 * 100}%')
elif currency == 'EUR' and operation == 'покупка':
    summ_2 = float(summ / EUR_buying)
    print(f'Вы пролучите {summ_2 - (summ_2 * tax_2):.2f} EUR , Комиссия {tax_2 * 100}%')
else:
    summ_2 = float(summ / EUR_selling)
    print(f'Вы пролучите {summ_2 - (summ_2 * tax_2):.2f} EUR , Комиссия {tax_2 * 100}%')


# Задача 9 Система контроля доступа

role = input('Кто Вы? (сотрудник/контрагент/гость):').lower()
time = int(input('Который час?(0-23): '))
day = input('День недели?:').lower()
sos = input('Экстренная ситтуация(да/нет):').lower()
escorted = input('Есть сопровождающий?(да/нет):').lower()
blacklist = ['Романчук' , 'Башко' ]
lastname = input('Введите вашу фамилию:').capitalize()

if lastname in blacklist:
    print('Доступ запрещен, Вы в черном списке')
elif sos == 'да':
    print('Доступ разрешен, экстренная ситтуация')
elif role == 'сотрудник':
    print('Доступ разрешён.')
elif role == 'контрагент' and day not in ['суббота', 'воскресенье']:
    print('Доступ разрешён.')
elif role == 'гость' and escorted == 'да':
    print('Доступ разрешён с сопровождающим.')
else:
    print('Доступ запрещён.')


# Задача 10 Генератор научных гипотез

temperature = float(input('Введите температуру°C: '))
davlenie = float(input('Введите давление кПа: '))
catalizator = input('да/нет: ').lower()

if temperature < 0 and davlenie > 100:
    print('Образование льда')
if temperature > 100 and catalizator == 'да':
    print('Реакция синтеза')
if temperature >200 and davlenie >500:
    print('Плазменное состояние')
else:
    print('Стабильное состояние')