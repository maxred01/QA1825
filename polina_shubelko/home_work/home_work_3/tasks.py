# Задача 1: Система безопасности банка

PIN = '1234'
balance = 150000
daily_limit = 100000

user_pin = input('Введите PIN-код (4 цифры): ')
if len(user_pin) != 4 or not user_pin.isdigit():
    print('Ошибка: PIN-код должен состоять из 4 цифр')
    exit()
if user_pin != PIN:
    print('Ошибка: неверный PIN-код')
    exit()
else:
    print('Верный PIN')

summa = float(input('Введите сумму для снятия: '))
if summa > balance:
    print('Ошибка: недостаточно средств на счёте')
elif summa > daily_limit:
    print('Ошибка: сумма превышает дневной лимит')
else:
    print('Операция успешно выполнена')

# Задача 2: Умный термостат

time_hour = int(input('Введите время суток (0-23): '))
weather = input('Погода на улице (холодно/тепло): ').lower()
people_home = input('Люди дома? (да/нет): ').lower()

if 6 <= time_hour <= 11:
    time_of_day = 'утро'
elif 12 <= time_hour <= 17:
    time_of_day = 'день'
elif 18 <= time_hour <= 23:
    time_of_day = 'вечер'
elif 0 <= time_hour <= 5:
    time_of_day = 'ночь'
else:
    print('Некорректный ввод времени суток')
    exit()

if people_home == 'да':
    if weather == 'холодно':
        temperature = 22
    elif weather == 'тепло':
        temperature = 20
    else:
        print('Некорректный ввод погоды')
        exit()
elif people_home == 'нет':
    temperature = 16
else:
    print('Некорректный ввод наличия людей дома')
    exit()

if time_of_day == 'ночь':
    temperature = 18
print(f'Рекомендуемая температура: {temperature}°C')

# Задача 3: Валидатор пароля

password = input('Введите пароль: ')
problems = []

if len(password) < 8:
    problems.append('Пароль должен содержать минимум 8 символов')
if not any(char.isdigit() for char in password):
    problems.append('Пароль должен содержать хотя бы одну цифру')
if not any(char.isupper() for char in password):
    problems.append('Пароль должен содержать хотя бы одну букву в верхнем регистре')
special_symbols = "!@#$%^&*"
if not any(char in special_symbols for char in password):
    problems.append('Пароль должен содержать хотя бы один спецсимвол (!@#$%^&*)')

if problems:
    print('Пароль невалиден по следующим причинам:')
    for problem in problems:
        print("-", problem)
else:
    print('Пароль валиден')

# Задача 4: Конвертер дат

date_input = input("Введите дату в формате 'ДД.ММ.ГГГГ' или 'ДД/ММ/ГГГГ': ")
import datetime
date_str = date_input.replace('/', '.')
try:
    date_obj = datetime.datetime.strptime(date_str, "%d.%m.%Y")
except ValueError:
    print("Некорректный формат даты.")
    exit()
iso_date = date_obj.strftime("%Y-%m-%d")
print(f"ISO-формат: {iso_date}")
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
day_of_week = days[date_obj.weekday()]
print(f"День недели: {day_of_week}")

# Задача 5: Калькулятор налогов

income = float(input('Введите ваш доход: '))
if income <= 20000:
    tax = income * 0.10
elif income <= 50000:
    tax = 20000 * 0.10
    excess = income - 20000
    tax += excess * 0.20
else:
    tax = 20000 * 0.10
    tax += (50000 - 20000) * 0.20
    excess = income - 50000
    tax += excess * 0.30 + 5000
print(f'Общий налог: {tax:.2f}')

# Задача 6: Система рекомендаций фильмов

age = int(input('Введите ваш возраст: '))
favorite_genre = input('Введите ваш любимый жанр (комедия, фантастика, ужасы): ').lower()
time_of_day = input('Когда вы планируете смотреть фильм? (утро/вечер): ').lower()
if age < 12:
    recommended_movie = 'Мультфильм'
