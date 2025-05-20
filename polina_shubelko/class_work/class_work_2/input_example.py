NAME_USER = input('Введите свое имя:')
AGE_USER = input('Введите свой возраст:')

print ('Привет, я Полина, мне 24 года')
print ('Привет, я', NAME_USER, ', мне', AGE_USER,'года')
print ('Привет, я ' + NAME_USER + ', мне ' + str(AGE_USER) + ' года')
print (f'Привет, я {NAME_USER}, мне {AGE_USER} года')

A = input ('Введите число A')
B = input ('Введите число B')


if A==B:
    print ('Числа равны')
else:
    print ('Числа не равны')

if A!=B:
    print ('Числа не равны')
else:
    print ('Числа равны')

if A > B:
    print('>')
else:
    print('<')

if A < B:
    print('<')
else:
    print('>')

A = input('Введите пароль')

if ('A = 123456'):
    print('Доступ разрешен')
else:
    print('Неверный пароль')

