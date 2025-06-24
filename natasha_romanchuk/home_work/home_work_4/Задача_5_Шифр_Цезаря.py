# Задача:
# Напишите функцию caesar_cipher(text, shift), которая:
#
# Принимает строку и сдвиг (целое число)
# Шифрует текст по принципу:
# Каждая буква заменяется на букву, стоящую на shift позиций дальше в алфавите
# Регистр сохраняется
# Неалфавитные символы остаются без изменений
# Пример вызова:
#
# print(caesar_cipher("Hello, World!", 3))  # "Khoor, Zruog!"
# print(caesar_cipher("XYZ", 4))           # "BCD"
# Требования:
#
# Использовать string.ascii_uppercase и string.ascii_lowercase
# Реализовать декодирование при отрицательном shift

import string

def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char in string.ascii_lowercase:
            new_char = string.ascii_lowercase[(string.ascii_lowercase.index(char) + shift) % 26]
            result += new_char
        elif char in string.ascii_uppercase:
            if char in string.ascii_uppercase:
                new_char = string.ascii_uppercase[(string.ascii_uppercase.index(char) + shift) % 26]
                result += new_char
        else:
            result += char
    return result
print(caesar_cipher("ABCdef2",2))



