numbers = int(input('Ведите число: '))
if numbers % 2 == 0:
    print('четное')
else:
    print('нечетное')


password = input("Введите пароль: ")
if password == 'qwerty123':
    print("Верный пароль")
else:
    print("Неверный пароль")


a = int(input("Ведите число: "))
b = int(input("Ведите число: "))
c = int(input("Ведите число: "))
if a >= b and a >= c:
    print("наибольшее a")
elif b >= a and b >= c:
    print("наибольшее b")
else:
    print(" наибольшее c")


weight = float(input("Ведите вес в киллограммах: "))
height = float(input("Ведите рос в метрах: "))
bmi = weight/(height ** 2)
if bmi < 18.5:
    print("Недостаточный вес")
elif 18.5 <= bmi < 25:
    print("Норма")
else :
    print("Избыточный вес")


password = input("Введите пароль: ")
login = input("Введите логин: ")
if password == '12345' and login == 'admin':
    print("Верный пароль")
else:
    print("Неверный пароль")
