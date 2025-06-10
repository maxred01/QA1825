n = int(input('Введите число: '))
for number in [n]:
    for i in range(1,11):
        result = number * i
        print(number, "*", i, "=", result)
