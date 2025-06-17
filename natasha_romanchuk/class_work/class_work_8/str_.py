text = 'Hello World! Привет, Мир! 123'

# Поиск и проверка содержимого
# 'in'  и 'not in'  (Операторы, не методы)
print('Hello' in text )  # True - проверка подстроки
print('Mars' not in text )  # True

#  .startswith(prefix)  -> bool
print(text.startswith('Hello')) # True - Начинается ли строка с префикса?
print(text.startswith(('Hi', 'By'))) # False - Можно передать кортеж префиксов

#  endswith(suffix)  -> bool
print(text.endswith('123')) # True - Заканчивается ли строка суффиксом?
print(text.endswith(('.', '!','?'))) # True - Кортеж суффиксов


#  .find(sub[, start[, end]]) -> int
#  Поиск ПОДСТРОКИ  'sub' . Возвращает индекс ПЕРВОГО вхождения или -1.
print(text.find('World'))  # 6
print(text.find('0'))      # 4 (первое '0')
print(text.find('0', 5))   # 7 (ищем '0' начиная с индекса 5)

print(text.find('Puthon'))  # -1 не найден

# .rfind(sub[, start[, end]]) -> int
    # Поиск ПОДСТРОКИ `sub`. Возвращает индекс ПОСЛЕДНЕГО вхождения или -1.
print(text.rfind("o"))     # 8 (последнее 'o' в "World")
print(text.rfind("Мир"))   # 24

    # .index(sub[, start[, end]]) -> int
    # Аналогичен .find(), но вызывает ValueError, если подстрока не найдена.
try:
    print(text.index("Python"))  # Вызовет ValueError
except ValueError:
    print("Подстрока не найдена!")

    # .rindex(sub[, start[, end]]) -> int
    # Аналогичен .rfind(), но вызывает ValueError, если подстрока не найдена.

    # .count(sub[, start[, end]]) -> int
    # Подсчет количества НЕПЕРЕКРЫВАЮЩИХСЯ вхождений подстроки `sub`.
    print(text.count("o"))     # 2 (в "Hello" и "World")
    print(text.count("!"))     # 1

    # Проверка на содержание только определенных символов
    # .isalpha() -> bool: Только буквы (Unicode) и не пустая?
    print("Hello".isalpha())   # True
    print("Hello123".isalpha()) # False
    print("Привет".isalpha())   # True

    # .isdigit() -> bool: Только цифры и не пустая?
    print("123".isdigit())     # True
    print("123.45".isdigit())  # False (точка не цифра)
    print("①".isdigit())       # True! (Unicode цифра)

    # .isnumeric() -> bool: Только числовые символы Unicode (цифры, дроби, римские и т.д.)?
    print("½".isnumeric())     # True
    print("Ⅳ".isnumeric())     # True (римская 4)
    print("123".isnumeric())   # True

# .isalnum() -> bool: Только буквы И/ИЛИ цифры? (isalpha + isdigit)
print("Hello123".isalnum())  # True
print("Hello 123".isalnum())  # False (пробел)

# .isspace() -> bool: Только пробельные символы (пробел, \t, \n и т.д.) и не пустая?
print("   \t\n".isspace())  # True
print("   a".isspace())  # False

# .islower() -> bool: Все буквенные символы в нижнем регистре? (Есть хотя бы одна буква)
print("hello".islower())  # True
print("Hello".islower())  # False ('H')
print("123!".islower())  # False (нет букв)

# .isupper() -> bool: Все буквенные символы в верхнем регистре? (Есть хотя бы одна буква)
print("HELLO".isupper())  # True
print("Hello".isupper())  # False ('e','l','l','o')
print("123!".isupper())  # False (нет букв)

# .istitle() -> bool: Каждое слово начинается с заглавной буквы?
print("This Is Title".istitle())  # True
print("This is not Title".istitle())  # False ("is", "not", "title")
print("123 Title".istitle())  # True (не-буквы игнорируются в проверке)


