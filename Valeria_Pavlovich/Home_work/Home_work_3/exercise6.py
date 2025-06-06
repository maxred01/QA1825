age = int(input('Enter your age: '))
if age < 12:
    print('Only cartoons are available')
else:
    time = input('Enter the time - morning or evening: ').lower()
    genre = input('Enter your favourite genre - comedy/fantasy/horror: ').lower()
    if time.lower() == 'morning':
        if genre.lower() == "comedy":
            print('Choose one of the following comedies')
        else:
            print('Comedies are recommended in the morning.')
    else:
        print('Choose any film')
