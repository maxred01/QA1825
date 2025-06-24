# базовый перебор списка
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f'Items {fruit}')
    print(f'{len(fruit)}')

# Перебор с индексом
for index, color in enumerate(['red', 'green', 'blue']):
    print(f'index {index}, color {color}')

# Фильтрация элементов
numbers = [12, 7, 18, 5, 9]
for num in numbers:
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')

# Вложенный цикл
for i in range(1, 4):
    for j in range(1, 4):
        print(f'Show all combinations ({i}, {j})')

# Работа со словарем
person = {'name': 'John', 'age': 20, 'city': 'London'}
for key, value in person.items():
    print(f'key {key.ljust(5)} value {value}')

# Одновременный перебор нескольких списков
names = ['John', 'Max', 'Bob']
ages = [28, 11, 25]
for name, age in zip(names, ages):
    print(f'{name} is {age} years old')

# Генератор списка
squares = [x**2 for x in range(1, 6)]
print(squares)

# # Обработка файлов
# with open('data.txt', 'r') as file:
#     for line_number, line in enumerate(file, 1):
#         print(f'{line_number}, {line.strip()}')

# Обработка вложенных структур
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for cell in row:
        print(f'{cell:2d}', end=' ')
    print()
