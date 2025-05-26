X = input ('Введите число:')
X_str = str (X)
print ('Число:', X_str)

A = input ('Введите первое число:')
B = input ('Введите второе число:')
result = int (A) + int (B)
print ('Сумма:', result)

numbers = [5,10,15]
numbers_tuple = tuple (numbers)
print (numbers_tuple)

word1 = input ('Введите первое слово:')
word2 = input ('Введите второе слово:')
result = word1 + ' ' + word2
print (result)

num_str = input ('Введите целое число:')
number = int (num_str)
result = number * 2
print ('Результат:', result)

fruits = ["apple", "banana", "cherry"]
fruits_tuple = tuple (fruits)
print (len (fruits_tuple))

num_str = input ('Введите число с плавающей точкой:')
num_float = float (num_str)
num_float_int = int (num_float)
print (num_float_int)

name = input ('Введите имя:')
age = input ('Введите возраст:')
print (f'Имя: {name}, Возраст: {age}')

str1 = 'Python'
str1_list = list (str1)
print (str1_list)

num_tuple = (1,2,3)
num_tuple_str = ''.join (map (str, num_tuple))
print (num_tuple_str)

words = input ('Введите предложение:')
words_split = words.split ()
print ('Количество слов:', len (words_split))

words = ["Hello", "world", "!"]
words_str = ' '.join (words)
print (words_str)
