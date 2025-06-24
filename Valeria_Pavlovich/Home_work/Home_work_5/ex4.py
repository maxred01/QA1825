from mod_currency_converter import convert, RATES
amount = float(input('Amount: '))
from_curr = input('From Currency: ').upper()
if from_curr not in RATES:
    print(f'Unknown currency: {from_curr}')
else:
    to_curr = input('To Currency: ').upper()
    if to_curr not in RATES:
        print(f'Unknown currency: {to_curr}')
    else:
        result = convert(amount, from_curr, to_curr)
        if result is not None:
            print(f'{result:.2f}')