text = "Hello World! Привет, Мир! 123"

#Поиск и проверка содержимого
# `in` и `not in` (операторы, не методы)
print("Hello" in text) # True - проверка подстроки
print("Mars" not in text) # True

# .startswith(prefix) -> bool
print(text.startswith("Hello"))  # True начинается ли строка с префикса?
print(text.startswith("Hi", "Bye")) # False - Можно передать кортеж префиксов

#.endswith(suffix) -> bool
print(text.endswith("123")) #True - заканчивается ли строка суфиксом?
print(text.endswith(".", "!", "?")) # True - Кортеж суффиксов

#.find(sub[, start[, end]]) -> int
#Поиск ПОДСТРОКИ `sub`. Возвращает индекс ПЕРВОГО вхождения или -1
print(text.find("World")) # 6
print(text.find("o")) # 4(первое 'о')
print(text.find("o",5)) # 7 (ищем 'о' начиная с индекса 5)

print(text.find("Python")) # -1 (не найден)

#.rfind(sub[, start[, end]]) -> int


