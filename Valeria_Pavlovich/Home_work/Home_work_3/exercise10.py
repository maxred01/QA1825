temperature = float(input('Enter temperature in Celsius: '))
if temperature < 0:
    pressure = float(input('Enter pressure in kPa: '))
    if pressure > 100:
        print('Ice formation')
    else:
        print('Stable state')
elif temperature > 200:
    pressure = float(input('Enter pressure in kPa: '))
    if pressure > 500:
        print('Plasma state')
    else:
        print('Stable state')
elif temperature > 100:
    catalyst = input('Is the catalyst present - yes or no?: ').lower()
    if catalyst == 'yes':
         print('Synthesis reaction')
    else:
        print('Stable state')
else:
    print('Stable state')