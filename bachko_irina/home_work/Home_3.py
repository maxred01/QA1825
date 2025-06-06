# Задача 1: Система безопасности банка
# Условие: Пользователь пытается снять деньги в банкомате.
#
# Проверьте ПИН-код (должен быть 4 цифры)
# Проверьте баланс (нельзя снять больше, чем есть)
# Проверьте лимит за день (не более 100 000 руб)
# Если все условия выполнены, разрешите операцию. Выводите конкретные сообщения об ошибках.


entered_pin = input('Введите ПИН-код: ')
balance = 200000
limit = 100000

if not entered_pin.isdigit() or len(entered_pin) != 4:
    print('Попробуйте еще раз! (введите четыре цифры)')
else:
    amount = int(input('Введите сумму для снятия: '))
    if amount >= limit or balance < amount:
        print(f'Превышен лимит. Лимит в день: {limit} руб.', f' Доступный баланс: {balance} руб.')
    else:
        balance -= amount
        limit += amount
        print(f'Операция прошла успешно. Остаток: {balance} руб.')



# Задача 2
# Умный термостат
# Условие: Система анализирует:
# Время суток (утро: 6-11, день: 12-17, вечер: 18-23, ночь: 0-5)
# Погоду на улице (холодно/тепло)
# Наличие людей дома (да/нет)


time = int(input('Введите время суток: '))
whether = str(input('Введите: холодно/тепло: ')).lower()
people = str(input('Люди дома: да/нет: ')).lower()

if 0 <= time <= 5:
    temp = 18
elif people_home == "нет":
    temp = 16
elif weather == "холодно":
    temp = 22
else:
    temp = 20

print(f"Температура установлена на {temp}°C")



#Задача 3
#Валидатор пароля
#Пароль должен содержать:
#Минимум 8 символов
#Хотя бы 1 цифру
#Хотя бы 1 букву в верхнем регистре
#Хотя бы 1 спецсимвол (!@#$%^&*)


password = input('Введите пароль: ')
numbers = '1234567890'
upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_letters = 'abcdefghijklmnopqrstuvwxyz'
symbols = '!@#$%^&*'
accep_password = numbers + upper_letters + lower_letters + symbols
passw = set(password)
if any(char not in accep_password for char in passw):
    print ('Ошибка. Запрещенный спецсимвол')
else:
    recommendations = []
    if len(password) < 8:
        recommendations.append(f'увеличить число символов - {8-len(password)}')
    for what, message in ((numbers,         'цифру '),
                          (upper_letters,   'заглавную букву '),
                          (lower_letters,   'строчную букву '),
                          (symbols,         'спецсимвол ')):
        if all(char not in what for char in passw):
            recommendations.append(f' добавить {message}')
    if recommendations:
        print( ",".join(recommendations))
    else:
        print('Отличный пароль. ')



# Задача 4: Конвертер дат
# Условие: Пользователь вводит дату в формате:
#
# "ДД.ММ.ГГГГ" или "ДД/ММ/ГГГГ" Программа должна:
# Проверить корректность формата
# Преобразовать в ISO-формат (ГГГГ-ММ-ДД)
# Определить день недели


date_str = "15.07.2025"

if "." in date_str:
    parts = date_str.split(".")
elif "/" in date_str:
    parts = date_str.split("/")
else:
    print('Неверный формат')
    exit()

if len(parts) != 3:
    print('Ошибка: должно быть три компонента')
else:
    day, month, year = parts
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        print('Ошибка: все части должны быть числами')
    else:
        iso_date = f'{year}-{month.zfill(2)}-{day.zfill(2)}'
        print(f'ISO-формат: {iso_date}')



# Задача 5: Калькулятор налогов
# Условие: Рассчитайте налог по прогрессивной шкале:
#
# Доход ≤ 20 000 → 10%
# 20 000 < доход ≤ 50 000 → 20% на часть превышения
# Доход > 50 000 → 30% на превышение + фиксированный платеж 5000


dohod = int(input('Введите ваш доход: '))

nalog_10 = 0.1
nalog_20 = 0.2
nalog_30 = 0.3

lim1=20000
lim2=30000

if dohod <= 20000:
    print (f'Сумма налога {dohod * nalog_10}')
elif 20000 < dohod <= 50000:
    lim = dohod - 20000
    print(f'Сумма налога {(lim1 * nalog_10) + (lim * nalog_20)}')
else:
    lim = dohod - 50000
    print(f'Сумма налога {(lim1 * nalog_10) + (lim2 * nalog_20) + (lim * nalog_30) + 5000}')



