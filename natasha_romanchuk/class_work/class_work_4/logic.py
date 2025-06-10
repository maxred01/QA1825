# a = int(input('Введи число'))
# if a %2==0:
#     print('Число четное')
# else:
#     print('Число не четное')

# a = input('Введи пароль')
# if a == 'qwerty123' :
#      print('Доступ разрешен')
# else:
#      print('Доступ запрещен')

# a = input('Введи число')
# # d = input('Введи число')
# # c = input('Введи число')
# # if  c < a > d:
# #     print('Число a большее')
# # elif a < d > c:
# #     print('Число d большее')
# # else:
# #     print('Число c большее')

# weight = float(input('Введите вес кг'))
# height = float(input('Введите рост м'))
# IMT = weight/(height**2)
# if IMT <= 16:
#     print('Дефицит массы тела')
# elif 16 <= IMT <= 18.5:
#     print('Норма')
# else:
#     print('Ожирение')

login = input('Введи логин')
password = input('Введи пароль')
if login == 'admin' and   password == 12345:
    print('Успешный вход')
else:
    print('Ошибка')