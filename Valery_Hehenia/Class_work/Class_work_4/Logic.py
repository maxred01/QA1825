from pycurl import LOGIN_OPTIONS  # elif - >else if
 # if not age -> if !age

# Задание 1: Напишите программу, которая определяет, является ли введенное число четным.

NUMBER = int (input('Введите число: '))
if NUMBER %2 ==0:
    print('Чётное число')
else:
    print('не четное число')

# Задание 2: Условие: Пользователь вводит пароль.
#  Если он совпадает с "qwerty123", выведите "Доступ разрешен", иначе — "Доступ запрещен".

PASSWORD = 'qwerty123'
WRITE_PASSWORD = input('Введите пароль: ')
if PASSWORD == WRITE_PASSWORD:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

# Задание 3: Условие: Напишите программу, которая находит наибольшее из трех чисел.

A=int(input('A='))
B=int(input('B='))
C=int(input('C='))

if A>B and A>C:
    print('A')
elif B>A and B>C:
    print('B')
else:
    print('C')


# Задание 4: Условие: Рассчитайте индекс массы тела (ИМТ) и выведите категорию:
# - ИМТ < 18.5 → "Недостаточный вес"
# - 18.5 ≤ ИМТ < 25 → "Норма"
# - ИМТ ≥ 25 → "Избыточный вес"

ROST = float(input('Введите ваш рост: '))
VAGA = int(input('Введите ваш вес: '))

INDEX = (VAGA/(ROST**2))
if  16 <= INDEX <= 18.5:
    print('Недостаточный вес')
elif 18.5 <= INDEX <= 25:
    print('Норма')
elif 25 <= INDEX <= 30:
    print('Избыточный вес')





# Задание 5: Пользователь вводит логин и пароль.
# Если логин "admin" и пароль "12345", выведите "Успешный вход", иначе — "Ошибка".

LOGIN = 'admin'
PASSWORD = '12345'

LOG = input('Введите логин: ')
PASS= input('Введите пароль: ')

if LOG == LOGIN and PASS == PASSWORD:
        print('успешный вход')
else:
    print('Ошибка')
