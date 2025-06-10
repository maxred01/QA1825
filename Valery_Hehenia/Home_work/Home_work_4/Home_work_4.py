

              #.............................FOR............................



# Задача 1: Вывод чисел от 1 до N
# Условие:
# Напишите программу, которая выводит все числа от 1 до N (включительно), где N вводит пользователь
# Комбинации:
#
# Можно добавить проверку, что N > 0
# Можно выводить числа в обратном порядке (range(n, 0, -1))


print('Задание 1 for')

N=int(input('N = '))
if N > 0:
    for i in range(N):
        print(i+1, end=' ')

    print('')

    for i in range(N,0,-1):
        print(i, end=' ')
else:
    print('Введите положительное число!')




# Задача 2: Сумма элементов списка
# Условие:
# Дан список чисел. Найти сумму всех элементов
#
# Комбинации:
# Можно вводить список с клавиатуры (numbers = list(map(int, input().split())))
# Можно искать сумму только чётных чисел (if num % 2 == 0)


print('Задание 2 for')

LIST = list(map(int,input('Введите числа через пробел: ').split()))
print(LIST)
a=0;
b=0;
for i in LIST:
    a = a + i

    if i % 2 != 0:
        b = b + i

print(f'Сумма всех чисел = {a}')
print(f'Сумма нечетных чисел = {b}')




# Задача 3: Подсчёт букв в строке
# Условие:
# Дана строка. Посчитайте, сколько раз в ней встречается буква "a" (регистр не учитывать)
#
# Комбинации:
# Можно считать любую букву (запросить у пользователя)
# Можно вывести процентное соотношение букв


print('Задание 3 for')

STRING = input('Введите строку: ').lower()
SEARCH_CHAR = input('Введите искомую букву: ').lower()
COURTER=0

for char in STRING:
    if char in SEARCH_CHAR == SEARCH_CHAR:
        COURTER+=1

TOTAL_CHARS = len(STRING)
PERC = (COURTER/TOTAL_CHARS)*100

print(f'Количество совпадений: {COURTER}')
print(f'{PERC:.2f}%' )




# Задача 4: Поиск минимального числа в списке
# Условие:
# Дан список чисел. Найти минимальное число
#
# Комбинации:
# Можно искать максимум (if num > max_num)
# Можно вывести индекс минимального элемента (enumerate)


print('Задание 4 for')

NUMBERS = list(map(int,input('Введите числа через пробел: ').split()))
MIN=float('inf')
MAX=0
INDEX_MIN=0
INDEX_MAX=0

for i in NUMBERS:
    if i<MIN:
        MIN=i

        INDEX_MIN=NUMBERS.index(i)

    if i>MAX:
        MAX=i

        INDEX_MAX=NUMBERS.index(i)

print(f'Минимальное число {MIN}, индекс {INDEX_MIN}')
print(f'Максимальное число {MAX}, индекс {INDEX_MAX}')




# Задача 5: Вывод таблицы умножения
# Условие:
# Вывести таблицу умножения для числа N (от 1 до 10)
#
# Комбинации:
# Можно сделать вложенный цикл для всей таблицы умножения
# Можно добавить форматирование (print(f"{n:2} * {i:2} = {n*i:3}"))


print('Задание 5 for')

NUMBER = int(input('Введите число: '))

print('')
print(f'Таблица умножения для числа: {NUMBER} ')

for i in range(1, 11):
    print(f"{NUMBER:2} * {i:2} = {NUMBER * i:3}")

print('')
print('Вся таблица умножения')

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i:2} x {j:2} = {i * j:3}")




          # .............................WHILE............................



# Задача 1: Угадай число
# Условие:
# Программа загадывает число от 1 до 10. Пользователь угадывает, пока не введёт правильное число
#
# Комбинации:
#
# Можно добавить счётчик попыток
# Можно давать подсказки (больше/меньше)


print('Задание 1 While')

import random
NUMBER = int(input('Угадай число (1-10): '))
RANDOM_NUMBER = random.randint(1,10)
COUNTER = 0

while RANDOM_NUMBER != NUMBER:

    if RANDOM_NUMBER != NUMBER:

        if NUMBER > RANDOM_NUMBER:
            print('Меньше')
        elif NUMBER < RANDOM_NUMBER:
            print('Больше')

        NUMBER = int(input('Нет! Попробуй ещё: '))
        COUNTER += 1

print()
print('Угадал!')
print(f'Количество попыток: {COUNTER}')




# Задача 2: Сумма чисел до 0
# Условие:
# Пользователь вводит числа, пока не введёт 0. Посчитать сумму всех введённых чисел
#
# Комбинации:
# Можно считать количество чисел (count += 1)
# Можно искать среднее арифметическое


print('Задание 2 While')

NUMBER_1=int(input('Введите число: '))
SUM=0
COUNTER=0

while NUMBER_1 != 0:
    SUM += NUMBER_1
    NUMBER_1 = int(input('Введите число: '))
    COUNTER+=1
print()
print(f'Сумма чисел: {SUM}')
print(f'Количество чисел: {COUNTER}')
print(f'Среднее значение чисел: {SUM/COUNTER}')




# Задача 3: Проверка пароля
# Условие:
# Пользователь вводит пароль, пока не введёт правильный (qwerty123)
#
# Комбинации:
# Можно ограничить число попыток (attempts += 1)
# Можно скрывать ввод (getpass.getpass())


print('Задание 3 While')
print()

PASSWORD = 'qwerty123'
COUNTER = 2

print(f'Осталось попыток: {COUNTER+1}')
INPUT_PASSWORD = input('Введите пароль: ')

while COUNTER > 0:

    if INPUT_PASSWORD == PASSWORD:
        print('Доступ разрешён!')
        break
    else:
        COUNTER -= 1
        print(f'Неверно! Осталось попыток: {COUNTER+1}')
        INPUT_PASSWORD = input('Введите пароль: ')

        if COUNTER == 0:
            print('Попытки закончились!')




# Задача 4: Обратный отсчёт
# Условие:
# Вывести числа от N до 1 с задержкой в 1 секунду
#
# Комбинации:
# Можно добавить звук (winsound.Beep)
# Можно сделать таймер с минутами и секундами


print('Задание 4 While')
print()
import winsound
import time
NUMBER = int(input('Введите число: '))

while NUMBER > 0:
    NUMBER-=1
    print(NUMBER+1)
    winsound.Beep(1000, 100)
    time.sleep(1)

winsound.Beep(2000, 500)
print('Старт!')




# Задача 5: Калькулятор до выхода
# Условие:
# Программа принимает числа и операцию (+, -, *, /), пока пользователь не введёт exit
#
# Комбинации:
# Можно добавить возведение в степень
# Можно сохранять историю операций


print('Задание 5 While')
print()

A = int(input('Число А: '))
B = int(input('Число B: '))

while True:

       OPERATION = input('Введите операцию (+, -, *, /,^, exit): ')

       if OPERATION == 'exit':
           break

       if OPERATION == '+':
           RESULT = A + B
       elif OPERATION == '-':
           RESULT = A - B
       elif OPERATION == '*':
           RESULT = A * B
       elif OPERATION == '/':
           if B != 0:
               RESULT = A / B
           else:
               print('На 0 делить нельзя')
               continue

       elif OPERATION == '^':
           RESULT = A ** B

       else:
           print('Неизвестная операция!')
           continue

       print('Результат:', RESULT)
       with open("history.txt", "a") as file:
            file.write(f"{A} {OPERATION} {B} = {RESULT}\n")

print('Завершение')