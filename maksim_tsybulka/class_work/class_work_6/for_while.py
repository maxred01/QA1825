# print('Привет')
# print('Привет')
# print('Привет')
# print('Привет')
# print('Привет')
# print('Привет')
# print('Привет')
# print('Привет')

# for _ in range(8):
#     print('Привет')



# words = ['яблоко', 'банан', 'вишня']
#
# for word in words:
#     print(word)

# while услвоие:
#     тело_цикла

# count = 0
# while count < 3:
#     print(f'Счет {count}')
#     count +=1


# while True:
#     print('Бескончено...')


# for элемент in последовательность:
#     тело_цикла

# for char in 'Python':
#     print(char)
#
# for num in range(1, 4):
#     print(num * 10)

# for num in range(10):
#     if num == 5:
#         break
#     print(num)
#     print(num, 'break')

# for num in range(5):
#     if num == 1:
#         continue
#     print(num)


# for num in range(3):
#     print(num)
# else:
#     print('Готово')

# total = 0
# for i in range(3):
#     x = i * 2
#     total += x
# print(total)
# print(x)


# total = 0
# num = int(input('введите число '))
# while num != 0:
#     total += num
#     num = int(input('слуд. число '))
# print(f'Итого {total}')

# names = ['анна', 'мария', 'петр']
# for name in names:
#     if name == 'петр':
#         print('найден')
#         break
#



# x = float(input())
# y = float(input())
#
# day = 1
# current = x
#
# while current < y:
#     day += 1
#     current *= 1.1
#
# print(day)



# x = int(input())
# p = int(input())
# y = int(input())
#
# years = 0
# current = x
#
# while current < y:
#     years += 1
#     result = current * p / 100
#     current += result
#     current = int(current)
# print(years)



#  Базовый перебор списка
fruits = ['яблоко', 'банана', 'вишня']

for fruit in fruits:
    print(f'Наименование {fruit}')
    print(f'{len(fruit)}')


# Пербор с индексом
for index, color in enumerate(['erd', 'green', 'blue']):
    print(f'индекс{index}, цвет {color}')


# Фильтрация элементов
numbers = [12, 7, 18, 5, 9]
for num in numbers:
    if num % 2 == 0:
        print(f'{num} четные')
    else:
        print(f'{num} нечетные')

# Вложенный цикл
for i in range(1, 4):
    for j in range(1, 4):
        print(f'Вывод всех комбинаций ({i}, {j})')

# Работа со словарем
person = {'name': 'Jon', 'age': 20, 'city': 'Minsk'}
for key, value in person.items():
    print(f'ключ {key.ljust(25)} значение {value}')


# Одновременнй пербор нескольких списков
names = ['jon', 'max', 'bob']
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
matrix = [[1,2,3], [4,5,6], [7,8,9]]
for row in matrix:
    for cell in row:
        print(f'{cell:2d}', end=' ')
    print()



count = 0  # Инициализация счетчика
while count < 5:  # Условие продолжения
    print(f"Count: {count}")
    count += 1  # Критически важное обновление!


valid_input = False
while not valid_input:  # Пока не получим валидный ввод
    user_input = input("Enter yes/no: ")
    if user_input.lower() in ["yes", "no"]:
        valid_input = True  # Выход из цикла
    else:
        print("Invalid input, try again")



data_stream = iter([5, 8, 2, 0, 3, 9, 1])  # Имитация потока
while (value := next(data_stream, None)) is not None:  # Walrus-оператор
    if value == 0:
        print("Terminator found!")
        break
    print(f"Processing: {value}")

