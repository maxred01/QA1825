import random
import string

def generate_password(length):

    if length < 8:
        return 'Password should be at least 8 characters long'

    uppercase_count = int(length * 0.4)
    lowercase_count = int(length * 0.4)
    digit_count = max(1, length - uppercase_count - lowercase_count)

    if digit_count > length * 0.2:
        extra_digits = digit_count - int(length * 0.2)
        digit_count = int(length * 0.2)
        if uppercase_count >= extra_digits:
            uppercase_count -= extra_digits
        else:
            lowercase_count -= extra_digits

    uppercase_letters = random.choices(string.ascii_uppercase, k=uppercase_count)
    lowercase_letters = random.choices(string.ascii_lowercase, k=lowercase_count)
    digits = random.choices(string.digits, k=digit_count)

    password_characters = uppercase_letters + lowercase_letters + digits

    random.shuffle(password_characters)

    password = "".join(password_characters)
    return password

length = int(input('How long would you like your password to be? '))
password = generate_password(length)
print(password)
