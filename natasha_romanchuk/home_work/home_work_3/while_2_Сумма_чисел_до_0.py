#Задача 2 сумма чисел
from statistics import mean

total = 0
number = int(input('Веви число(0 для выхода): '))
while number != 0:
    total += number
    number = int(input('Веви число(0 для выхода): '))
print(f'Сумма : {total}')

#Задача 2 количество чисел
count = 0
number = int(input('Веви число(0 для выхода): '))
while number != 0:
    count += 1
    number = int(input('Веви число(0 для выхода): '))
print(f'Количество введенных чисел : {count}')

#Задача 2 среднее арифметическое чисел
total = 0
count = 0

while True:
    number = int(input('Веви число(0 для выхода): '))
    if number == 0:
        break
    total += number
    count += 1

if count > 0:
    average = total / count
    print(f'Среднее арифметическое : {average}')