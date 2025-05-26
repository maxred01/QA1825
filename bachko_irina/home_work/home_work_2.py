#Задача 1

X = int (input('Введите число X: '))

print(f'Число: {X}')

#Задача 2

A = int (input('Введите число A:'))
B = int (input('Введите число B:'))

print(A + B)

#Задача 3

numbers = [5, 10, 15]
numbers_tuple = tuple(numbers)

print (numbers_tuple)

#Задача 4

A = input('Введите слово: ')
B = input('Введите слово: ')

print (f'{A} {B}')

#Задача 5

A = int(input('Введите число: '))

print(A * 2)

#Задача 6

fruits = ['apple', 'banana', 'cherry']
fruits_tuple = tuple(fruits)

print(len(fruits_tuple))

#Задача 7

A = 3.14
I = int(A)

print(I)

#Задача 8

NAME_USER = input('Введите имя:')
AGE_USER = input('Введите возраст:')

print(f' Имя: {NAME_USER} , Возраст: {AGE_USER} ')

#Задача 9

TEXT = "pyton"

print (list(TEXT))

#Задача 10

NUMBERS = [1,2,3]
str_nambers = [str(n) for n in NUMBERS]
result = ''.join(str_nambers)

print (result)

#Задача 11

TEXT = "Привет мир Pyton"
WORDS = TEXT.split()

print (len(WORDS))

#Задача 12

WORDS = ["Hello", "word", "!"]
result = ' '.join(WORDS)

print (result)