# Задача 6: Система рекомендаций фильмов
# Условие: Рекомендуйте фильм на основе:
#
# Возраста пользователя
# Любимого жанра (комедия, фантастика, ужасы)
# Времени просмотра (утро/вечер)
# Правила:
#
# Детям < 12 → только мультфильмы
# Утром → легкие жанры
# Вечером → любые жанры


age = int(input('Введите возраст: '))
time = input('Введите Утро/Вечер: ').lower()

if age > 12:
    if time == 'утро':
        print('Комедия, фантастика ')

    elif time == 'вечер':
        print('Ужасы, фантастика ')

else:
    print('только мультфильмы ')



# Задача 7: Анализатор здоровья
# Условие: На основе введенных данных:
#
# Возраст
# Вес (кг)
# Рост (м)
# Курение (да/нет)
# Рассчитайте:
#
# ИМТ (вес / рост²)
# Риск для здоровья:
# ИМТ > 30 → высокий
# Курение и возраст > 40 → высокий
# Остальные → умеренный


age = int(input('Введите возраст: '))
weight = float(input('Введите свой вес: '))
height = float(input('Введите свой рост: '))
smoke = str(input('Курите? Да или Нет: ')).lower()

IMT = (weight/(height*height))

if IMT > 30 or smoke == str('да') and age > 40:
    print('Риск для здоровья: Высокий! ')
else:
    print('Риск для здоровья: Умеренный! ')



# Задача 8: Конвертер валют с комиссиями
# Условие: Пользователь вводит:
#
# Сумму в рублях
# Целевую валюту (USD, EUR, CNY)
# Тип операции (покупка/продажа)
# Курс и комиссии:
#
# USD: 90 руб (покупка), 88 руб (продажа), комиссия 1.5%
# EUR: 100 руб (покупка), 98 руб (продажа), комиссия 1%


USD_buying = 90
USD_selling = 88
com1 = 0.015

EUR_buying = 100
EUR_selling = 98
com2 = 0.01

if currency == 'USD' and operation == 'покупка':
    summ_1 = float(summ / USD_buying)
    print(f'Вы пролучите {summ_1-(summ_1*com1):.2f} USD, Комиссия {com1*100}%')
elif currency == 'USD' and operation == 'продажа':
    summ_1 = float(summ / USD_selling)
    print(f'Вы пролучите  {summ_1 - (summ_1 * com1):.2f} USD, Комиссия {com1 * 100}%')
elif currency == 'EUR' and operation == 'покупка':
    summ_2 = float(summ / EUR_buying)
    print(f'Вы пролучите {summ_2 - (summ_2 * com2):.2f} EUR , Комиссия {com2 * 100}%')
else:
    summ_2 = float(summ / EUR_selling)
    print(f'Вы пролучите {summ_2 - (summ_2 * com2):.2f} EUR , Комиссия {com2 * 100}%')


# Задача 9: Система контроля доступа
# Условие: Проверьте доступ в зону:
#
# Сотрудник: доступ всегда
# Контрагент: только с 9:00 до 18:00 в будни
# Гость: только с сопровождающим
# Дополнительные условия:

# Экстренная ситуация → доступ всем
# Проверка на запрещенный список


data = input('Введите данные (сотрудник/контрагент/гость):').lower()
time = int(input('Введите время? (0-23): '))
day = input('Введите день недели?:').lower()
emergency = input('Экстренная ситтуация (да/нет):').lower()
escorted = input('Есть сопровождающий? (да/нет):').lower()
black = ['Иванов' , 'Петров']
lastname = input('Введите вашу фамилию:').capitalize()

if lastname in black:
    print('Доступ запрещен, Вы в черном списке')
elif emergency == 'да':
    print('Доступ разрешен, экстренная ситтуация')
elif data == 'сотрудник':
    print('Доступ разрешён')
elif data == 'контрагент' and day not in ['суббота', 'воскресенье']:
    print('Доступ разрешён')
elif data == 'гость' and escorted == 'да':
    print('Доступ разрешён с сопровождающим')
else:
    print('Доступ запрещён')


# Задача 10: Генератор научных гипотез
# Условие: На основе введенных параметров:
#
# Температура (°C)
# Давление (кПа)
# Наличие катализатора (да/нет)
# Сгенерируйте гипотезу:
#
# t < 0 и давление > 100 → "Образование льда"
# t > 100 и катализатор → "Реакция синтеза"
# t > 200 и давление > 500 → "Плазменное состояние"
# Иначе → "Стабильное состояние"


temp = int(input('Введите температуру: '))
press = int(input('Введите давление: '))
catalyst = input('Имеется катализатор? Да или Нет: ').lower()

if temp < 0 and press > 100:
    print('Образование льда')
elif  temp > 100 and catalyst == 'да':
    print('Реакция синтеза')
elif temp > 200 and press > 500:
    print('Плазменное состояние')
else:
    print('Стабильное состояние')
