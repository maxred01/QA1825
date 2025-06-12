text = "Hello Word! Привет, Мир! 123"

# Поиск и проверка содержимого
# 'in' и 'not in' ( операторы, не методы )
print("Hello" in text) # true проверка подстроки
print("Mars" not in text) # true

# .startswith(prefix) -> bool
print(text.startswith("Hello"))
print(text.startswith("Hi", "Byi"))

# endswith(prefix)) -> bool
print(text.endswith("123"))
print(text.startswith(".", "!", "?")) # Кортеж суффиксов

#
#
print(text.find("World")) # 6
print(text.find("o")) # 4 (первые "o")
print(text.find("o", 5)) # 7 (ищем "o" начиная с индекса 5)

print(text.find("Pyton")) # -1 (не найдена в переменной)









