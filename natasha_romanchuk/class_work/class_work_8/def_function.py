def name(name):
    print (f"Имя мое, {name}")

name ("Nata")                  # Имя мое, Nata


def calculate_tax (prise):
    print( prise * 0.2)

calculate_tax(1000)            #  200.0


def calculate_tax_1(prise):
    return prise * 0.2

total_tax = calculate_tax_1(1000) + 1000
print(total_tax)                # 1200.0

# Декомпозиция   разбиение на маленькие задачи
# def process_data(data):
#     cleaned = clean(data)
#     analized = analize(cleaned)
#     return report(analized)
#
# processed_data = process_data(1000)


# Встроенные функции len ...

def func1 (num):
    return num * 1000

def func2(num):
    return num / 10

def func3(num):
    peremennaya_1 = func1(num)
    peremennaya_2 = func2(peremennaya_1)
    print(peremennaya_2)

func3(300)


# имя фам  меня зовут имя и фам

def name(my_name):
    return my_name
def lastname(my_lastname):
    return my_lastname
def text(my_name, my_lastname):
    text1 = name(my_name)
    text2 = lastname(my_lastname)
    print(f' Меня зовут {text1} {text2}')

text ('Nata', 'Romanchuk')



# имя фам  меня зовут имя и фам через input
# def name():
#     return input()
# def lastname():
#     return input()
# def text():
#     text1 = name()
#     text2 = lastname()
#     print(f' Меня зовут {text1} {text2}')
#
# text()

# Функции библиотек    docs.python.org

import math
print(math.sqrt(25))   # квадратный корень
print(math.pi)
print(math.factorial(5))
print(math.log(1))
print(math.sin(60))

import random
print(random.randint(1, 10))
print(random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']))
mylist = [1,2,3]
random.shuffle(mylist)   # Перемешать значения
print(mylist)


def func_name(argument):
    """ Надо писать описание на каждую функцию"""
    body_function
    return результат

def many_print():
    print('Hello')
    print('Hello')
    print('Hello')
    print('Hello')
many_print()

# Аргумент и возвращаемые значения
def power(base, exponent):
    return base**exponent

power(2, 3)   # позиционный подход

power(base=2, exponent=3)   # именованный


def power_2(base, exponent=2):
    return base**exponent
power_2(3)



def min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = min_max([1,2,3])

print(min_val)
print(max_val)


from datetime import datetime
now = datetime.now()
print(now.strftime("%d,%m,%Y"))
now_h = datetime.now().minute
print(now_h)

import requests
response = requests.get("http://hoster.by")
print(response.status_code)







