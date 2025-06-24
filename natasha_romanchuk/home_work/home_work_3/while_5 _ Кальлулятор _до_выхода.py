while True:
    op = input("Операция (+, -, *, /, exit): ")

    if op == "exit":
        print("Завершение")
        break

    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    if op == "+":
        print(f'Результат: {a + b}')
    elif op == "-":
        print(f'Результат: {a-b}')
    elif op == "*":
        print(f'Результат:{a*b}')
    elif op == "/":
        if b != 0:
            print(f'Результат:{a/b}')
        else:
            print("Ошибка: деление на ноль")
    else:
        print("Неизвестная операция")