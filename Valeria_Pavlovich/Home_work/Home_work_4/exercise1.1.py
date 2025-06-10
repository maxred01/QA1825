number = int(input("Enter a number: "))
if number < 0:
    print("The number cannot be negative.")
else:
    for i in range(1, number + 1):
        print(i, end=' ')
    print()
    for i in range(number, 0, - 1):
        print(i, end=' ')
