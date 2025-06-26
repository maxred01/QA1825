# def arseniy():
#     """"Эта функция умеет говорить привет мир!"""
#     print('Привет мир')
#
#
# arseniy()
#
# def add_number(a: int, b: int) -> int:
#     """Складывать два числа и возвращать результат"""
#     result = a + b
#     return result
#
#
# def test_add():
#     assert add_number(2, 3) == 5
#     assert add_number(-1, 1) == 0
#
#
# def create_user(name: str, role: str = "tester") -> dict:
#     return {"name": name, "role": role}
#
# def test_user():
#     assert create_user("Alice") == {"name": "Alice", "role": "tester"}
#     assert create_user("Bob", "developer") == {"name": "Bob", "role": "developer"}
#
# def analizye_text(text: str) -> tuple:
#     length = len(text)
#     words = len(text.split())
#     return length, words
#
# def test_text():
#     text = "Арсений учись!"
#     char_counts, word_count = analizye_text(text)
#     assert char_counts == 14
#     assert word_count == 2
#
# is_even = lambda x: x % 2 == 0 #  Лямда функция
#
# def test_even_check():
#     assert is_even(4) is True
#     assert is_even(5) is False
#
#
# def three_args(var1 = None, var2= None, var3= None):
#     args = []
#     if var1 is not None:
#         args.append(f"var1 ={var1}")
#     if var2 is not None:
#         args.append(f"var2 ={var2}")
#     if var3 is not None:
#         args.append(f"var3 ={var3}")
#     if args:
#         print("Переданные аргументы: ", ", ".join(args))
#     else:
#         print("Нет аргументов отличных от None ")
#
# three_args(var1 = 21)
# three_args(var2 = 'Python', var3 =3)
# three_args(var1 = 'Python', var2 =3, var3 =9)

sum_lambda = lambda x, y : x + y
result = sum_lambda(5, 1)
print(result)

