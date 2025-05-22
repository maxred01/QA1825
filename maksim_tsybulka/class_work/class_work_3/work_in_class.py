# Напишите приложение которое принимает возраст брата, сестры и мамы.
# Вывести общий возраст брата, сестры, мамы и приобразовать полученный результат в строку

brother_age = int(input("Введите возраст брата: "))
sister_age = int(input("Введите возраст сестры: "))
mother_age = int(input("Введите возраст мамы: "))

total_age = brother_age + sister_age + mother_age

total_age_str = str(total_age)
print("Общий возраст семьи: " + total_age_str)


# Создайте словарь users с ключами: name, age, city.
# Выведите данные в формате "Пользователь [name], возраст [age], проживает в [city]"
user = {
    "name": "max",
    "age": 25,
    "city": "Minsk"
        }
message = f"Пользователь {user['name']}, возраст {user['age']}, проживает в {user['city']}"
print(message)




# В коде есть ошибка. Исправьте ее
text = 'Стоимость: '
price = 99.9
print(text + price)


text = 'Стоимость: '
price = 99.9
print(text + str(price))

















words = ['Привет', 'мир', 'Python']
words_python = 'Python'
words_python_split = 'Привет-мир-Python'
results_join = '-'.join(words_python)
results_split = words_python_split.split('-')
print(results_join)
print(results_split)
print(results_split[0])
print(words_python[0])
