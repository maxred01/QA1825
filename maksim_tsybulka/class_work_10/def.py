def name(name):
    print(f"Имя мое, {name}")

name('Максим')


def calculate_tax(price):
    return price * 0.2

total = calculate_tax(1000) + 1000
print(total)

#
# def process_data(data):
#     cleaned = clean(data)
#     analized = analize(cleaned)
#     return report(analized)

# process_data(1000)


def func1(num):
    return num * 1000


def func2(num):
    return num / 10


def func3(num):
    peremennay1 = func1(num)
    peremennay2 = func2(peremennay1)
    print(peremennay2)


func3(1000)




# def name():
#     return input()
#
# def second_name():
#     return input()
#
# def sumdef():
#     results1 = name()
#     results2 = second_name()
#     print(f'Привет: меня звать {results1} {results2}')
#
# sumdef()
#
#


import math
import random

print(math.sqrt(25))
print(math.pi)
print(math.factorial(5))
print(math.log(1))
print(math.sin(60))


print(random.randint(1, 10))
print(random.choice(['a', 'b', 'c']))
results = [1,2,3]
random.shuffle(results)
print(results)


# def имя_функции(аргумент):
#     """Документация (описание функции)"""
#     тело_функции
#     return результат


# def power(base, exponent):
#     return base ** exponent
#
# power(2, 3)
#
# power(exponent=3, base=2)
#
# def power_2(base, exponent=2):
#     return base ** exponent
#
# power_2(3)
#
# def min_max(numbers):
#     return min(numbers), max(numbers)
#
# min_val, max_val = min_max([1,2,3])



from datetime import datetime
now = datetime.now()
print(now.strftime('%d, %m ,%Y'))
now_h = datetime.now().minute
print(now_h)

#
# import requests
# respons = requests.get('https://hoster.by')
# print(respons.status_code)
