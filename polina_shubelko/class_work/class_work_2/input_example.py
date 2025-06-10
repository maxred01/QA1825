NAME_USER = input('Введите свое имя:')
AGE_USER = input('Введите свой возраст:')

print ('Привет, я Полина, мне 24 года')
print ('Привет, я', NAME_USER, ', мне', AGE_USER,'года')
print ('Привет, я ' + NAME_USER + ', мне ' + str(AGE_USER) + ' года')
print (f'Привет, я {NAME_USER}, мне {AGE_USER} года')

A = input ('Введите первое число:')
B = input ('Введите второе число:')
result = int (A) + int (B)
print('Сумма:', result)

A = input ('Введите первое число:')
B = input ('Введите второе число:')
result = int (A) - int (B)
print ('Разность:', result)


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

password = '123456'
my_password = input('Введите пароль:')
if password == my_password:
    print('Доступ разрешен')
else:
    print('Неверный пароль')
