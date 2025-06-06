# Пример 1
for _ in range(8):
    print('Привет')

# Пример 2
worlds = ['яблоко', 'банан','вишня']

for world in worlds:
    print(world)

# Пример 3
count = 0
while count < 3:
    print(f'Счет {count}')
    count += 1

# Пример 4
while True:
    print('Бесконечный...')

# Пример 5
for char in 'Python': # выводит каждую букву построчно
    print(char)

# Пример 6
for num in range(1, 4):
    print(num * 10)

# Пример 7
for num in range(10):
    if num == 5:
        break
    print(num, 'break')

# Пример 8
for num in range(5):
    if num == 1: # пропустили значение как оно выполнилось
        continue
    print(num,)

#Пример 9
for num in range(3):
        print(num)
else:
    print('Готово') # выполнится всегда

#Пример 10
total = 0 # глобальная переменная
for i in range(3):
    x = i * 2 # локальная переменная
    total +=x
print(total)
print(x)

# Пример 11
total = 0
num = int(input('Введите число: '))
while num != 0:
    total += num
    num = int(input('след. число'))
print(f'Итого {total}')

#Пример 12
names = ['анна', 'мария', 'петр']
for name in  names:
    if name == 'петр':
        print('Найден')
        break



