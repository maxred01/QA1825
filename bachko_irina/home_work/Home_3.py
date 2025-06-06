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

if time >=6 and time <=11:
    result_time = 'утро'
elif 12 <= time <= 17:
    result_time = 'день'
elif 18 <= time <= 23:
    result_time = 'вечер'
elif 0 <= time <= 5:
    result_time = 'ночь'

if result_time != 'ночь' and people == 'да' and whether == 'холодно':
     print('люди дома и холодно → 22°C')
else:
     print('люди дома и тепло → 20°C')

if result_time == 'ночь' and people == 'да':
    print('ночь → 18°C')
else:
    print('людей нет → 16°C')


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



# Задача 5: Калькулятор налогов
# Условие: Рассчитайте налог по прогрессивной шкале:
#
# Доход ≤ 20 000 → 10%
# 20 000 < доход ≤ 50 000 → 20% на часть превышения
# Доход > 50 000 → 30% на превышение + фиксированный платеж 5000



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



# Задача 9: Система контроля доступа
# Условие: Проверьте доступ в зону:
#
# Сотрудник: доступ всегда
# Контрагент: только с 9:00 до 18:00 в будни
# Гость: только с сопровождающим
# Дополнительные условия:
#
# Экстренная ситуация → доступ всем
# Проверка на запрещенный список


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