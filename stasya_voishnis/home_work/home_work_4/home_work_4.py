# #FOR
# #Задача 1
# #вариант 1
# n = int(input('Введите число больше нуля: '))
# if n > 0:
#     for i in range(1, n+1):
#         print(f'{i:2d}', end=' ')
# else:
#     print('Введено отрицательное число')
#
# #вариант 2
# n = int(input('Введите число больше нуля: '))
# if n > 0:
#     for i in range(n, 0, -1):
#         print(f'{i:2d}', end=' ')
# else:
#     print('Введено отрицательное число')
#
# #Задача 2
# #вавриант 1
# numbers = [x for x in range(1, 9)]
# sum = 0
# for number in numbers:
#     sum +=number
# print(f'Сумма: {sum}')
#
# #вариант 2
# numbers = list(map(int, input('Введите несколько чисел через пробел: ').split()))
# sum = 0
# for number in numbers:
#     sum +=number
# print(f'Сумма: {sum}')
#
# #вариант 3
# numbers = [x for x in range(1, 11)]
# sum = 0
# for number in numbers:
#     if number % 2 == 0:
#        sum += number
# print(f'Сумма четных чисел: {sum}')
#
# #Задача 3
# #вариант 1
# word= 'Abracadabra'.lower()
# count = 0
# for letter in word:
#     if letter =='a':
#         count += 1
# print(count)
#
# #вариант 2
# word = input('Введите любое слово: ').lower()
# letters = input('Введите букву какую требуется подсчитать: ').lower()
# count = 0
# len_word = len(word)
# for letter in word:
#     if letter ==letters:
#         count += 1
#         percentage = (count / len_word) * 100
# print(f"Буква '{letters}' встречается {count} раз(а).")
# print(f"Это составляет {percentage:.2f}% от всех букв.")
#
# #Задача 4
# #вариант 1
# numbers = [5, 3, 8, 1, 9]
# min_num = numbers[0]
# for num in numbers:
#     if num < min_num:
#         min_number = num
# print(min_num)
#
# #вариант2
# numbers = [5, 3, 8, 1, 9]
# max_num = numbers[0]
# for num in numbers:
#     if num > max_num:
#         max_num = num
# print(max_num)
#
# #вариант 3
# numbers = [5, 3, 8, 1, 9]
# min_num = numbers[0]
# for num in numbers:
#     if num < min_num:
#         min_number = num
# for index, number in enumerate(numbers):
#     if number == min_num:
#         print(f'Индекс {index}, номер {number:2d}')
#
# #Задача 5
# #вариант 1
# num = int(input('Введите число: '))
# for z in range(1, 11):
#     result = num * z
#     print(f'{num} * {z} = {result}')
#
# #WHILE
# #Задача 1
# #вариант 1
# n = int(input('Угадайте число от 1 до 10: '))
# numbers = 9
# while n != 9:
#     n = int(input('Нет! Попробуй ещё: '))
# print('Угадал!')
#
# # вариант 2
# n = int(input('Угадайте число от 1 до 10: '))
# numbers = 9
# count = 1
# while n != 9:
#     count +=1
#     n = int(input(f'Нет! Попробуй ещё. Попытка {count}: '))
# print(f'Угадал! С {count} попытки.')
#
# #вариант 3
# n = int(input('Угадайте число от 1 до 10: '))
# numbers = 9
# while n != 9:
#     if n < numbers:
#         n = int(input('Нет! Число должно быть больше. Попробуй ещё: '))
#     else:
#         n = int(input('Нет! Число должно быть меньше. Попробуй ещё: '))
# print('Угадал!')
#
# #Задача 2
# #вариант 1
# num = int(input('Введите число: '))
# sum = num
# while num != 0:
#     num = int(input('Введите ещё одно число: '))
#     sum += num
# print(f'Cумма введеных чисел {sum}')
#
# #вариант 2
# num = int(input('Введите число: '))
# sum = num
# count = 1
# while num != 0:
#     num = int(input('Введите ещё одно число: '))
#     sum += num
#     count += 1
# print(f'Cумма введеных чисел {sum}, всего введено чисел {count}')
#
# #вариант 3
# num = int(input('Введите число: '))
# sum = num
# count = 1
# mean = 0
# while num != 0:
#     num = int(input('Введите ещё одно число: '))
#     sum += num
#     count += 1
# mean = sum/count
# # print(f' среднее арифметическое введенных чисел {mean}')
#
# #Задача 3
# #вариант 1
# pas = input('Введите пароль: ')
# password = 'qwerty123'
# count = 1
# while pas != password:
#      pas = input('Неверно! Попробуй ещё: ')
# print('Доступ разрешён!')
#
# #вариант 2
# pas = input('Введите пароль: ')
# password = 'qwerty123'
# count = 1
# while pas != password:
#     if count < 5:
#        pas = input('Неверно! Попробуй ещё: ')
#        count +=1
#     else:
#         print('Превышен лимит попыток')
#         break
# else:
#     print('Доступ разрешён!')
#
# #Задача 4
# import time
#
# count = int(input('Введите число: '))
# while count >0:
#     time.sleep(1)
#     print(count)
#     count -= 1
# print('Старт!')

#Задача 5
while True:
    operation = input("Операция (+, -, *, /, exit): ")

    if operation == "exit":
        print("Завершение.")
        break

    n_1 = float(input("Введите первое число: "))
    n_2 = float(input("Введите второе число: "))

    if operation == "+":
        print(f'Результат: {n_1 + n_2}')
    elif operation == "-":
        print(f'Результат: {n_1-n_2}')
    elif operation == "*":
        print(f'Результат:{n_1*n_2}')
    elif operation == "/":
        if b != 0:
            print(f'Результат:{n_1/n_2}')
        else:
            print("Деление на ноль невозможно")
    else:
        print("Неизвестная операция")