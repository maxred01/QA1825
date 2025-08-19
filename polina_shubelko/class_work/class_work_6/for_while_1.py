print('Привет')
print('Привет')
print('Привет')
print('Привет')
print('Привет')
print('Привет')
print('Привет')
print('Привет')

for _ in range(8):
    print ('Привет') #цикл (итерация - количество проходов в цикле (8))

words = ['яблоко', 'банан', 'вишня']

for word in words:
    print (word)

# цикл while - бесконечный цикл

count = 0
while count < 3:
    print(f'Счет {count}')
    count += 1

while True:
    print('Бесконечно...')

# for элемент in последовательность:
#     тело_цикла
# while условие:
#     тело_цикла

for char in "Python":
    print(char)
for num in range(1, 4):
    print(num * 10)

for num in range(10):
    if num ==5:
        break
    print(num)

for num in range(3):
    if num == 1:
        continue
    print(num)

for num in range(3):
    print(num)
else:
    print('Готово')

total = 0 #глобальая переменная
for i in range(3):
    x = i * 2 #локальная переменная
    total += x
print(total)
print(x)

total = 0
num = int(input("Введите число"))
while num != 0:
    total += num
    num = int(input("Следующее число"))
print(f'Итого {total}')

names = ['анна', 'мария', 'петр']
for name in names:
    if name == 'петр':
        print('Найден')
        break

x = float(input("Кол-во км в первый день"))
y = float(input("Пробег спортсмена"))
day = 1
current = x

while current < y:
    day +=1
    current *= 1.1
    print(day)

x = int(input("Вклад в банке"))
p = int(input("Кол-во процентов"))
y = int(input("Кол-во лет"))
years = 0
current = x
while current < y:
    years += 1
    result = (current * p)/100
    current += result
    current = int(current)
print(years)
