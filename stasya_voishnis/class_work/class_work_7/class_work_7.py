# Базовый перебор списка
from numpy.matrixlib.defmatrix import matrix

fruits = ['яблоко', 'банан', 'вишня']
for fruit in fruits:
    print(f'Наименование {fruit}')
    print(f'{len(fruit)}')

#Перебор с индексом через метод enumerate
for index, color in enumerate(['red', 'green', 'blue']):
    print(f'Индекс {index}, цвет {color}')

# фильтрация элементов
numbers = [12, 7, 18, 5, 9]
for num in numbers:
    if num %2 == 0: # проверка на четность
        print(f'{num} четные')
    else:
        print(f'{num} нечетные')

# Вложенный цикл
for i in  range(1, 4):
    for j in range (1, 4):
        print(f'Вывод всех комбинаций ({i}, {j})')

# Работа со словарями
person = {'name': 'Jon', 'age': 20, 'city': 'Minsk' }
for key, value in person.items():
    print(f'ключ {key.ljust(5)} значение {value}') # ljust - Количество отступов

#  Одновременный перебор нескольких списков
names = ['jpn', 'max', 'bob']
ages = [28, 11, 25]
for name, age in zip (names, ages): # Одновременный перебор нескольких списков
    print(f'{name} is {age} years old')

# генератор списка
squares = [x**2 for x in range(1, 6)]
print(squares)

# Обработка файлов
# with open('data.txt', 'r') as file:
#     for line_number, line in enumerate(file, 1):
#         print(f'{line_number}, {line.strip()}')


# Обработка вложенных структур
matrix = [[1,2,3], [4,5,6], [7,8,9]]
for row in  matrix:
    for cell in row:
        print(f'{cell:2d}', end=' ')
    print()
