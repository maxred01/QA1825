# Задача 1: Система безопасности банка
# Условие: Пользователь пытается снять деньги в банкомате.
#
# Проверьте ПИН-код (должен быть 4 цифры)
# Проверьте баланс (нельзя снять больше, чем есть)
# Проверьте лимит за день (не более 100 000 руб)
# Если все условия выполнены, разрешите операцию. Выводите конкретные сообщения об ошибках.

print('Задание 1')
PIN = input('Введите ПИН-код (4 цифры): ')
CURRENT_BALANCE = 80000
USED_TODAY = 75000
DAILY_LIMIT= 100000

if not PIN.isdigit() or len(PIN) !=4:
    print('Ошибка: ПИН-код должен состоять из 4 циф.')

else:
    WITHROW_AMOUNT = int(input('Введите сумму для снятия: '))
    if CURRENT_BALANCE < WITHROW_AMOUNT:
         print(f'Ошибка: недостаточно средств. Доступный баланс: {CURRENT_BALANCE} руб.')
    else:
         if USED_TODAY + WITHROW_AMOUNT > DAILY_LIMIT:
             print(f'Ошибка: Превышен суточный лимит в {DAILY_LIMIT}. Уже использовано {USED_TODAY} руб')
         else:
             CURRENT_BALANCE -= WITHROW_AMOUNT
             DAILY_LIMIT += WITHROW_AMOUNT
             print(f'Операция разрешена. Снято: {WITHROW_AMOUNT} руб. Остаток: {CURRENT_BALANCE} руб.')





# Задача 2: Умный термостат
# Условие: Система анализирует:
#
# Время суток (утро: 6-11, день: 12-17, вечер: 18-23, ночь: 0-5)
# Погоду на улице (холодно/тепло)
# Наличие людей дома (да/нет)
# Правила:
#
# Если люди дома и холодно → 22°C
# Если люди дома и тепло → 20°C
# Если ночь → 18°C
# Если нет людей → 16°C


print('Задание 2')
TIME_DAY = int(input('Введите время суток: '))
WEATHER_OUTSIDE = str(input('Введите: Холодно/Тепло: ')).lower()
PEOPLE_HOME = str(input('Люди дома: Да/Нет: ')).lower()

if TIME_DAY >=6 or TIME_DAY <=11:
    CURRENT_TIME = 'утро'
elif 12 <= TIME_DAY <= 17:
    CURRENT_TIME = 'день'
elif 18 <= TIME_DAY <= 23:
    CURRENT_TIME = 'вечер'
elif 0 <= TIME_DAY <= 5:
    CURRENT_TIME = 'ночь'

if CURRENT_TIME == 'ночь':
    print('ночь → 18°C')
else:
    if PEOPLE_HOME == 'да':
        if WEATHER_OUTSIDE == 'холодно':
            print('люди дома и холодно → 22°C')
        else:
            print('люди дома и тепло → 20°C')
    else:
        print('нет людей → 16°C')





# Задача 3: Валидатор пароля
# Условие: Пароль должен содержать:
#
# Минимум 8 символов
# Хотя бы 1 цифру
# Хотя бы 1 букву в верхнем регистре
# Хотя бы 1 спецсимвол (!@#$%^&*)
# Выведите список проблем, если пароль невалиден.


print('Задание 3')
PASSWORD = input('Введите пароль: ')
if len(PASSWORD) < 8:
    print('Ошибка: Пароль имеет меньше 8 символов!')

elif not any (char.isdigit() for char in PASSWORD):
    print('Ошибка: Пароль должен содержать хотя бы ОДНУ цифру!')

elif not any(not char.isalnum() for char in PASSWORD):
    print('Ошибка: Пароль должен содержать хотя бы ОДИН спецсимвол!')

elif not any(char.isupper() for char in PASSWORD):
    print('Ошибка: Пароль должен содержать хотя бы ОДНУ заглавную  букву')

else:
    print('Пароль соответствует всем требованиям.')





# Задача 4: Конвертер дат
# Условие: Пользователь вводит дату в формате:
#
# "ДД.ММ.ГГГГ" или "ДД/ММ/ГГГГ" Программа должна:
# Проверить корректность формата
# Преобразовать в ISO-формат (ГГГГ-ММ-ДД)
# Определить день недели


print('Задание 4')
import datetime
DATA = input('Введите дату в формате ДД.ММ.ГГГГ" или "ДД/ММ/ГГГГ:  ')

if '.' in DATA:
    DATE_1 = DATA.replace('.','-',2)
elif '/' in DATA:
    DATE_1 = DATA.replace('/', '-', 2)

DAY, MONTH, YEAR = DATE_1.split('-')
CONVERT_DATA = f'{YEAR}-{MONTH}-{DAY}'
print(CONVERT_DATA)

DATE_OBJ = datetime.date(int(YEAR), int(MONTH), int(DAY))
DAYS = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
WEEKDAY_NAME = DAYS[DATE_OBJ.weekday()]
print("День недели:", WEEKDAY_NAME)





