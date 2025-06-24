#Создайте функцию generate_password(length), которая:

# Генерирует пароль заданной длины (минимум 8 символов)
# Состоит из:
# Заглавных букв (40%)
# Строчных букв (40%)
# Цифр (20%)
# Гарантирует хотя бы одну цифру в пароле

import random  # Выбор случайных чисел и перемешивание
import string   # Готовые наборы букв и цифр

from string import digits


def generate_password(lenght):
    if lenght < 8:
        return "Ошибка: длинна пароля должна оставлять не меньше 8 символов"

    digits_count = max(1, round(0,2*lenght))  # хотябы 1 цифра , 20% от длинны пароля, округляем до ближ целого
    total_letters = lenght - digits_count     #общ колво букв
    uppercase_letters = total_letters // 2    # колво заглавных
    lowercase_letters = total_letters - uppercase_letters  # количество прописных
    digits_list = [random.choice(string.digits) for _ in range(digits_count)]  # возврыщает рандомную цифру
    uppercase_letters_list = [random.choice(string.ascii_uppercase) for _ in range(uppercase_letters)]  # возврыщает рандомную заглавную букву
    lowercase_letters_list = [random.choice(string.ascii_lowercase) for _ in range(lowercase_letters)]   # возврыщает рандомную прописную букву
    all_lists = digits_list + uppercase_letters_list + lowercase_letters_list  # соединяем все символы
    random.shuffle(all_lists)            # перемешиваем
    password = "".join(all_lists)         # соединяем
    return password
print(generate_password(8))

