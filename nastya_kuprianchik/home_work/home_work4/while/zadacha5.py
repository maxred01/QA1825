while True:
    op = input("Введите операцию (+, -, *, /, exit): ")
    if op == "exit":
        print("Завершение")
        break

    a = int(input("Введите число: "))
    b = int(input("Введите число: "))

    if op == "+":
        print("Результат:", a + b)
    elif op == "-":
        print("Результат:", a - b)
    elif op == "*":
        print("Результат:", a * b)
    elif op == "/":
        if b == 0:
            print("Ошибка: деление на ноль!")
        else:
            print("Результат:", a // b)
