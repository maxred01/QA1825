#Напишите приложение, которое принимает возраст брата, сестры и мамы
#Вывести общий возраст семьи в строку

#brother_age = int(input ("Введите возраст брата: "))
#sister_age = int(input ("Введите возраст сестры: "))
#mother_age = int(input ("Введите возраст мамы: "))

#total_age = brother_age + sister_age + mother_age

#total_age_str = str(total_age)
#print ("Общий возраст семьи: " + total_age_str)

#Создать словарь users с ключами: name, age, city.
#Вывести данные в формате "Пользователь [name] , возраст [age], проживает в [city]"

#user = {
#    "name": "irina",
#    "age": 25,
#    "city": "Minsk"
#}
#massage = f"Пользователь {user['name']}, возраст {user['age']} , проживает в {user['city']}"
#print(massage)

#Исправить

#price = 99.9
#price_str = str(price)
#print ("Стоимость: " + price_str)

produkt = {
    "text": "Стоимость: ",
    "price": 99.9
}
massage = f"{produkt ['text']} {produkt ['price']}"
print(massage)

