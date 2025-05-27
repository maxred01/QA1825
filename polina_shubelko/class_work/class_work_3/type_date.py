num_str = '123' # строка
num_int = 123 # число
num_float = 12.3 # дробное число
num_int_str = int (num_int) # преобразование строки в число
results = str (num_float)
print (results)

num_int = 100500
num_int_str_ = str (num_int) # преобразование числа в строку

num_float = 12.3
num_float_int = int (num_float)
results = int (num_float)
print (results) # преобразование числа с плавающей точкой в число

results = float (num_int) # преобразование чиса в число с плавающей точкой
print (results)

num_bool_true = True # логичсекая правда
num_bool_false = False #логическая не правда

results = bool (num_bool_true)
print (results)

my_list = [1,2,3]
my_tuple = tuple (my_list)
print (my_tuple)  # преобразование списка в кoртеж

my_dict = {"name": "max", "age": 24} # словарь
print (my_dict)

my_list_1 = [1,2,3,4,5,6,7,8,9,10]
results_dict = {f"key_{i+1}": num for i, num in enumerate(my_list_1)} # преобразование списка в словарь
