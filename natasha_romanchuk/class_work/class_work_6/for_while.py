#print('Hello')

# for _ in range(8):   # range повторяет 8 раз вложенное действие
#     print('Hello')


# words = ['яблоко', 'банан','вишня']
#
# for word in words:
#     print(word)


# while условие:
#     тело_цикла

# count = 0
# while count < 3:
#     print(f'Счет {count}')
#     count +=1                          #0 1 2 столбиком

# while True:
#     print('Бесконечно...')


# for элемент in последовательность:
#     тело_цикла

# for char in 'Python':  #выведет по буквам
#     print(char)
#
#
# for num in range(1,4):  # от 1 до 3 умножит на 10
#     print(num * 10)
#
# for num in range(10):
#     if num == 5:     #прервали действие
#         break
#     print(num)

#
# for num in range(3):
#     if num == 1:      # пропустили 1
#         continue
#     print(num)       # 0  1


# for num in range(3):
#     print(num)           # 0 1 2
# else:
#     print('Готово')     # выполняется всегда последней, после выполнения итерации


# total = 0
# for i in range(3):
#     x = i * 2
#     total += x
# print(total)
# print(x)


# total = 0
# num = int(input('Введите число'))
# while num != 0 :                              # пока не равно 0 складывает числа
#     total += num
#     num = int(input('след число'))
# print(f'Итого {total}')


# names = ['анна','мария','петр']
# for name in names:
#     if name == 'петр':
#         print('найден')
#         break


# x = float(input('Введи расстояние'))
# y = float(input('Введи сколько хочешь пробежать'))
# day = 1
# current = x
#
# while current <  y :
#     day +=1
#     current *=1.1
#     print(day)

#Банковские проценты

# x = int(input('Введи сумму вклада'))
# p = int(input('Введи процент вклада'))
# y = int(input('Желаемая сумму вклада'))
# years = 0
# current = x
# while current < y :
#     years += 1
#     result = current * p / 100
#     current += result
#     current = int(current)
# print(years)