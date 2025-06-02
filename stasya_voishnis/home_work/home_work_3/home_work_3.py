# Задача 1: Система безопасности банка

pin =  int(input('Введите ПИН-код: '))
bank = 250000
cash = int(input('Введите сумму для снятия наличных: '))
limit_d = 100000
bank_new = bank-cash

if len(str(pin)) != 4:
    print('ПИН-код неверный')

elif cash > bank:
    print('Недостаточно средств')

elif cash > limit_d:
    print('Превышен дневной лимит')

else:
    print(f'Снятие наличных разрешено! Остаток {bank_new}')

# Задача 2: Умный термостат

people = input('Есть ли дома люди? (Да/Нет): ').lower()
weather = input('Кака] погода на улице? (Холодно/Тепло): ').lower()
time = float(input('Введите время суток в часах: '))

if people == 'да' and weather =='холодно':
    print('22°C')

elif people == 'да' and weather =='тепло':
    print('20°C')

elif 0 < time < 5:
    print('18°C')

else:
    print('16°C')

# Задача 3: Валидатао пароля

import re # Для работы с регулярными выражениями

def chek_password(password): # Определяет функцию
    problems = [] # Список

    if len(password) <8: # Количество символов
        problems.append('Пароль должен быть минимум 8 символов') # Добавление в список

    if not re.search(r'\d', password): # Наличие цифр
        problems.append('Пароль должен иметь хотя бы одну цифру') # Добавление в список

    if not re.search(r'[A-Z]', password): # Наличие заглавных букв
        problems.append('Пароль должен иметь хотя бы одну букву верхнего регистра') # Добавление в список

    if not re.search(r'[!@#$%^&*]', password): # Наличие !@#$%^&*
        problems.append('Пароль должен иметь спецсимвол (!@#$%^&*)') # Добавление в список

    return problems # Передает результаты функции в код

password = input('Введите пароль: ')
problems = chek_password(password) # Список проблем

if problems:
    print('Пароль недействителен по причинам: ')
    for problem in problems: # Цикл проверки
        print(f'{problem}') # Отображение проблем
else:
    print('Пароль создан')

# Задача 4: Конвертер дат

from datetime import datetime

data_input = input('Введите дату в формате(ДД.ММ.ГГГГ или ДД/ММ/ГГГГ): ')
try:
     data = datetime.strptime(data_input, '%d.%m.%Y') # Проверка формата
except ValueError:
    try:
        data = datetime.strptime(data_input, '%d/%m/%Y')
    except ValueError:
        print('Некорректный формат даты.')
        exit()

iso_format = data.strftime('%Y-%m-%d') # Преобразование
week = data.strftime('%A') #День недели
print(f'Дата: {iso_format}. День недели: {week}')

# Задача 5: Калькулятор налогов

dohod = float(input('Введите ваш доход: '))

if dohod  <= 20000:
    nalog = float(0.1 * dohod)
    print(f'При доходе {dohod:.2f}, налог составит {nalog:.2f}')

elif 20000 < dohod <= 50000:
    nalog = float(0.1 * 20000 + 0.2 *(dohod - 20000))
    print(f'При доходе {dohod:.2f}, налог составит {nalog:.2f}')

else:
    nalog = float(0.1 * 20000 + 0.2 * (50000 - 20000) + 0.3 *(dohod - 50000) + 5000)
    print(f'При доходе {dohod:.2f}, налог составит {nalog:.2f}')

# Задача 6: Система рекомендаций фильмов

age = int(input('Введите возраст: '))
genre = input('Введите любимый жанр(Комедия/Фантастика/Ужасы): ')
time = input('Введите время просмотра (Утро/Вечер): ').lower()

if age < 12:
    print('Рекомендуем к просмотру только мультфильмы')

elif time == 'утро':
    print('Рекомендуем к просмотру Комедию или Фантастику')

else:
    print(f'Рекомендуем к просмотру {genre}')

# Задача 7: Анализатор здоровья

age = int(input('Введите возраст: '))
weight = float(input('Введите вес в кг: '))
height =  float(input('Введите рост в метрах: '))
smoking = input('Курение (Да/Нет): ').lower()

bmi = float(weight/(height**2))

if bmi > 30:
    print('Риск здоровья: Высокий')
elif smoking == 'да' and age > 40:
    print('Риск здоровья: Высокий')
else:
    print('Риск здоровья: Умеренный')

# # Задача 8: Конвертер валют с комиссиями

operation = input('Выберите тип операции (Покупка/Продажа): ').lower()
valuta = input('Выберите валюту(USD/EUR/CNY)').upper()
cash = float(input('Введите сумму: '))

rates = {
    'USD': {'buy': 90, 'sell': 88, 'com': 0.015},
    'EUR': {'buy': 100, 'sell': 98, 'com': 0.01}
}

if valuta not in rates:
    print("Нет данных по этой валюте.")
    exit()

if operation == 'покупка':
    rate = rates[valuta]['buy']
    result = (cash / rate) * (1 - rates[valuta]['com'])
    print(f"Получите примерно {result:.2f} {valuta}")
else:
    rate = rates[valuta]['sell']
    result = cash * rate * (1 - rates[valuta]['com'])
    print(f"Получите примерно {result:.2f} рублей")


# # Задача 9: Система контроля доступа

visitor = input("Тип посетителя (Сотрудник/Контрагент/Гость): ").lower()
emergency = input("Экстренная ситуация? (Да/Нет): ").lower()
ban = input("В черном списке? (Да/Нет): ").lower()

if visitor == 'гость':
    escort = input("Есть сопровождающий? (Да/Нет): ").lower()

if visitor == 'контрагент':
    date_time = input("Рабочее время? (Да/Нет): ").lower()

if emergency == 'да':
    print("Доступ разрешен (экстренная ситуация).")
elif ban == 'да':
    print("Доступ запрещен: в черном списке.")
elif visitor == 'сотрудник':
    print("Доступ разрешен: сотруднику.")
elif visitor == 'контрагент':
    # В будни с 9 до 18
    if date_time == 'да':
        print("Доступ разрешен: контрагент в рабочие часы.")
    else:
        print("Доступ запрещен: не рабочие часы.")
else:
    if escort == 'да':
        print("Доступ разрешен: гость с сопровождающим.")
    else:
        print("Доступ запрещен: гость без сопровождающего.")


# # Задача 10: Генератор научных гипотез

t = int(input('Введите температуру в С: '))
p = int(input('Введите давление в (кПа): '))
c = input('Катализатор? (Да/Нет): ').lower()

if t < 0 and p > 100:
    print('Образование льда')
elif t > 100 and c == 'да':
    print('Реакция синтеза')
elif t > 200 and p > 500:
    print('Плазменное состояние')
else:
    print('Стабильное состояние')
