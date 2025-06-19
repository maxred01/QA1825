def name(name):
    print(f"Имя мое, {name}")

name('Максим')


def calculate_tax(price):
    return price * 0.2

total = calculate_tax(1000) + 1000
print(total)

#
# def process_data(data):
#     cleaned = clean(data)
#     analized = analize(cleaned)
#     return report(analized)

# process_data(1000)


def func1(num):
    return num * 1000


def func2(num):
    return num / 10


def func3(num):
    peremennay1 = func1(num)
    peremennay2 = func2(peremennay1)
    print(peremennay2)


func3(1000)


