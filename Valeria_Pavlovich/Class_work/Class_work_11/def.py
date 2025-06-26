# def calculate_tax(price):
#     return price * 0.2
#
#
# total = calculate_tax(1000) + 1000
# print(total)
#
# def process_data(data):
#     cleaned = clean(data)
#     analyzed = analyze(cleaned)
#     return report(analyzed)
#
# number = int(input('a: '))
#
#
# def multiply(number):
#     return number * 1000
#
#
# def divide(number):
#     return number / 10
#
#
# def total(number):
#     a = multiply(number)
#     b = divide(a)
#     print(b)
#
#
# total(number)

# fname = input('Name: ')
# surname = input('Surname: ')
#
#
# def name(fname, surname):
#     return f'Your name is {fname} {surname}'
#
#
# print(name(fname, surname))


# def name():
#     return input('Name: ')
#
#
# def second_name():
#     return input('Surname: ')
#
#
# def name_surname():
#     a = name()
#     b = second_name()
#     print(f'Your name is {a} {b}')
#
#
# name_surname()
#
#

# import math
# print(math.sqrt(25))
# print(math.pi)
# print(math.factorial(5))

# import random
# print(random.randint(1, 10))
# print(random.choice(['a', 'b', 'c']))


# def name(abc):
#     """annotation"""
#     body
#     return result

# def power(base, exponent):
#     return base ** exponent
#
# power(2, 3)
# power(base=2, exponent=3)

# def power_2(base, exponent=2):
#     return base ** exponent
# power_2(3)
#
# def min_max(numbers):
#     return min(numbers), max(numbers)
#
# min_val, max_val = min_max([1,2,3])

# from datetime import datetime
# now = datetime.now()
# print(now.strftime('%d, %m, %Y'))

from datetime import datetime
current_datetime = datetime.now()
now_h = datetime.now().hour
print(now_h)