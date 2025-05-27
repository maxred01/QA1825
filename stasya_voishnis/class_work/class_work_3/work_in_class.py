# Напишитти приложение которое принимает возвраст брата, сестры и мамы.
# Вывести общий возраст брата, сестры, мамы и приобразовать полученный результат в строку

age_b = int(input('Введите возвраст брата: '))
age_s = int(input('Введите возвраст сестры: '))
age_m = int(input('Введите возвраст мамы: '))

print(age_b + age_s + age_m)
results = str(age_b + age_s + age_m)
print(results)


# Cоздайте словарь user с ключами: name, age, city.
# Выведите в формате "пользователь[name], возраст [age], проживает в [city]"


user = {"name": "Stasya", "age": 25, "city": "Minsk" }
massage = f"пользователь {user['name']}, возраст {user['age']}, проживает в {user['city']}"
print(massage)


# В коде есть ошибка. Исправьте ее
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




