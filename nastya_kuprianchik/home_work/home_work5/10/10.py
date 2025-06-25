import time
from functools import wraps


def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        message = f"Функция {func.__name__} выполнилась за {elapsed:.3f} секунд\n"

        # Вывод в консоль
        print(message.strip())

        # Сохранение в лог-файл
        with open("timings.log", "a", encoding='utf-8') as f:
            f.write(message)

        return result

    return wrapper
@timed
def calculate_sum(n):
    return sum(range(n))

# Пример вызова
calculate_sum(1_000_000)
