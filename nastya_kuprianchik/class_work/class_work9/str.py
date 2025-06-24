text = 'Hello Word! Привет, Мир! 123'

#Поиск и проверка содержимого
# 'in' и 'not in' (операторы, не методы)
print('Hello' in text)# True - проверка подстроки
print('Mars' not in text) # True


#.startswitch(prefix)-> bool
print(text.startswith('Hello'))# True - начинается ли строка с префикса?
print(text.startswith('Hi', 'Bye'))# False - можно передать кортеж префиксом

#.endswitch(suffix) -> bool
print(text.startswith('123'))#True-заканчивает ли строка суффиксом?
print(text.endswith('.', '!', '?'))#True -кортеж суффиксов

#.find(sub[, start[, end]]) -> int
#поиск ПОДСТРОКИ 'sub'. Возвращает индекс ПЕРВОГО вхождения или -1
print(text.find('Word'))#6
print(text.find('o'))#4 (первое 'o')
print(text.find('o', 5))# 7 (ищет 'o' начиная с индекса 5

print(text.find('Python'))#-1 (не найдено)


print(text.find('o'))
print(text.rfind('Мир'))

try:
    print(text.index('Python'))
except ValueError:
    print('Подстрока не найдена')
