#пример 1
#комбинированое прелбразование
#num1 = '15'
#num2 = '7.5'

#if num1.isdigit() and num2.replace('.', '', 1).isdigit():
 #   total = float(num1) + float(num2)
  #  print(f'Сумма {total}')
#else:
 #   print('Ошибка')



#пример 2 bool
#user_input = input('Хотите продолжить? (Да/Нет) ').lower()

#continue_program = True if user_input == 'да' else  False

#if continue_program and 10 > 5:
 #   print('продолжить работу')
#else:
  #  print('завершить')



#weather = input('Погода (солнце/дождь/снег) ').lower()
#if weather == 'дождь' or weather == 'снег':
 #   print('Возми зонт')
#elif weather == 'солнце' and int(input('индекс')) > 5:
 #   print('используй крем')
#else:
 #   print('улыбайся')

account_type = 'premium'
balance = 15000
withdraw = 20000
if account_type == 'premium':
    if balance > withdraw:
        print('выдча денег')
    else:
        overdraft = withdraw - balance
        if overdraft <= 5000:
            print('одобрен')
        else:
            print('превышен лимит')
else:
    if balance >= withdraw:
        print('выдача денег')
    else:
        print('недостаточно средств')