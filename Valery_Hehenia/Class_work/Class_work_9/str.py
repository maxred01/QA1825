text = "Hello World! Привет, мир! 123"

print ("Hello" in text) #True - проверка подстроки
print("Mars" is not text) # True


# .startswich(prefix) ->bool
print(text.startswith("Hello")) #True - Начинается ли строка с префикса
print(text.startswith("Hi, Bye")) #False - Можно передать кортеж префиксов


# .endswich(suffix) -> bool
print(text.endswith("123")) #True  Заканчивается ли строка суффиксом
print(text.endswith(".", "!", "?")) # True - Кортеж суффиксов


# .find(sub[,start[,end]]) ->int
#Поиск ПОДСТРОКИ 'sub' Возвращает индекс ПЕРВОГО вхождения или -1
print(text.find("World")) #6
print(text.find("o")) #4 (первое 'o')
print(text.find("o", 5)) #(ищем 'o' начиная с индекса 5)
print(text.find("Python")) # -1 (не найдено)


print(text.rfind("o")) #работает только с обратной стороны




