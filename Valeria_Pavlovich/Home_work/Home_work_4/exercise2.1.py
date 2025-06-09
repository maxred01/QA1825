import random
print('The number guessing game (1-10). You have 5 attempts')
num = random.randint(1,10)
attempt = 5
while attempt > 0:
    number = int(input('Enter a number: '))
    if number == num:
        print('Correct!')
        break
    elif number > num:
        print('Too high!')
    elif number < num:
        print('Too low!')
    attempt -= 1
    if attempt == 0 and number != num:
        print(f'You ran out of attempts. The number was {num}')
