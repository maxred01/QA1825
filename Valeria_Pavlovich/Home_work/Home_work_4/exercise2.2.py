total_sum = 0
total_count = 0
while True:
    number = int(input('Enter a number (enter 0 to stop): '))
    if number == 0:
        break
    total_sum += number
    total_count += 1
    avg = total_sum / total_count
print(f'Total sum is {total_sum}')
print(f'Total count is {total_count}')
print(f'Average is {avg:.2f}')
