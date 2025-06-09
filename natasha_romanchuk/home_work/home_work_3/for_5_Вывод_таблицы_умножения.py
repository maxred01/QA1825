#Задача 5 вывод таблицы умножения
x = int(input('Введи число:'))
for i in range(1,11):
    result = x * i
    print(f'{x} x {i} = {result}')