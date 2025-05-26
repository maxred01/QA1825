# Задача 1
# Описание: Пользователь вводит число. Преобразуйте его в строку и выведите сообщение: "Число: X", где X — введённое число (в виде строки)
num = int(input('Enter a number: '))
num_str = str(num)
print(f'Number: {num_str}')

# Задача 2
# Описание: Сложите два числа, введённых пользователем. Выведите результат
num_1 = int(input('Enter the first number: '))
num_2 = int(input('Enter the second number: '))
total_sum = num_1 + num_2
print(f'Total: {total_sum}')

# Задача 3
# Описание: Дан список numbers = [5, 10, 15]. Преобразуйте его в кортеж и выведите на экран
numbers = [5, 10, 15]
numbers_tuple = tuple(numbers)
print(numbers_tuple)

# Задача 4
# Описание: Пользователь вводит два слова. Объедините их через пробел и выведите
word_1 = input('Enter the first word: ')
word_2 = input('Enter the second word: ')
print(word_1, word_2)

# Задача 5
# Описание: Пользователь вводит строку, которая является целым числом (например, "123"). Преобразуйте её в целое число и выведите результат умножения на 2
num_string = input('Enter a number: ')
num_integer = int(num_string)
multiple = num_integer*2
print(f'Total: {multiple}')

# Задача 6
# Описание: Создайте кортеж из списка fruits = ["apple", "banana", "cherry"] и выведите его длину
fruits = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits)
print(len(fruits_tuple))

# Задача 7
# Описание: Пользователь вводит число с плавающей точкой (например, 3.14). Преобразуйте его в целое число (отбросив дробную часть) и выведите
num_fl = float(input('Enter a floating-point number: '))
num_new = int(num_fl)
print(num_new)

# Задача 8
# Описание: Используя input(), получите имя и возраст пользователя. Выведите сообщение: "Имя: [имя], Возраст: [возраст]"
name = input('Enter your name: ')
age = int(input('Enter your age: '))
print(f'Name: {name}, Age: {age}')

# Задача 9
# Описание: Преобразуйте строку "python" в список символов и выведите этот список
word_python = 'python'
print(list(word_python))

# Задача 10
# Описание: Создайте кортеж из чисел 1, 2, 3, преобразуйте его в строку (в формате "123") и выведите
tuple_new = (1,2,3)
(a,b,c) = tuple_new
result_string = str(a)+str(b)+str(c)
print(result_string)

# Задача 11 (Новая: split())
# Описание: Пользователь вводит предложение. Разбейте его на слова с помощью метода split() и выведите количество слов.
# Пример ввода: "Привет мир Python"
# Пример вывода: 3
sentence = input('Enter your sentence: ')
sentence_split = sentence.split()
print(len(sentence_split))

# Задача 12 (Новая: join())
# Описание: Дан список words = ["Hello", "world", "!"]. Объедините его в одну строку с пробелами между словами и выведите.
# Пример вывода: "Hello world !"
words = ["Hello", "world", "!"]
words_join = " ".join(words)
print(words_join)