# Задача 1
n = int(input("Введи число:"))
if n > 0:
    for i in range(1, n + 1):
         print(i , end=' ')
else:
    print('Введи число больше нуля')


# Задача 1 в обратном порядке
n = int(input("Введи число:"))
if n > 0:
    for i in range(n, 0, -1):
         print(i , end=' ')
else:
    print('Введи число больше нуля')




