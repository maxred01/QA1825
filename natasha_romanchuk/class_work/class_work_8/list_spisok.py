a =[1,2,3]
b = a      # копирование ссылки
b.append(4)
print(a)  # [1,2,3,4]

empty = []
empty2 = list()
print(empty2)

# С элементами
numbers = [1, 2, 3, 4, 5]
mixed = [10, "hello", True, 3.14]

# Из других коллекций
chars = list("abcde")  # ['a', 'b', 'c', 'd', 'e']
nums = list(range(5))  # [0, 1, 2, 3, 4]

#  ГЕНЕРАТОРЫ СПИСКОВ
# Квадраты чисел
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Четные числа
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Парные элементы
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
# [(1, 3), (1, 4), (2, 3), (2, 4)]

# Базовые операции:
# my_list = [10, 20, 30]

# Индексация (с 0)
print(my_list[0])  # 10

# Срезы [start:stop:step]
print(my_list[1:3])  # [20, 30]
print(my_list[::-1])  # [30, 20, 10] - реверс

# Конкатенация
new_list = my_list + [40, 50]  # [10, 20, 30, 40, 50]

# Повторение
zeros = [0] * 5  # [0, 0, 0, 0, 0]

# Длина списка
print(len(my_list))  # 3

# Основные методы:
# Добавление элементов
lst = [1, 2]
lst.append(3)      # [1, 2, 3] - добавить в конец
lst.insert(0, 0)   # [0, 1, 2, 3] - вставить по индексу
lst.extend([4, 5]) # [0, 1, 2, 3, 4, 5] - объединить списки

# Удаление элементов
last = lst.pop()    # 5, lst=[0, 1, 2, 3, 4] - удалить последний
second = lst.pop(1) # 1, lst=[0, 2, 3, 4] - удалить по индексу
lst.remove(2)       # [0, 3, 4] - удалить первое вхождение
lst.clear()         # [] - очистить список

# Сортировка
nums = [3, 1, 4, 2]
nums.sort()         # [1, 2, 3, 4] - сортировка (изменяет список)
sorted_nums = sorted(nums, reverse=True) # [4, 3, 2, 1] - возвращает новый список

# Реверс
nums.reverse()      # [4, 3, 2, 1] - обратный порядок

# Поиск
index = nums.index(3)  # 1 - индекс первого вхождения
count = nums.count(3)  # 1 - количество вхождений

# Копирование
copy = nums.copy()     # Поверхностная копия

# Проверка наличия элемента:
fruits = ["apple", "banana", "orange"]
print("apple" in fruits)    # True
print("grape" not in fruits) # True

# Поиск элемента
# 1.Линейный поиск:

def linear_search(lst, target):
    for i, item in enumerate(lst):
        if item == target:
            return i
    return -1


# 2.Бинарный поиск(для отсортированных списков):

def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# 3. Использование встроенных методов:

# Индекс первого вхождения
index = lst.index(target)  # ValueError если нет элемента

# Проверка наличия
exists = target in lst


# Особенности списков: ссылки и клонирование
# Проблема:
a = [1, [2, 3]]
b = a.copy()  # Поверхностная копия
b[0] = 10     # Не влияет на a
b[1][0] = 20  # Изменяет вложенный список в a!
print(a)      # [1, [20, 3]]

# Решение: глубокое копирование:
import copy
a = [1, [2, 3]]
b = copy.deepcopy(a)
b[1][0] = 20  # Не влияет на a













numbers = [1,2,3,4,5]
mixed = [10,'hello', True, 3.14]

