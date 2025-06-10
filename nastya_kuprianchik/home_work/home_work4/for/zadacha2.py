numbers = list(map(int,input("Введите числа через пробел: ").split()))
total = 0
for num in numbers:
    if num % 2 == 0:
        total += num
print(f'Сумма {total}')

