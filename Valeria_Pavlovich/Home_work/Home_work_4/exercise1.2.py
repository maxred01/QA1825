numbers = list(map(int, input('Enter numbers: ').split()))
number_sum = sum(numbers)
even_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num
print(f'Total sum: {number_sum}')
print(f'Sum of even numbers: {even_sum}')
