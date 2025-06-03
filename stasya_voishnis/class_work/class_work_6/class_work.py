x = float(input('Введите сколько километров вы пробежали: '))
y = float(input('Введите сколько километров хотите пробежать: '))
d = 1

while x < y:
    x *= 1.1
    d +=1
print(f'Потребовалось {d} дней')

#Проценты = (Сумма вклада * Процентная ставка * Количество дней) / 365
x = float(input('Введите сумму вклада: '))
p = float(input('Введите процент вклада: '))
y = float(input('Введите сумму которую хотите накопить: '))
years = 0
current = x
while current < y:
    resalt = x * p / 100
    current += int(resalt)
    years +=1
print(years)
