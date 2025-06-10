#Преобразование типов
#комбинированное преобразование

#num1 = '15'
#num2 = '7.5'

#if num1.isdigit() and num2.replace('.', '', 1).isdigit():
#    total = float(num1) + float(num2)
#   print(f'Сумма {total}')
#else:
#    print('Ошибка')

#Пример 2

#user_input = input('Хотите продолжить? (Да/Нет) ').lower()

#continue_program = True if user_input == 'да' else False

#if continue_program and 10 > 5:
#    print('Продолжаем работу')
#else:
#    print('Завершаем работу')

# Условия и их комбинации
# Пример 1 Множественные условия с or

#weather = input('Погода (сщлнце/дождь/снег) ').lower()
#if weather == 'дождь' or weather == 'снег':
#    print('Возьмите зонт')
#elif weather == 'солнце' and int(input('уф- индекс ')) > 5:
#    print('используйте крем')
#else:
#    print('улыбайся, хорошего дня')

# Вложенные конструкции
#Пример 1 многоуровневая вложенность

account_type = 'premium'
balance = 15000
withdraw = 20000
if account_type == 'premium':
   if balance >= withdraw:
       print('выдача денег')
   else:
       overdraft = withdraw - balance
       if overdraft <= 5000:
           print('овердрафт одобрен')
       else:
           print('превышен лимит')
else:
    if balance >= withdraw:
        print('Выдача денег')
    else:
        print('Недостаточно средств')











