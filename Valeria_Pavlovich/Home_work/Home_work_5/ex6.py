import re

password = input('Enter password: ')
def validate_password(password):
    results = {'length': len(password) >= 8,
               'digit': bool(re.search(r'\d', password)),
               'uppercase': bool(re.search(r'[A-Z]', password)),
               'special': bool(re.search(r'[!@#$%^&]', password))}
    return results
print(validate_password(password))
