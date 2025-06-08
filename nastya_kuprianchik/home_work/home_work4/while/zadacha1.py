import random
target = random.randint(1, 10)
attempts = 0
prompt = "Угадай число (1-10): "

while True:
    guess = int(input(prompt))
    attempts += 1
    if guess == target:
        print("Угадал! Количество попыток:", attempts)
        break
    prompt = "Нет! Попробуй ещё: "