#Основные методы строк (Часть 2 - Преобразование регистра)

text = "hello world! python is awesome."

# .lower() -> str: Все буквы в нижний регистр.
print(text.lower())        # "hello world! python is awesome." (без изменений)
print("ПриВет".lower())    # "привет"

# .upper() -> str: Все буквы в верхний регистр.
print(text.upper())        # "HELLO WORLD! PYTHON IS AWESOME."
print("ПриВет".upper())    # "ПРИВЕТ"

    # .capitalize() -> str: Первый символ строки в верхний регистр, остальные - в нижний.
print(text.capitalize())   # "Hello world! python is awesome."

    # .title() -> str: Первую букву КАЖДОГО слова в верхний регистр.
print(text.title())        # "Hello World! Python Is Awesome."

    # .swapcase() -> str: Меняет регистр каждой буквы на противоположный.
print("HeLLo WoRLD".swapcase()) # "hEllO wOrld"


# Основные методы строк (Часть 3 - Управление пробелами и форматирование)

text = "   Hello World!   \t\n"
padded = "42"
user_input = "user,data,with,commas"

# .strip([chars]) -> str: Удаляет пробельные символы (или символы из `chars`) с ЛЕВОГО и ПРАВОГО конца строки.
print(text.strip())  # "Hello World!" (удалил пробелы, табуляцию, перенос)
print(",,,data...".strip(',.'))  # "data" (удалил запятые и точки по краям)

# .lstrip([chars]) -> str: Удаляет пробельные символы (или символы из `chars`) только с ЛЕВОГО конца.
print(text.lstrip())  # "Hello World!   \t\n"

# .rstrip([chars]) -> str: Удаляет пробельные символы (или символы из `chars`) только с ПРАВОГО конца.
print(text.rstrip())  # "   Hello World!"

# .center(width[, fillchar]) -> str: Центрирует строку в поле шириной `width`, заполняя пробелы символом `fillchar` (по умолч. пробел).
print(padded.center(10))  # '    42    '
print(padded.center(10, '*'))  # '****42****'

# .ljust(width[, fillchar]) -> str: Выравнивает строку по ЛЕВОМУ краю в поле шириной `width`.
print(padded.ljust(5))  # '42   '
print(padded.ljust(5, '-'))  # '42---'

# .rjust(width[, fillchar]) -> str: Выравнивает строку по ПРАВОМУ краю в поле шириной `width`.
print(padded.rjust(5))  # '   42'
print(padded.rjust(5, '0'))  # '00042'

# .zfill(width) -> str: Заполняет строку нулями слева до достижения длины `width`. Учитывает знак числа.
print("42".zfill(5))  # '00042'
print("-42".zfill(5))  # '-0042'
print("+3.14".zfill(7))  # '+003.14'


# .replace(old, new[, count]) -> str: Заменяет ВСЕ вхождения подстроки `old` на `new`. Если указан `count` - заменяет только первые `count` вхождений.
print("spam eggs spam".replace("spam", "SPAM")) # "SPAM eggs SPAM"
print("spam eggs spam".replace("spam", "SPAM", 1)) # "SPAM eggs spam"

    # .split(sep=None, maxsplit=-1) -> list: Разбивает строку на список подстрок, используя разделитель `sep` (по умолч. пробельные символы). `maxsplit` - макс. кол-во разбиений.
print("one two three".split())       # ['one', 'two', 'three']
print("one,two,three".split(','))    # ['one', 'two', 'three']
print("one  two   three".split())     # ['one', 'two', 'three'] (множеств. пробелы)
print("one.two.three".split('.', 1)) # ['one', 'two.three'] (только одно разбиение)
print(user_input.split(','))         # ['user', 'data', 'with', 'commas']

    # .rsplit(sep=None, maxsplit=-1) -> list: Аналогичен .split(), но разбивает начиная с КОНЦА строки.
