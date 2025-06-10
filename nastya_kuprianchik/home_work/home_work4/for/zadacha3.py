text = str(input('Введите текст: '))
letter = input('Введите букву: ')
count = 0
for char in text:
    if char.lower() == letter.lower():
        count=count+1
print(f'Буква {letter} встречается {count} раз')
