text = "Hello World! Привет, Мир! 123"

print("Hello" in text)
print("Mars" not in text)

print(text.startswith("Hello"))
print(text.startswith(("Hi", "Bye")))

print(text.endswith("123"))
print(text.endswith((".", "!", "?")))

print(text.find("World")) # index of the first letter
print(text.find("o")) # index of the first O
print(text.find("o", 5)) # search starts with index 5

print(text.find("Python")) # word does not exist in var

