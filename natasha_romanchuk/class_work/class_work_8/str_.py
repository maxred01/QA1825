text = 'Hello World! Привет, Мир! 123'

# Поиск и проверка содержимого
# 'in'  и 'not in'  (Операторы, не методы)
print('Hello' in text )  # True - проверка подстроки
print('Mars' not in text )  # True

#  .startswith(prefix)  -> bool
print(text.startswith('Hello')) # True - Начинается ли строка с префикса?
print(text.startswith(('Hi', 'By'))) # False - Можно передать кортеж префиксов

#  .endswith(suffix)  -> bool
print(text.endswith('123')) # True - Заканчивается ли строка суффиксом?
print(text.endswith(('.', '!','?'))) # True - Кортеж суффиксов


#  .find(sub[, start[, end]]) -> int
#  Поиск ПОДСТРОКИ  'sub' . Возвращает индекс ПЕРВОГО вхождения или -1.
print(text.find('World'))  # 6
print(text.find('0'))      # 4 (первое '0')
print(text.find('0', 5))   # 7 (ищем '0' начиная с индекса 5)

print(text.find('Puthon'))  # -1 не найден






