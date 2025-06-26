a = [1, 2, 3]
b = a#копирование ссылки
b.append(4) #добавление
print(a)# [1, 2, 3, 4] - изменился исходный объект

empty = []
empty1 = list()#способы создать пустой список

numbers = [1, 2, 3, 4, 5]
mixed = [10, 'hello', True, 3.14]

chars = list('abcde') #['a', 'b', 'c', 'd', 'e']
nums = list(range(5)) #[0, 1, 2, 3, 4]


pairs = [(x, y) for x in [1, 2] for y in [3,4]]
#[(1, 3), (1, 4), (2,3), (2, 4)]

my_list = [10, 20, 30]
print(my_list[1:3])
print(my_list[::-1])

new_list = my_list + [40, 50]

