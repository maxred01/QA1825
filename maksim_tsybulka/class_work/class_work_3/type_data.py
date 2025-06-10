num_str = '123.2'  # строка
num_int = 123  # число
num_float = 12.3  # дробное число
num_bool_true = True  # логическая правда
num_bool_false = False  # логическая не правда

my_list = [1, 2, 3]  # Список
my_tuple = (1, 2, 3)  # кортеж
my_dict = {"name": "max", "age": 30}  # словарь

print(list(my_dict.values()))


# приобразовали список в словарь. Для этого создайте список из 10 значений (числа)
results_dict = {f"key_{i+1}": num for i, num in enumerate(my_list)}
results_dict_v2 = {num: num ** 2 for num in my_list}
print(results_dict)
print(results_dict_v2)


price = str(100) + "$"
print(price)


num = int(float("5.8"))
print(num)

print(bool([]))

