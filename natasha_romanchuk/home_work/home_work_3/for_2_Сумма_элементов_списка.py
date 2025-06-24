# Задача 2
numbers = [2,4,6,8]
sum = 0
for num in numbers:
    sum += num
print(f'Сумма: {sum}')

# Задача 2 ввод списка с клавиатуры
numbers = list(map(int, input('Введите числа через пробел: ').split()))
sum = 0
for num in numbers:
    sum += num
print(f'Сумма: {sum}')

# Задача 2 сумма только четных чисел
numbers = [1,2,3,4,5,6,8]
sum = 0
for num in numbers:
    if num % 2 == 0:
        sum += num
print(f'Сумма четных чисел: {sum}')