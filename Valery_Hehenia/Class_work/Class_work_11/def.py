from distutils.command.clean import clean


def name(name, familia):
    print (f'Имя мое, {name},{familia}')

name('Valery','Hehenia')

def calcutate_tax(price):
    return price * 0.2

total = calcutate_tax(1000)+1000
print(total)


def process_data(data):
    cleaned = clean(data)
    analized = analize(cleaned)
    return report(analized)



def mult(number):
    return number * 1000


def dele(number_1):
    return  number_1 /10



def logic(num):
    p1=mult(num)
    p2=dele(p1)
    print(p2)

logic(1)

def name(name):
    return name

def familia(familia):
    return familia

def fio(name,familia):
    print(f'Привет, меня зовут {name} {familia}!')

fio(name('Valery'),familia('Hehenia'))


import math
import random

print(math.sqrt(25))
print(math.pi)
print(math.factorial(5))
print(math.log(1))

print(random.randrange(1, 10))
print(random.choice(['a', 'b', 'c']))
ran = ['a', 'b', 'c']
random.shuffle(ran)
print(ran)

def name_fukc(argumenti):
    """Документация (аннотация функции) описание"""
    telo_funkcii
    return rezultat

def power(base, exponent):
    return base ** exponent

power(2,3) #пазиционное
power(exponent=3,base=2) #именованное

def power_2(base, exponent=2):
    return base ** exponent

power_2(2)


from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))


import requests
response = requests.get("https://hoster.by")
print(response.status_code)

