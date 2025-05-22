num_str = '123'  # строка
num_int = 123    # число
num_float = 12.3   # дробное число
num_bool_true = True
num_bool_false = False

my_list = [1,2,3,4,5,6,7,8,9,10] # список
my_tuple = (1,2,3) # кортеж
my_dict = {"name": "max", "age": 30} # словарь

print(list(my_dict))

results_dict = {f"key_{i+1}": num for i, num in enumerate(my_list)} #преобразовать список в словарь
results_dict_v2 = {num: num ** 2 for num in my_list} #преобразовать список в словарь
print(results_dict)



#results = str(num_float)
#print(results)

#num_int = 100500
#results = str(num_int)
#print(results)

# преобразовать число в строку

#num_float = 12.5
#results = int(num_float)
#print(results)

#num_bool_true = True
#num_bool_false = False
#results = int(num_bool_false)
#print(results)

#num_int =123
#results = float(num_int)
#print(results)

#num_str ='123.2'
#results = float(num_str)
#print(results)