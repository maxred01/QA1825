import re

def validate_password(password):
    return {
        "length": len(password) >= 8,
        "digit": any(char.isdigit() for char in password),
        "uppercase": any(char.isupper() for char in password),
        "special": bool(re.search(r"[!@#$%^&*]", password))
    }
print(validate_password("Weak"))
# {'length': False, 'digit': False, 'uppercase': True, 'special': False}

print(validate_password("Strong1@"))
# {'length': True, 'digit': True, 'uppercase': True, 'special': True}
