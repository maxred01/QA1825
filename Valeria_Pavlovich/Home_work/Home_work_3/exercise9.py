import datetime
time = datetime.datetime.now()
weekday = time.weekday()
hour = time.hour
role = input('Enter the role: ').lower()
emergency = input('Is it an emergency - yes/no?: ').lower()
if emergency == 'yes':
    print('Access granted')
else:
    blacklist = input('Is this person blacklisted - yes/no?: ').lower()
    if blacklist == 'yes':
        print('Access denied')
    else:
        if role == 'employee':
            print ('Access granted')
        elif role == 'contractor':
            if 9 <= hour < 18 and weekday < 5:
                print('Access granted')
            else:
                print('Access denied')
        elif role == 'guest':
            accompany = input('Are you accompanied by the employee - yes or no?: ').lower()
            if accompany == 'yes':
                print('Access granted')
            else:
                print('Access denied')
        else:
            print('Unknown role - access denied')
