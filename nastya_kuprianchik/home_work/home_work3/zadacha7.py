age = int(input('Введите свой возраст: '))
wes = float(input('Введите свой вес в кг: '))
height = float(input('Введите свой рост в м: '))
kyr = input('Курение (да/нет): ').lower()

imt = wes/ (height ** 2)

if imt > 30:
    print('высокий риск для здоровья')
elif kyr == 'да' and age > 40 :
    print('высокий риск для здоровья')
else:
    print('умеренный риск для здоровья')
