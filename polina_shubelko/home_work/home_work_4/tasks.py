# Задача 1: Вывод чисел от 1 до N

N = int(input('Введите число N (больше 0): '))

if N > 0:
    for i in range(1, N + 1):
        print(i)
else:
    print('Число должно быть больше 0.')

N = int(input('Введите число N (больше 0): '))

if N > 0:
    for i in range(N, 0, -1):
        print(i)
else:
    print('Число должно быть больше 0.')

# Задача 2: Сумма элементов списка

numbers = list(map(int, input('Введите числа: ').split()))

total_sum = 0

for num in numbers:
    total_sum += num
print('Сумма всех элементов:', total_sum)

numbers = list(map(int, input('Введите числа: ').split()))

even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
print('Сумма чётных элементов:', even_sum)

# Задача 3: Подсчёт букв в строке

text = input('Введите строку: ').lower()
letter = input('Введите букву для подсчёта: ').lower()

count = 0

for char in text:
    if char == letter:
        count += 1
print(f'Буква {letter} встречается {count} раз(а).')

total_chars = len(text)
if total_chars > 0:
    percentage = (count / total_chars) * 100
    print(f'Это составляет {percentage:.2f}% от всей строки.')
else:
    print('Строка пустая.')

# Задача 4: Поиск минимального числа в списке

numbers = list(map(int, input('Введите числа: ').split()))

min_num = numbers[0]
for num in numbers:
    if num < min_num:
        min_num = num
print(min_num)

max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(max_num)

numbers = list(map(int, input('Введите числа: ').split()))

min_num = numbers[0]
min_index = 0

for index, num in enumerate(numbers):
    if num < min_num:
        min_num = num
        min_index = index
print(f'Минимальное число: {min_num}')
print(f'Индекс минимального числа: {min_index}')

# Задача 5: Вывод таблицы умножения

N = int(input('Введите число N: '))
for i in range(1, 11):
    print(f"{N:2} * {i:2} = {N * i:3}")

# Задача 1: Угадай число

import random

secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input('Угадай число (1-10): '))
    attempts += 1

    if guess == secret_number:
        print('Угадал!')
        print(f'Количество попыток: {attempts}')
        break
    elif guess < secret_number:
        print('Нет! Попробуй ещё: больше')
    else:
        print('Нет! Попробуй ещё: меньше')

# Задача 2: Сумма чисел до 0

total = 0
count = 0

while True:
   num = int(input('Введите числа: '))
   if num == 0:
       break
   total += num
   count += 1
print(total)

if count > 0:
    average = total / count
    print(f'Среднее арифметическое: {average}')

# Задача 3: Проверка пароля

correct_password = "qwerty123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    password = input('Введите пароль: ')
    attempts += 1
    if password == correct_password:
        print('Доступ разрешён!')
        break
    else:
        print('Неверно! Попробуй ещё.')
else:
    print('Доступ заблокирован. Попытки исчерпаны.')

# Задача 4: Обратный отсчёт

import time
import winsound

N = int(input('Введите число N: '))

for i in range(N, 0, -1):
    print(i)
    winsound.Beep(1000, 500)
    time.sleep(1)

print('Старт!')

import time

minutes = int(input('Введите минуты: '))
seconds = int(input('Введите секунды: '))

total_seconds = minutes * 60 + seconds

while total_seconds > 0:
    mins = total_seconds // 60
    secs = total_seconds % 60
    print(f'{mins:02d}:{secs:02d}')
    time.sleep(1)
    total_seconds -= 1

print('Старт!')

# Задача 5: Калькулятор до выхода

history = []

print("Калькулятор. Введите 'exit' для завершения.")

while True:
    operation = input("Введите операцию (+, -, *, /): ").strip()
    if operation.lower() == 'exit':
        print("Завершение.")
        break
    elif operation not in ['+', '-', '*', '/']:
        print("Некорректная операция. Попробуйте снова.")
        continue

    num1 = float(input("Введите число: "))
    num2 = float(input("Введите число: "))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Ошибка: деление на ноль.")
            continue
        result = num1 / num2

    print(f"Результат: {result}")

    history.append(f"{num1} {operation} {num2} = {result}")

print("\nИстория операций:")
for record in history:
    print(record)
