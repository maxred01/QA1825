pin = int(input('Enter your pin: '))
balance = 150000
limit = 100000
if len(str(pin)) != 4:
    print('PIN must be 4 digits')
else:
    print('Your balance is:', balance)
    print('Would you like to proceed? yes or no')
    if input().lower() == "yes":
        sum_withdraw = float(input('Enter the sum to withdraw: '))
        if sum_withdraw > balance:
            print('The operation is terminated - insufficient funds')
        elif sum_withdraw > limit:
            print('The operation is terminated - withdrawal limit is exceeded')
        else:
            print('The operation is successful - please, take your money')
    else:
        print('The operation is terminated by the client')
