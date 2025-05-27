num_int = int(input('Enter a number: '))
if num_int % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')
###
password = input('Enter the password: ')
if password == 'qwerty123':
    print('The password is correct')
else:
    print('The password is incorrect')
###
a = int(input('Enter number a: '))
b = int(input('Enter number b: '))
c = int(input('Enter number c: '))
if a > b and a > c:
    print ('The biggest number is a')
elif b > a and b > c:
    print('The biggest number is b')
else:
    print('The biggest number is c')
###
height = int(input('Enter your height: '))
weight = int(input('Enter your weight: '))
height_adapt = height / 100
bmi = weight / height_adapt**2
print (f'Your body mass index is {bmi:.2f}')
if bmi < 18.5:
    print ('Your weight is insufficient')
elif 18.5 <= bmi < 25:
    print('Your weight is normal')
else:
    print ('You are overweight')
###
login = input('Enter the login: ')
password = input('Enter the password: ')
if login == 'admin' and password == '12345':
    print('You are successfully logged in')
else:
    print('Access denied')




