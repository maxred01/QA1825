num_str = '123' # строка
num_int = int(num_str) # число
num_float = 12.3 # дробное число
num_bool_true = True # Логическое правда
num_bool_false = False # Логическое не правда

my_list = [1, 2, 3] # список,  всегда  кваратными скобками
my_tupe = (1, 2, 3)
my_dict = {"name": "max", "age": 30} # словарь

price = str(100) + "$"
print(price)


results_dict = {f"key_{i+1}": num for i, num in enumerate(my_list)}  # перевести список в словарь
results_dict_v2 = {num: num ** 2 for num in my_list}
print(results_dict)
print(results_dict_v2)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # приобразовать из списка в словарь(невозможно)
results = {dict(my_list)}
print(results)




print(list(my_dict.values()))

print(list(my_tupe)) # приобразования кортеж в список

my_tuple = tuple(my_list) # приобразовали список в кортеж

results = (bool(""))
print(results)

results = str(num_bool_true)
print(results)

results = int(num_bool_true) # приоброзование строки в число
res = int(num_bool_false)
print(results, res)

num_int_str = int(num_str) # приоброзование строки в число
results = str(num_float) # приоброзование строки в число
print(results)

# приоброзовать число в строку
num_int = 100500
results = str(num_int)
print(results)

# приоброзовать дробное числов число
num_float = 12.3
res = int(num_float)
print(res)


