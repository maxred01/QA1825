age = int(input('Enter your age: '))
height = int(input('Enter your height: '))
weight = int(input('Enter your weight: '))
smoking = input('Do you smoke: yes or no? ').lower()
bmi = weight / (height/100)**2
print (f'Your body mass index is {bmi:.2f}')
if bmi < 18.5:
    print ('Your weight is insufficient')
elif 18.5 <= bmi < 25:
    print('Your weight is normal')
elif 25 <= bmi < 30:
    print ('You are overweight')
if (smoking == 'yes' and age > 40) or bmi >=30:
    print('Your health risk is high')
else:
    print('Your health risk is moderate')
