#Задача 4 обратный отсчет
import time
import winsound
countdown = int(input("Введите начальное значение для обратного отсчета: "))

while countdown > 0:
    print(countdown)
    time.sleep(1)
    countdown -= 1

print("Старт!")
winsound.Beep(1000,500)