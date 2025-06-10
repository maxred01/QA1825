# базовый перебор списка

# fruits = ['яблоко', 'банан', 'вишня']
#
# for fruit in fruits:
#     print(f'Наименование {fruit}')
#     print(f'{len(fruit)}')



# перебор с индексом
# позиционирование элементов на сайте
# for index, color in enumerate(['red', 'green', 'blue']):
#     print(f'индекс {index}, цвет {color}')

# Фильтрация элементов
# numbers = [12, 7, 18, 5, 9]
# for num in numbers:
#     if num % 2 == 0:
#         print(f'{num} четные ')
#     else:
#         print(f'{num} нечетные ')

# Вложенный цикл

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f'Вывод всех комбинаций ({i}, {j})')

#Работа со словарями

# person = {'name': 'Jon', 'age': 20, 'city': 'Minsk'}
# for key, value in person.items():
#     print(f'ключ {key.ljust(5)} значение {value}')

# {key.ljust(5)} количество отступов

# Одновременный перебор нескольких списков

# name = ['Jon', 'Max', 'bob']
# ages = [28, 11, 25]
# for name, age in zip(name, ages):
#     print(f'{name} is {age} years old')


# Генератор списка

# squares = [x**2 for x in range(1, 6)]
# print(squares)

# Обработка файлов

# with open('data.txt', 'r') as file:
#     for line_number, line in enumerate(file, 1):
#         print(f'{line_number}, {line.strip()}')

# Обработка вложенных структур
# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# for row in matrix:
#     for cell in row:
#         print(f'{cell:2d}', end=' ')
#     print()

