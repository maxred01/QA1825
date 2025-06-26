a = [1,2,3]
b = a # Копирование ссылки
b.append(4) # Добавление к массиву числа 4
print(a) # Изменился исходный объект

empty = [] # Пустой список
empty2 = list () # Пустой список

numbers = [1,2,3,4,5,6,7,8,9]
mixed = [10, 'Hello', True, 3.14]

chars = list ("abcde") # ['a', 'b', 'c', 'd', 'e']
nums = list (range(5)) # [0, 1, 2, 3, 4]

squares = [x**2 for x in range(5)] # x**2 - возводит в квадрат
evens = [x for x in range(10) if x % 2 == 0] # x%2==0 - выводит четные
