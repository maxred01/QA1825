# def name(name):
#     print(f'Имя мое, {name}')
#
# name('Irina')
#
# def calculate_text(price):
#     return price * 0.2
#
# total = calculate_text(1000) + 1000
# print(total)
#
#
# def process_data(data):
#     cleaned = clean(data)
#     analized = analiz(cleaned)
# #     return report(analized)
#
# process_data(1000)

# def func1(num):
#      return num * 1000
#
# def func2(num):
#     return num / 10
#
# def func3(num):
#      peremennay1 = func1(num)
#      peremennay2 = func2(peremennay1)
#      print(peremennay2)
#
# func3(1000)
#
#
# def name(my_name):
#     return my_name
#
#
# def second_name (my_second_name):
#     return my_second_name
#
#
# def func3(my_name,my_second_name):
#     rez1 = name(my_name)
#     rez2 = second_name(my_second_name)
#     print(f'Привет: {rez1}, {rez2}')
#
# func3("Irina", 'Bachko')
#
# import math
# import random
#
# print(math.sqrt(25))
# print(math.pi)
# print(math.factorial(5))
# print(math.log(1))
# print(math.sin(60))
#
# print(random.randint(1, 10))
# print(random.choice(['a','b','c']))
# mylist = [1,2,3]
# random.shuffle(mylist)
# print(mylist)
#
# def имя_функции(аргумент):
#     """Документация (описание функции)"""
#     тело_функции
#     return результат

# def power(base, exponent):
#     return base ** exponent
#
# power(2, 3)
#
# power(base=2, exponent=3)
# # можно и так
# power(exponent=3, base=2)
#
# def power_2(base, exponent=2):
#     return base ** exponent
#
# power_2(3)

# def min_max(numbers):
#     return min(numbers), max(numbers)
#
# min_val, max_val = min_max([1,2,3])

from datetime import datetime
now = datetime.now()
print(now.strftime('%d, %m, %Y'))
now_h = datetime.now().hour
print(now_h)

# import requests
# respons = request.get('https://hoster.by')
# print(respons.status_code)







