total = 0
num = int(input('Введите число: '))
while num != 0:
    total += num
    num = int(input('Следующее число: '))
print(f'{total}')
