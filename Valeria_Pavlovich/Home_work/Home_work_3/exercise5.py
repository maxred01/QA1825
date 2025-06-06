income = int(input("Enter your income: "))
if income <= 20000:
    tax_low = income * 0.1
    print(f'Your tax sum is {tax_low}')
if 20000 < income <= 50000:
    tax_medium = 20000 * 0.1 + ((income - 20000) * 0.2)
    print(f'Your tax sum is {tax_medium}')
if income > 50000:
    tax_high = 20000 * 0.1 + ((income - 20000) * 0.3) + 5000
    print(f'Your tax sum is {tax_high}')