# Задача 5: Калькулятор налогов
# Условие: Рассчитайте налог по прогрессивной шкале:
#
# Доход ≤ 20 000 → 10%
# 20 000 < доход ≤ 50 000 → 20% на часть превышения
# Доход > 50 000 → 30% на превышение + фиксированный платеж 5000


print('Задание 5')
INCOME = int(input('Введите ваш доход: '))

TAX1 = 0.1
TAX2 = 0.2
TAX3 = 0.3

DIFF_1=20000
DIFF_2=30000

if INCOME <= 20000:
    print (f'Сумма налога {INCOME*TAX1}')
elif 20000 < INCOME <= 50000:
    DIFF = INCOME - 20000
    print(f'Сумма налога {(DIFF_1 * TAX1) + (DIFF * TAX2)}')
else:
    DIFF = INCOME - 50000
    print(f'Сумма налога {(DIFF_1 * TAX1) + (DIFF_2 * TAX2) + (DIFF * TAX3) + 5000}')



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


print('Задание 6')
YEAR = int(input('Введите возрост: '))
TIME_DAY = input('Введите Утро/День: ').lower()

if YEAR >12:
    if TIME_DAY == 'утро':
        print('Комедия')

    elif TIME_DAY == 'вечер':
        print('фантастика, ужасы')

else:
    print('только мультфильмы')




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


print('Задание 7')
YEAR = int(input('Введите ваш возрост: '))
VAGA = int(input('Введите ваш вес: '))
HEIGHT = float(input('Введите ваш рост: '))
SMOKING = input('Курите? Да/Нет: ').lower()

IMT = (VAGA/(HEIGHT*HEIGHT))

if IMT > 30 or SMOKING == 'да' and YEAR > 40:
    print('Риск для здоровья: Высокий!')
else:
    print('Риск для здоровья: Умеренный!')




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


print('Задание 8')
SUMMA = int(input('Введите сумму в рублях: '))
VALUTA  = input('Введите целевую валюту: USD, EUR, CNY: ').lower()
TYPE_OPERACIA = input('Покупка/Продажа: ').lower()

USD_POKUPKA = 90
USD_PRODAJA = 88

EUR_POKUPKA = 100
EUR_PRODAJA = 98

TAX1 = 0.015
TAX2 = 0.01

if VALUTA == 'usd' and TYPE_OPERACIA == 'покупка':
    SUMMA1=SUMMA/USD_POKUPKA
    print(f'Покупка USD {SUMMA1-(SUMMA1*TAX1)}. Комиссия {TAX1*100}%')
elif VALUTA == 'usd' and TYPE_OPERACIA == 'продажа':
    SUMMA1=SUMMA/USD_PRODAJA
    print(f'Продажа USD {SUMMA1}. На руки {SUMMA - (SUMMA * TAX1)} руб. Комиссия {TAX1*100}%')

elif VALUTA == 'eur' and TYPE_OPERACIA == 'покупка':
    SUMMA1=SUMMA/EUR_POKUPKA
    print(f'Покупка USD {SUMMA1-(SUMMA1*TAX2)}. Комиссия {TAX2*100}%')
elif VALUTA == 'eur' and TYPE_OPERACIA == 'продажа':
    SUMMA1=SUMMA/EUR_PRODAJA
    print(f'Продажа USD {SUMMA1}. На руки {SUMMA - (SUMMA * TAX2)} руб. Комиссия {TAX2*100}%')




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


print('Задание 9')
SOTRUDNIK = 'Иванов'
KONTRAGENT = 'Петров'
GUEST = 'Сидоров'
BLACK_LIST = ['Плохиш', 'Злодей']

EMERGENCY = input('Экстренная ситуация? Да/Нет: ').lower()
STATUS = input('Введите Фамилию: ')

if EMERGENCY == 'нет':
    if STATUS == SOTRUDNIK:
        print('Доступ открыт')
    elif STATUS == KONTRAGENT:
        TIME = input('Введите время входа: ')
        TIME_INT = int(TIME.replace(':', '', 1))
        if 900 <= TIME_INT <= 1759:
            print('Доступ открыт')
        else:
            print('Доступ закрыт')

    elif STATUS == GUEST:
        SOPROVOJDENIE = input('Сопровождение имеется? Да/Нет: ').lower()
        if SOPROVOJDENIE == 'да':
            print('Доступ открыт')
        else:
            print('Доступ закрыт')

    if STATUS in BLACK_LIST:
        print('Доступ закрыт')
else:
    print('Доступ открыт')





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


print('Задание 10')
TEMP = int(input('Введите температуру: '))
PRESSURE = int(input('Введите давление: '))
KATALIZATOR = input('Имеется катализатор? Да/Нет: ').lower()

if TEMP < 0 and PRESSURE >100:
    print('Образование льда')
elif  TEMP > 100 and KATALIZATOR == 'да':
    print('Реакция синтеза')
elif TEMP > 200 and PRESSURE >500:
    print('Плазменное состояние')
else:
    print('Стабильное состояние')
