numbers = list(map(int,input('Введите список чисел: ').split()))
min_number = numbers[0]
for num in numbers:
    if num < min_number:
        min_number = num
print(f'Минимальный элемент {min_number}')