word = input('Enter a word: ')
letter_example = input('Enter a letter: ')
count = 0
for letter in word:
    if letter.lower() == letter_example.lower():
        count += 1
if count == 0:
    print(f'The word {word} does not have letter {letter_example}')
elif count == 1:
    print(f'The word {word} has {count} letter {letter_example}')
else:
    print(f'The word {word} has {count} letters {letter_example}')
total_letters = len(word.lower())
count_one = word.lower().count(letter_example.lower())
percent_letter = count_one / total_letters * 100
print(f'Total number of letters in the word {word}: {total_letters}')
print(f'The percentage of letter {letter_example} in the word {word}: {percent_letter:.2f}%')
