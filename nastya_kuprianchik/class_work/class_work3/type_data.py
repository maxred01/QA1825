num_str = '123' # cтрока
num_int = 123 # число
num_int_str = int(num_str) # преобразование
num_float = 12.3 # дробное
num_bool_true = True # логическая правда
num_bool_false = False # логическая ложь

my_list = [1, 2, 3] # список
my_tuple = (1, 2, 3)# картеж
#my_tuple = tuple(my_list)
my_dict = {"name": "nina", "age": 19} #словарь

price = str(100) + "$"
print(price)

words = ['Привет', 'мир', 'Python']
words_python = 'Python'
words_python_split = 'Привет-мир-Python'
results = '-'.join(words_python)#разъединяет и соединяет
results_split = words_python_split.split('-')#обратное от join
print(results_split)
print(results_split[0])
print(results)
