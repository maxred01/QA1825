NAME_USER = input('Введите имя : ')
AGE = input('Введите возраст: ')

print('Привет, я Настя мне 19 лет')
print('Привет, я', NAME_USER, 'мне',AGE, 'лет')
print('Привет, я '+ NAME_USER + ' мне '  +  str(AGE) + ' лет')
print(f'Привет, я {NAME_USER} мне, {AGE} лет')

a = int(input('Вести число a : '))
b = int(input('Вести число b : '))
result = a + b
res = a - b
resul = a * b
resu = a/b
print(f'Cумма: {result}, 'f'Вычитание: {res}',f'Умножение: {resul}',f'Деление: {resu}')

f = int(input('Вести число f : '))
d= int(input('Вести число d : '))
if f == d:
     print('Равны')
else: print('Не равны')

if f > d :
    print('больше')
else:
    print('меньше')

if f < d :
    print('меньше')
else:
    print('больше')

if f >= d:
        print('больше или равно')
else:
        print('меньше или равно')

if f <= d :
    print('меньше или равно')
else:
    print('больше или равно')

if f != d:
        print('Не равны')
else:
        print('равны')

c = input('Ведите пароль: ')
k = 123456
if (c == k):
    print('Доступ разрешен')
else:
    print('Неверный пароль')

celsia = int(input('Ведите цельсия: ' ))
resultat = celsia + 32
print(f'Вывод фаренгейт: {resultat}')
