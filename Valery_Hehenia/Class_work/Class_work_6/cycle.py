for _ in range(3):
    print('Привет')


words = ['яблоко', 'банан', 'вишня']
for word in words:
    print(word)




# while условие:
#     тело_цикла


count =0
while count <3:
    print(f'счет {count}')
    count+=1

for char in 'Python':
    print(char)


for num in range(1,101):
    print(num*10)


for num in range(10):
    if num == 5:
        break
    print(num)\



for num in range(3):
    if num == 1:
        continue
    print(num)
    print('break')


for num in range(3):
    print(num+1)
else:   # else выполнится всегда только в конце цикла
    print('done')


total = 0
for i in range(3):
    x=i*2
    total+=x
print(total)
print(x)

total = 0
num = int(input('vvedite chislo:'))
while num != 0:
    total += num
    num = int(input('sled. chislo:'))
print(f'Итого {total}')

names = ['Anna', 'Petr', 'Maria']
for name in names:
    if name == 'Petr':
        print('done')
        break


range1 = float(input('1: '))
range2 = float(input('2: '))
proc = 1.1
day=1

distance = range1

while distance <= range2:
    distance*=proc
    day+=1
print(day)


summa = float(input('summa1= '))
summa1 = float(input('summa2= '))
pricent = float(input('proc= '))

dist=0
year=0

while dist < summa1:
    year += 1
    result= (dist*pricent)/100
    dist+=result
    dist=int(dist)

print(year)

#базовый перебор списка
fruits = ['яблоко', 'банана', 'вишня']
for fruit in fruits:
    print(f'Наименовение: {fruit}')
    print(f'{len(fruit)}')

#перебор с индексом
for index, color in enumerate (['red', 'green', 'blue']):
    print(f'индекс{index}, цвет {color}')

#фильтрация элементов
numbers = [12,7,18,5,9]
for num in numbers:
    if num % 2 == 0:
        print(f'{num} четные')
    else:
        print(f'{num} нечетное')

#вложенный цикл
for i in range(1,4):
    for j in range(1,4):
        print(f'вывод всех комбинаций ({i},{j})')

#работа со словарем
#items возвращает пара-ключ, работает только со словарями
person = {'name': 'John', 'age': 20, 'city': 'Minsk'}
for key, value in person.items():
    print(f'key{key.ljust(5)} value{value}')


#одновременный перебор нескольких списков
names = ['john', 'max', 'bob']
ages = [28,11,25]
for name, age in zip (names, ages):
    print(f'{name} is {age} years old')


#генератор списка
squeares = [x**2 for x in range(1,6)]
print(squeares)


#обработка файлов
with open('data.txt', 'r') as file:
    for line_number, line in enumerate(file,1):
        print(f'{line_number}, {line.strip()}')


#Обработка вложеных структур
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    for col in row:
        print(f'{col:2d}', end=' ')
    print()