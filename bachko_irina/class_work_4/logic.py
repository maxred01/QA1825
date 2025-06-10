#namber = int(input('Введите число: '))

#if namber % 2 == 0:
#     print("Четное")
#else:
#    print("Не четное")

#password = '1234'
#pass_user = input('Введите пароль: ')

#if password == pass_user:
#    print('Успешная регистрация')
#else:
#    print('Отказано')

#A = int(input('Введите число: '))
#B = int(input('Введите число: '))
#C = int(input('Введите число: '))
#if A>=B and B>=C:
#    print('Наибольшее A')
#else:
#    print('Наибольшее B')

#Weight = int(input('Введите вес: '))
#Height = int(input('Введите рост: '))

#IMT = Weight / (Height ** 2)

#if IMT <= 18.5:
#    print('Недостаточная масса тела')
#if IMT >= 18.5 IMT <= 25:
#    print('НОРМА')
#else:
#    print('ОЖИРЕНИЕ')


password = '1234'
login = 'admin'

pass_user = input('Введите пароль: ')
log_user = input('Введите логин: ')

if password == pass_user and login == log_user:
    print('Успешная регистрация')
else:
    print('Отказано')
