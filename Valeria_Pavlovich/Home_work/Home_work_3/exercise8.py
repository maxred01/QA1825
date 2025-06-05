operation_type = input('Enter the operation type - sale or buy: ')
currency = input('Enter the currency: ')
usd_sale = 88.00
usd_buy = 90.00
eur_sale = 98.00
eur_buy = 100.00
if currency.upper() == 'USD':
    if operation_type == 'sale':
        amount = float(input('Enter the amount in USD: '))
        amount_given = amount * usd_sale - ((amount * usd_sale) * 0.015)
        print(f'You will get {amount_given:.2f} RUB')
    else:
        amount = float(input('Enter the amount in RUB: '))
        amount_given = amount / usd_buy - ((amount / usd_buy) * 0.015)
        print(f'You will get {amount_given:.2f} USD')
elif currency.upper() == 'EUR':
    if operation_type == 'sale':
        amount = float(input('Enter the amount in EUR: '))
        amount_given = amount * eur_sale - ((amount * eur_sale) * 0.01)
        print(f'You will get {amount_given:.2f} RUB')
    else:
        amount = float(input('Enter the amount in RUB: '))
        amount_given = amount / eur_buy - ((amount / eur_buy) * 0.01)
        print(f'You will get {amount_given:.2f} EUR')
