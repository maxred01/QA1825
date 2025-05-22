bro = int(input("Enter brother's age: "))
sis = int(input("Enter sister's age: "))
mum = int(input("Enter mother's age: "))
total_age = bro + sis + mum
total_age_str = str(total_age)
print ("Total age: " + total_age_str)

users_dict= {'name': 'valeria', 'age': 26, 'city': 'Minsk'}
a = users_dict.get('name')
b = users_dict.get('age')
c = users_dict.get('city')
print(f'User {a}, age {b}, lives in the city of {c}')

text = 'Price: '
price = 99.9
print(text+str(price))