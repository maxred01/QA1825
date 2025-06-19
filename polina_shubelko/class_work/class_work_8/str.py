text = "Hello World! Привет, Мир! 123"

print("Hello" in text)
print("Mars" not in text)

print(text.startswith("Hello"))
print(text.endswith(("Hi", "Bye")))

print(text.endswith("123"))
print(text.endswith((".", "!", "?")))

print(text.find("World"))
print(text.find("o"))
print(text.find("o", 5))

print(text.find("Python")) # -1 (не найдено)

# .lower - нижний регистр (все буквы маленькие)
# .upper - верхний регистр (все буквы большие)
# .title - первая буква каждого слова в верхнем регистре
# .swapcase - меняет регистр каждой буквы на противоположный
# .strip - удаляет пробельные символы
# .center - центрирует строку в поле
# .ljust - выравнивает строку по левому краю
# .rjust - выравнивает строку по правому краю
# .replace - заменяет все вхождения подстроки "old" на "new"

