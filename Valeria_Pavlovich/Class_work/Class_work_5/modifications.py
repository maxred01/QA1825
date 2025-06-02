# num1 = '15'
# num2 = '7.5'
#
# if num1.isdigit() and num2.replace('.','', 1).isdigit():
#     total = float(num1) + float(num2)
#     print(f'Total {total}')
# else:
#     print('Error')

# user_input = input('Do you want to continue? (Yes/No) ').lower()
# continue_program = True if user_input == 'yes' else False
#
# if continue_program and 10 > 5:
#     print('continue working')
# else:
#     print('stop working')
#

# weather = input('Weather (sun/rain/snow) ').lower()
# if weather == 'rain' or weather == 'snow':
#     print('Take an umbrella')
# elif weather == 'sun' and int(input('UV index ')) > 5:
#     print('Use SPF')
# else:
#     print('Smile and have a good day')

account_type = 'premium'
balance = 15000
withdraw = 20000
if account_type == 'premium':
    if balance >= withdraw:
        print('money withdrawal')
    else:
        overdraft = withdraw - balance
        if overdraft <= 5000:
            print('overdraft is approved')
        else:
            print('the limit is exceeded')
else:
    if balance >= withdraw:
        print('money withdrawal')
    else:
        print('insufficient funds')
