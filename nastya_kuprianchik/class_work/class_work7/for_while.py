#базовый перебор списка
fruits = ['яблоко', 'банан','вишня']

for fruit in fruits:
    print(f'Наименование {fruits}')
    print(f'{len(fruit)}')

#перебор с индексом
for index, color in enumerate(['red', 'blue', 'black']):
    print(f'индекс {index}, цвет {color}')



#фильтрация с элементами
numbers = [12, 7, 18, 5, 9]
for num in numbers:
    if num % 2 == 0:
        print(f'{num} четное')
    else:
        print(f'{num} нечетно')


#вложенный цикл
for i in range(1, 4):
    for j in range(1, 4):
        print(f'Вывод всех комбинаций ({i}, {j})')


#работа со словорем
person = {'name':'Jon', 'age':20, 'city':'Minsk'}
for key, value in person.items():
    print(f'ключ {key.ljust(10)} значение {value}')

#одновремк=енный перебор нескольких списков
names = ['jon', 'max', 'bob']
ages = [28, 11, 25]
for name, age in zip(names, ages):
    print(f'{name} is {age} years old')


#генерация списка
squares = [x**2 for x in range(1, 6)]
print(squares)


#обработка файлов
#with open ('data.txt', '') as file:
   # for line_number, line in enumerate(file, 1):
  #      print(f'{line_number}, {line.strip()}')



#обработка вложенных структур
matrix = [[1,2,3], [4,5,6], [7,8,9]]
for row in matrix:#строки
    for cell in row:#столбцы
        print(f'{cell:2d}', end=' ')
print()


#