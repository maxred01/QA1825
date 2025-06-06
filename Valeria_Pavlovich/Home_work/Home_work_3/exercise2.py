time = int(input('Enter the time (hours only): '))
if 0 <= time <= 5:
    print('Set the temperature to 18 C')
else:
    people = input('The presence of people - yes/no: ').lower()
    if people == 'no':
        print("Set the temperature to 16 C")
    else:
        weather = input('Enter the weather - cold/warm: ').lower()
        if weather == 'cold':
            print('Set the temperature to 22 C')
        else:
            print('Set the temperature to 20 C')
