def name (name):
    print (f"Имя мое, {name}")

name ('Полина')


def calculate_tax (price):
    return price * 0.2

total = calculate_tax (1000) + 1000
print (total)


# def process_data (data):
#     cleaned = clean (data)
#     analized = analize (cleaned)
#     return report (analized)
#
# process_data (1000)


def number (number):
    return number * 1000

result = number (5)
print (result)


def func1 (num):
    return num * 1000

def func2 (num):
    return num / 10

def func3 (num):
    peremennay1 = func1(num)
    peremennay2 = func2(peremennay1)
    print (peremennay2)

func3 (1)


def name (my_name):
    return my_name

def second_name (my_second_name):
    return my_second_name

def sumdef (my_name, my_second_name):
    results1 = name (my_name)
    results2 = second_name (my_second_name)
    print (f"Привет, меня зовут: {results1} {results2}")

sumdef ('Полина', "Шубелько")


import math
import random

print(math.sqrt(25))
print(math.pi)
print(math.factorial(5))
print(math.sin(60))
print(math.log(1))

print(random.randint(1, 10))
print(random.choice(['a', 'b', 'c', 'd', 'e']))

my_list = ['a', 'b', 'c', 'd', 'e']
random.shuffle(my_list)
print(my_list)


# def имя_функции (аргумент):
#     "Документация (описание функции)"
#     тело_функции
#     return результат (не обязателен)

def power(base, exponent):
    return base ** exponent

print(power(2, 3)) #позиционный подход
print(power(base=2, exponent=3)) #именнованный подход

def power_2(base, exponent=3):
    return base ** exponent

print(power_2(2))

def min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = min_max([1,2,3])
print(min_val)
print(max_val)

# import requests
# response = requests.get('https://hoster.by')
# print(response.status_code)

from datetime import datetime
now = datetime.now()
print(now.strftime("%d. %m. %Y"))
now_h = datetime.now().minute
print(now_h)

def arseniy ():
    """Эта функция умеет говорить привет мир!"""
    print ("Привет мир!")

arseniy()

def add_number(a: int, b: int) -> int:
    """Складывать два числа и возвращать результат"""
    results = a + b
    return results

# def test_add():
#     assert add_number(2, 3) == 5
#
#     assert add_number(-1, 1) == 0
#
# def create_user(name: str, role: str = "tester") -> dict:
#     return {'name': name, 'role': role}
#
# def test_user():
#     assert create_user("Alice") == {"name": "Alice", "role": "tester"}
#     assert create_user("Bob", "developer") == {"name": "Bob", "role": "developer"}
#
# def anlizye_text(text: str) -> tuple:
#     length = len(text)
#     words = len(text.split())
#     return length, words
#
# def test_text():
#     text = "Арсений учись!"
#     char_count, word_count = anlizye_text(text)
#     assert char_count == 14
#     assert word_count == 2
#
# is_even = lambda x: x % 2 == 0
#
# def test_even_check():
#     assert is_even(4) is True
#     assert is_even(5) is False

def three_args(*, var1=None, var2=None, var3=None):
    args = []
    if var1 is not None:
        args.append(f"var1={var1}")
    if var2 is not None:
        args.append(f"var2={var2}")
    if var3 is not None:
        args.append(f"var3={var3}")
    if args:
        print('Переданы аргументы', ', '.join(args))
    else:
        print('Нет аргументов отличных от None')

three_args (var1=21)
three_args (var1='Python', var3=3)
three_args (var1='Python', var2=3, var3=9)

sum_numbers = lambda a,b: a+b
result = sum_numbers (3,5)
print(result)

