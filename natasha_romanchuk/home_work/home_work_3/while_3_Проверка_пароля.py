
#Задача 3 проверка пароля
from getpass import getpass

x = 0
password = 123
while x != password:
    x = int(input('Введите пароль:'))
    if x != password:
        print('Неверно, попробуй еще раз')
print('Доступ разрешен')

#Задача 3 проверка пароля с ограничением попыток
password = 123
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    x = int(input('Введите пароль:'))
    attempts += 1
    if x == password:
        print('Доступ разрешен')
        break
    elif attempts < max_attempts:
        print(f'Неверно, у вас осталось {max_attempts - attempts} попыток')
    else:
        print('Доступ запрещен!Превышено число попыток.')

# Задача 3 проверка пароля со скрытием ввода пароля
from getpass import getpass
password = 123
while True:
    x = getpass('Введите пароль:')
    if x == password:
        print('Доступ разрешен')
        break
    else:
     print('Неверно, попробуй еще раз')