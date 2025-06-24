history = []
while True:
    operation = input('Enter the operation (+, -, *, /, **, exit): ')
    if operation.lower() == 'exit':
        print('Stop!')
        print('Operation history: ')
        for entry in history:
            print(entry)
        break
    num_1 = float(input('Enter the first number: '))
    num_2 = float(input('Enter the second number: '))
    if operation == '+':
        result = num_1 + num_2
    elif operation == '-':
        result = num_1 - num_2
    elif operation == '*':
        result = num_1 * num_2
    elif operation == '/':
        if num_2 == 0:
            print('You cannot divide by zero!')
            continue
        result = num_1 / num_2
    elif operation == '**':
        result = num_1 ** num_2
    if result is not None:
        print('Result: ', result)
        history.append(f'{num_1} {operation} {num_2} = {result}')
    print(result)
