numbers = list(map(int, input('Enter numbers: ').split()))
max_number = numbers[0]
min_number = numbers[0]
max_index = 0
min_index = 0
for index, num in enumerate(numbers):
    if num > max_number:
        max_number = num
        max_index = index
    if num < min_number:
        min_number = num
        min_index = index
print(f'The largest number is: {max_number}')
print(f'The smallest number is: {min_number}')
print('The index of the largest number is:', max_index)
print('The index of the smallest number is:', min_index)
