num_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
result = {index: value for index, value in enumerate(num_list)}
print (result)

words = ['Hello', 'world', 'Python']
words_python = 'Python'
words_python_split = 'Hello-world-Python'
result_1 = '-'.join(words_python)
result_2 = words_python_split.split('-')
print(result_1)
print(result_2)
print(result_2[0])