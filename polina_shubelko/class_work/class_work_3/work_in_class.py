age_1 = int(input("Введите возраст брата: "))
age_2 = int(input("Введите возраст сестры: "))
age_3 = int(input("Введите возраст мамы: "))
result = age_1 + age_2 + age_3
print ('Сумма: ', result)
result_str = str (result)
print(result_str)

user = {"name": "polina", "age": 24, "city": "Minsk"}
message = f"Пользователь {user['name']}, возраст {user['age']}, проживает в {user['city']}"
print(message)

text = 'Стоимость'
price = 99.9
print (text + str(price))

words = ['Привет', 'мир', 'Python']
words_python = 'Python'
words_python_split = 'Привет-мир-Python'
results_join = '-'.join(words_python)
results_split = words_python_split.split('-')
print(results_join)
print (results_split)