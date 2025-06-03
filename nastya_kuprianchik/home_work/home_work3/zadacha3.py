password = input('введите пароль: ')
errors = []

if len(password) < 8 :
    print('Пароль должен содержать минимум 8 символов.')

if not any(char.isdigit() for char in password):
    errors.append("Пароль должен содержать хотя бы 1 цифру.")

if not any(char.isupper() for char in password):
    errors.append("Пароль должен содержать хотя бы 1 букву в верхнем регистре.")

if not any(char in "!@#$%^&*" for char in password):
    errors.append("Пароль должен содержать хотя бы 1 спецсимвол (!@#$%^&*).")

if errors:
    print("Невалидный пароль. Обнаружены следующие проблемы:")
    for error in errors:
        print(" -", error)
else:
    print("Пароль валиден!")