# Задача 2
# Умный термостат
# Условие: Система анализирует:
# Время суток (утро: 6-11, день: 12-17, вечер: 18-23, ночь: 0-5)
# Погоду на улице (холодно/тепло)
# Наличие людей дома (да/нет)


time = int(input('Введите время суток: '))
whether = str(input('Введите: холодно/тепло: ')).lower()
people = str(input('Люди дома: да/нет: ')).lower()

if time >=6 and time <=11:
    result_time = 'утро'
elif 12 <= time <= 17:
    result_time = 'день'
elif 18 <= time <= 23:
    result_time = 'вечер'
elif 0 <= time <= 5:
    result_time = 'ночь'

if result_time != 'ночь' and people == 'да' and whether == 'холодно':
     print('люди дома и холодно → 22°C')
else:
     print('люди дома и тепло → 20°C')

if result_time == 'ночь' and people == 'да':
    print('ночь → 18°C')
else:
    print('людей нет → 16°C')


#weather = input('Погода (сщлнце/дождь/снег) ').lower()
#if weather == 'дождь' or weather == 'снег':
#    print('Возьмите зонт')
#elif weather == 'солнце' and int(input('уф- индекс ')) > 5:
#    print('используйте крем')
#else:
#    print('улыбайся, хорошего дня')



#Задача 3
#Валидатор пароля
#Пароль должен содержать:
#Минимум 8 символов
#Хотя бы 1 цифру
#Хотя бы 1 букву в верхнем регистре
#Хотя бы 1 спецсимвол (!@#$%^&*)

# password = input('Введите пароль: ')
# numbers = '1234567890'
# upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# lower_letters = 'abcdefghijklmnopqrstuvwxyz'
# symbols = '!@#$%^&*'
# accep_password = numbers + upper_letters + lower_letters + symbols
# passw = set(password)
# if any(char not in accep_password for char in passw):
#     print ('Ошибка. Запрещенный спецсимвол')
# else:
#     recommendations = []
#     if len(password) < 8:
#         recommendations.append(f'увеличить число символов - {8-len(password)}')
#     for what, message in ((numbers,         'цифру '),
#                           (upper_letters,   'заглавную букву '),
#                           (lower_letters,   'строчную букву '),
#                           (symbols,         'спецсимвол ')):
#         if all(char not in what for char in passw):
#             recommendations.append(f' добавить {message}')
#     if recommendations:
#         print( ",".join(recommendations))
#     else:
#         print('Отличный пароль. ')