print("one two three".rsplit(maxsplit=1)) # ['one two', 'three']

    # .join(iterable) -> str: Собирает строку из элементов итерируемого объекта (списка, кортежа и т.д.), используя исходную строку как разделитель.
words = ["Python", "is", "powerful"]
print(" ".join(words))     # "Python is powerful"
print(",".join(words))     # "Python,is,powerful"
print("...".join(words))   # "Python...is...powerful"
    # Часто используется для эффективной сборки строк из множества частей.
parts = ["Hello", "World", "!"]
result = " ".join(parts)   # Эффективнее, чем 'Hello' + ' ' + 'World' + ' ' + '!'


# Срезы строк (Slicing)

s = "PythonProgramming"

    # Отдельный символ
print(s[0])   # 'P' (первый)
print(s[-1])  # 'g' (последний)

    # Подстрока (срез)
print(s[0:6]) # 'Python'  [0, 1, 2, 3, 4, 5] (6 не включается!)
print(s[6:])  # 'Programming' (от индекса 6 до конца)
print(s[:6])  # 'Python' (от начала до индекса 5)
print(s[2:5]) # 'tho' (индексы 2, 3, 4)

    # С шагом
print(s[::2]) # 'Pto rgamn' (каждый 2-й символ: 0,2,4,6,...)
print(s[1::2]) # 'yhnPormig' (каждый 2-й, начиная с 1: 1,3,5,7,...)

    # Отрицательный шаг (Реверс строки - частый пример)
print(s[::-1]) # 'gnimmargorPnohtyP' (весь текст с шагом -1)
print(s[5:2:-1]) # 'noh' (от индекса 5 до 2 (не вкл.) с шагом -1: 5,4,3)

    # Отрицательные индексы в срезах
print(s[-4:-1]) # 'min' (индексы -4, -3, -2)

#*   Пример 1: Форматирование вывода (f-строки)

name = "Анна"
age = 30
height = 1.75
    # f-строки (Python 3.6+): Внутри {} можно писать выражения!
print(f"Имя: {name}, Возраст: {age}, Рост: {height:.2f} м")
    # Вывод: Имя: Анна, Возраст: 30, Рост: 1.75 м

#*   Пример 2: Валидация пользовательского ввода

user_input = input("Введите номер телефона (только цифры): ")
    # Убираем возможные пробелы/тире и проверяем, что остались только цифры
cleaned_input = user_input.replace(" ", "").replace("-", "")
if cleaned_input.isdigit() and len(cleaned_input) == 11:
    print(f"Номер принят: {cleaned_input}")
else:
    print("Некорректный ввод! Нужно ровно 11 цифр.")

#*   Пример 1: Форматирование вывода (f-строки)

name = "Анна"
age = 30
height = 1.75
    # f-строки (Python 3.6+): Внутри {} можно писать выражения!
print(f"Имя: {name}, Возраст: {age}, Рост: {height:.2f} м")
    # Вывод: Имя: Анна, Возраст: 30, Рост: 1.75 м

#*   Пример 2: Валидация пользовательского ввода

user_input = input("Введите номер телефона (только цифры): ")
    # Убираем возможные пробелы/тире и проверяем, что остались только цифры
cleaned_input = user_input.replace(" ", "").replace("-", "")
if cleaned_input.isdigit() and len(cleaned_input) == 11:
    print(f"Номер принят: {cleaned_input}")
else:
    print("Некорректный ввод! Нужно ровно 11 цифр.")

#*   Пример 5: Генерация текста (`join` для эффективности)

    # Неэффективно (создается много промежуточных строк):
result = ""
for i in range(1, 101):
    result += str(i) + ", "  # Конкатенация в цикле - плохо!
print(result)

    # Эффективно (с использованием списка и join):
numbers = []
for i in range(1, 101):
    numbers.append(str(i))
result = ", ".join(numbers)
print(result)








