correct_password = 'qwerty123'
attempt = 3
while attempt > 0:
    password_input = input('Enter a password: ')
    if password_input == correct_password:
        print ('Access granted!')
        break
    elif attempt > 1:
        print (f'Access denied! Attempts left: {attempt - 1}')
    attempt -= 1
else:
    print(f'You ran out of attempts. The account is blocked!')
