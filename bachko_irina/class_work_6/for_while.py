# конструкция для повторения данных
# определенное кол-во раз
#
# for _ in range(8):
#     print('Привет')

# итерация число рпоходов в цикле

# words = ['яблоко', 'банан','вишня']
#
# for word in words:
#      print(word)

# while условие:
#     тело_цикла

# count = 0
# while count < 3:
#     print(f'Счет {count}')
#     count += 1

# while True:
#     print('Бесконечно ...')

# синтаксис
#
# for элемент in последовательность:
#         тело_цикла
#
# for char in 'Pyton':
#     print(char)
#
# for num in range(1, 4):
#     print(num * 10)

# for num in range(10):
#     if num == 5:
#         break
#     print(num)
#     print(num, 'break')

# for num in range(3):
#     if num == 1:
#         continue
#     print(num)


# for num in range(3):
#     print(num)
# else:
#     print('Готово')
#
# схему нужно знать, цикл уметь построить

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
#     num = int(input('след. число '))
# print(f'Итого {total}')

# names = ['анна', 'мария','петр']
# for name in names:
#     if name == 'петр':
#         print('найден')
#         break

# x = float(input('Сколько киллометров пробежал в первый день: '))
# y = float(input('Сколько киллометров хочет пробежать: '))
# day = 1
# curent = x
#
# while curent < y:
#     day += 1
#     curent *= 1.1
#     print(day)


x = int(input('сумма вклада: '))
p = int(input('проценты по вкладу: '))
y = int(input('капитализация вклада: '))

years = 0
curent = x

while curent < y:
    years += 1
    result = curent * p / 100
    curent += result
    curent = int(result)
    print(years)