elif time_of_day == 'утро':
    if favorite_genre in ['комедия', 'фантастика']:
        recommended_movie = f'{favorite_genre} фильм для утреннего просмотра'
    elif favorite_genre == 'ужасы':
        recommended_movie = 'Рекомендуется выбрать более легкий жанр для утра'
    else:
        recommended_movie = 'Рекомендуемый жанр не распознан'
elif time_of_day == 'вечер':
    recommended_movie = f'{favorite_genre} фильм для вечернего просмотра'
else:
    recommended_movie = 'Некорректный ввод времени суток'

print(f'Рекомендуемый фильм: {recommended_movie}')

# Задача 7: Анализатор здоровья

age = int(input('Введите ваш возраст: '))
weight = float(input('Введите ваш вес в (кг): '))
height = float(input('Введите ваш рост в (м): '))
smoking_input = input('Курите? (да/нет): ').lower()

bmi = weight / (height ** 2)
if bmi > 30:
    health_risk = 'высокий'
elif smoking_input == 'да' and age > 40:
    health_risk = 'высокий'
else:
    health_risk = 'умеренный'
print(f'Ваш индекс массы тела (ИМТ): {bmi:.2f}')
print(f'Уровень риска для здоровья: {health_risk}')

# Задача 8: Конвертер валют с комиссиями

amount_rub = float(input('Введите сумму в рублях: '))
target_currency = input('Введите целевую валюту (USD, EUR): ').upper()
operation_type = input('Введите тип операции (покупка/продажа): ').lower()

rates = { "USD": {"buy": 90, "sell": 88, "commission": 0.015},
    "EUR": {"buy": 100, "sell": 98, "commission": 0.01}}

if target_currency not in rates:
    print('Некорректная валюта')
    exit()

if operation_type == 'покупка':
    rate = rates[target_currency]["buy"]
elif operation_type == 'продажа':
    rate = rates[target_currency]["sell"]
else:
    print('Некорректный тип операции')
    exit()

commission_rate = rates[target_currency]["commission"]

if operation_type == 'покупка':
    amount_in_currency = (amount_rub / rate) * (1 - commission_rate)
    print(f"Вы получите примерно {amount_in_currency:.2f} {target_currency}")
elif operation_type == 'продажа':
    amount_in_rub = amount_rub * rate * (1 - commission_rate)
    print(f"Вы получите примерно {amount_in_rub:.2f} рублей")

# Задача 9: Система контроля доступа

from datetime import datetime, time
role = input('Введите роль (сотрудник, контрагент, гость): ').lower()
is_emergency = input('Экстренная ситуация? (да/нет): ').lower() == 'да'
is_on_banned_list = input('В запрещённом списке? (да/нет): ').lower() == 'да'

current_time = datetime.now().time()
current_weekday = datetime.now().weekday()  # 0=Понедельник, 6=Воскресенье

if is_emergency:
    print('Доступ разрешён: экстренная ситуация')
elif is_on_banned_list:
    print('Доступ запрещён: пользователь в запрещённом списке')
else:
    if role == 'сотрудник':
        print('Доступ разрешён: сотрудник')
    elif role == 'контрагент':
        if current_weekday < 5 and time(9, 0) <= current_time <= time(18, 0):
            print('Доступ разрешён: контрагент в рабочие часы')
        else:
            print('Доступ запрещён: вне рабочего времени для контрагента')
    elif role == 'гость':
        has_companion = input('Есть сопровождающий? (да/нет): ').lower() == 'да'
        if has_companion:
            print('Доступ разрешён: гость с сопровождающим')
        else:
            print('Доступ запрещён: гость без сопровождающего')
    else:
        print("Некорректная роль")

# Задача 10: Генератор научных гипотез

temperature = float(input('Введите температуру (°C): '))
pressure = float(input('Введите давление (кПа): '))
catalyst_input = input('Наличие катализатора (да/нет): ').lower()

has_catalyst = catalyst_input == 'да'

if temperature < 0 and pressure > 100:
    hypothesis = 'Образование льда'
elif temperature > 100 and has_catalyst:
    hypothesis = 'Реакция синтеза'
elif temperature > 200 and pressure > 500:
    hypothesis = 'Плазменное состояние'
else:
    hypothesis = 'Стабильное состояние'

print(f'Гипотеза: {hypothesis}')
