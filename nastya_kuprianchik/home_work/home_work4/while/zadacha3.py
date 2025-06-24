correct_password = "qwerty123"
password = input("Введите пароль: ")
while password != correct_password:
    print("Неверно! Попробуй ещё:")
    password = input("Введите пароль: ")

print("Доступ разрешён!")
