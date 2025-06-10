#Задача 3
stroka = 'abracadabra'
count = 0
for letter in stroka:
    if letter == 'a':
        count += 1
print(count)

#Задача 3 запросить у пользователя
stroka = str(input('Введи слово'))
stroka = stroka.lower()
count = 0
for letter in stroka:
    if letter == 'a':
        count += 1
print(count)