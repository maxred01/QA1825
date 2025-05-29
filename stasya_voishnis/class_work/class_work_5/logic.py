# ПРИОБРОЗОВАНИЕ ТИПОВ
# Пример 1. Комбинированное приобразование

# nu1 = '15'
# nu2 = '7.5'
#
# if nu1.isdigit() and nu2.replace('.','', 1).isdigit(): # .isdigit() проверяет состоит ли строка только из цифр
#     total =float(nu1) + float(nu2)
#     print(f'Сумма {total}')
# else:
#     print('Ошибка')

# Пример 2. Булевые приобразования с условием

# user_input = input('Хотите продолжить? (Да/Нет)').lower()
#
# continue_program = True if user_input == 'да' else False
#
# if continue_program and 10 > 5:
#     print('Продолжаем работу')
# else:
#     print('Завершаем работу')


# УСЛОВИЯ И ИХ КОМБИНАЦИИ
# Пример 1. Множественные условия с or

# weather = input('Погода(солнце/дождь/снег: ').lower()
#
# if weather == 'дождь' or weather == 'снег':
#     print('Возьмите зонт')
# elif weather == 'солнце' and int(input('уф- индекс '))>5:
#     print('Используйте крем')
# else:
#     print('Улыбайся, хорошего дня')


# ВЛОЖЕННЫЕ КОНСТРУКЦИИ
# Пример 1. Многоуровневая вложенность

# account_type = 'premium'
# balance = 15000
# withdraw = 20000
#
# if account_type == 'premium':
#     if balance >= withdraw:
#         print('Выдача денег')
#     else:
#         overdraft = withdraw - balance
#         if overdraft <= 5000:
#             print('Овердрафт одобрен')
#         else:
#             print('Превышен лимит')
# else:
#     if balance >= withdraw:
#         print('Выдача денег')
#     else:
#         print('Недостаточно средств')
