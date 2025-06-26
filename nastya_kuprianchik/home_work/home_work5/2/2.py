import random
import string


def generate_password(length):
    if length < 8:
        raise ValueError("Минимальная длина пароля — 8 символов")

    upper_count = max(1, int(length * 0.4))
    lower_count = max(1, int(length * 0.4))
    digit_count = length - upper_count - lower_count

    # Гарантируем хотя бы одну цифру
    if digit_count < 1:
        digit_count = 1
        if upper_count > lower_count:
            upper_count -= 1
        else:
            lower_count -= 1

    password_chars = (
            random.choices(string.ascii_uppercase, k=upper_count) +
            random.choices(string.ascii_lowercase, k=lower_count) +
            random.choices(string.digits, k=digit_count)
    )

    random.shuffle(password_chars)
    return ''.join(password_chars)


# Вызов функции — без этого ничего не будет отображаться!
print(generate_password(10))
