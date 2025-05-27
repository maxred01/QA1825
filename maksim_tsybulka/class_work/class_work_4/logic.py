# Что такое условие?
weather = 'Дождь'

if weather == 'Дождь':
    print('Возьми зонт!')



# Условные инструкции и их синтаксис
temperature = 0

if temperature <= 0:
    print('Надень шубу')
elif temperature < 15:
    print('Надень куртку')
else:
    print('Надень футболку')


# Понятие блока выполнения
many = 100

if many >= 120:
    print('У вас много денег')
    print('Вы можете купить билет')

print('Спасибо за покупку')



# Логические выражения и операторы
age = 20
company = False
has_ticket = True

if not age <= 18:
    print('Добро пожловать на концерт!')

else:
    print('Вход запрещен!')



#Операторы ветвлений if...else
day = 'Вторник'
time = 15

if day == 'Вторник':
    if 10 <= time < 18:
        print('Магазин открыт')

    else:
        print('Магазин закрыт')

else:
    print('Магазин работает по вторникам')



# Блок схема для условий
password = input('Введите проль: ')

if password == '12342314':
    print('Доступ разрешен')
else:
    print(' Доступ запрещен')



#Вложенные конструкции
is_weekend = True
is_sonny = False

if is_weekend:
    if is_sonny:
        print('Едем на пляж')
    else:
        print('Смотрим фльм дома')
else:
    print('Идем на работу')
