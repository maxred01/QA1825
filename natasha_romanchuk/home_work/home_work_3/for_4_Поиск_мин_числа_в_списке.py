#Задача 4 поиск мин числа списка
numbers = [5,3,8,1,9]
min_number = min(numbers)
print(min_number)

#Задача 4 поиск max числа списка
numbers = [5,3,8,1,9]
max_number = max(numbers)
print(max_number)

#Задача 4 индекс минимального элемента
numbers = [5,3,8,1,9]
for index, number in enumerate(numbers):
    if number == min_number:
        print(f'Индекс{index}, номер {number:2d}')
