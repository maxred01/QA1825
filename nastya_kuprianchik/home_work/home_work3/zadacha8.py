money = float(input('Введите сумму: '))
val = input('Целевая валюта ((USD/EUR/CNY): ').upper()
type_oper = input('Тип операции (покупка/продажа): ').lower()

if val == 'USD':
    if type_oper == 'покупка':
        rate = 90
        commission = 0.015
        summa = (money * (1 - commission)) / rate
        print(f'Сумма: {summa}')
    elif type_oper == 'продажа':
        rate = 88
        commission = 0.015
        summa = (money * (1 - commission)) / rate
        print(f'Сумма: {summa}')
    else:
        print('Неверный тип операции!')
elif val == 'EUR':
        if type_oper == 'покупка':
            rate = 100
            commission = 0.01  # исправлено: 1%
            summa = (money * (1 - commission)) / rate
            print(f'Сумма: {summa}')
        elif type_oper == 'продажа':
            rate = 98
            commission = 0.01  # исправлено: 1%
            summa = (money * (1 - commission)) / rate
            print(f'Сумма: {summa}')
        else:
            print('Неверный тип операции!')
else:
    print('Неверно выбрана валюта')