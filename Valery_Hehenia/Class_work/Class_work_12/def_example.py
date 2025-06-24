def add_number(a:int, b:int)->int:
    """Складывать два числа и возвращать результат"""
    results = a + b
    return results


def test_add():
    assert add_number(2, 3) == 5

    assert add_number(-1, 1) == 0


def create_user(name:str, role:str = "tester")->dict:
    return {'name':name, 'role':role}

def test_user():
    assert create_user('Alice') == {'name':'Alice', 'role': 'tester'}
    assert create_user('Bob', 'developer') == {'name':'Bob', 'role': 'tester'}


def anlizye_text(text: str)->tuple:
    length = len(text)
    words = len(text.split())
    return length, words

def test_text():
    text= '12345'
    char_count, word_count = anlizye_text(text)
    assert char_count == 14
    assert word_count == 2


is_even = lambda x: x % 2 == 0

def test_even():
    assert is_even(is_even(4)) is True
    assert is_even(is_even(5)) is False




# Задача 1
# Создайте функцию three_args(), которая принимает 1, 2 или 3 строго ключевых параметра.
# В результате ее работы на печать в консоль выводятся значения переданных переменных,
# но только если они не равны None.
# Получим, например, следующее сообщение: Переданы аргументы: var1 = 2, var3 = 10.


def three_args(*, var1=None,var2=None, var3=None):
    args=[]
    if var1 is not None:
        args.append(var1)
    if var2 is not None:
        args.append(var2)
    if var3 is not None:
        args.append(var3)
    if args:
        print("Переданы аргументы:", ", ".join(args))
    else:
        print('Нет аргументов отличных от None')

three_args(var1=21)
three_args(var1='Python', var3=3)
three_args(var1='Python', var2=3, var3=9)


#Написать лямбда функцию которая вычисляет сложение двух чисел и выводит результат

sum_numbers = lambda x, y: x + y
print(sum_numbers(5, 3))
