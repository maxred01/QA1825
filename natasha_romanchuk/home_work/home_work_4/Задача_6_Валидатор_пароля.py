#Создайте функцию validate_password(password), которая проверяет:
# Длина >= 8 символов
# Содержит минимум 1 цифру
# Содержит минимум 1 заглавную букву
# Содержит минимум 1 специальный символ !@#$%^&*
# Пример вызова:
# print(validate_password("Weak"))     # False
# print(validate_password("Strong1@")) # True
# Требования:
# Возвращать словарь с результатами проверки:
# {
#     "length": True/False,
#     "digit": True/False,
#     "uppercase": True/False,
#     "special": True/False
# }

def validate_password(password):
    return {
     "length": len(password) >=8,
     "digit": any(char.isdigit() for char in password),
     "uppercase": any(char.isupper() for char in password),
     "special": any(char in '!@#$%^&*' for char in password),
 }
print(validate_password("12kgjfgr"))