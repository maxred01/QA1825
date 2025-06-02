# Приобразование типов
# Пример 1 комбинированное преобразование

# NUM1 = '15'
# NUM2 = '7.5'
#
# if NUM1.isdigit() and NUM2.replace('.','', 1).isdigit():
#     TOTAL =  float(NUM1)+float(NUM2)
#     print(f'Summa = {TOTAL}')
# else:
#     print('Error')

# Привет 2 булевые преобразования с условием

# USER_INPUT  = input('Hotite prodoljit?(DA/NET) ').lower()
#
# CONTINUE_PROGRAM = True if USER_INPUT == 'da' else False
#
# if CONTINUE_PROGRAM and 10>5:
#     print('Prodoljaem raboty')
# else:
#     print('Zavershaem raboty')



# УСЛОВИЯ И ИХ КОМБИНАЦИИ
# Пример 1 Множественные условия с or

# WETHER = input('Pogoda (solnce/dojd/sneg): ').lower()
#
# if WETHER == 'dojd' or WETHER == 'sneg':
#     print('Vozmi zont')
# elif WETHER == 'solnce' and int (input('uf-index: '))>5:
#     print('Ispolzuite krem')
# else:
#     print('ulibaisya, horoshego dnya')




# ВЛОЖЕННЫЕ КОНСТРУКЦИИ
# Пример 1: многоуровневая вложенность

ACCOUNT_TYPE = 'premium'
BALANCE = 15000
WITHDRAW = 20000

if ACCOUNT_TYPE == 'premium':
    if BALANCE >= WITHDRAW:
        print('vidacha deneg')
    else:
        OVERDRAFT = WITHDRAW - BALANCE
        if(OVERDRAFT <= 5000):
            print('overdraft odobren')
        else:
            print('previshen limit po overdraftu')
else:
    if BALANCE >= WITHDRAW:
        print('vidacha deneg')
    else:
        print('nedostatochno deneg')