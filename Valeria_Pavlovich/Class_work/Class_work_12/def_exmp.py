#
#
# def add_number(a: int, b: int) -> int:
#     results = a + b
#     return results
#
#
# def test_add():
#     assert add_number(2, 3) == 5
#
#     assert add_number(-1, 1) == 0


# def create_user(name: str, role: str = 'tester') -> dict:
#     return {'name': name, 'role': role}
#
#
# def test_user():
#     assert create_user('Alice') == {'name': 'Alice', 'role': 'tester'}
#     assert create_user('Bob', 'developer') == {'name': 'Bob', 'role': 'developer'}

# def analyze_text(text: str) -> tuple:
#     length = len(text)
#     words = len(text.split())
#     return length, words
#
#
# def test_text():
#     text = 'hello, world!'
#     char_count, word_count = analyze_text(text)
#     assert char_count == 13
#     assert word_count == 2


# is_even = lambda x: x % 2 == 0
#
#
# def test_even_check():
#     assert is_even(4) is True
#     assert is_even(5) is False

# def three_args(*, var1=None, var2=None, var3=None):
#     args = []
#     if var1 is not None:
#         args.append(f'var1 = {var1}')
#     if var2 is not None:
#         args.append(f'var2 = {var2}')
#     if var3 is not None:
#         args.append(f'var3 = {var3}')
#     if args:
#         print('Pass the arguments:', ",".join(args))
#     else:
#         print('No arguments different from None')
#
# three_args(var1 = 21)
# three_args(var1='Python', var3=3)
# three_args(var1='Python', var2=3, var3=9)

x = lambda a, b: a + b
print(x(2, 3))