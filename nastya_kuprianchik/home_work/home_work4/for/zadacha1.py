n = int(input("Введите число: "))
if n > 0:
    for i in range(1, n + 1):
        print(i, end=' ')
    for i in range(n,0 , - 1):
        print(i, end=' ')
else:
    print("N должно быть больше 0!")
