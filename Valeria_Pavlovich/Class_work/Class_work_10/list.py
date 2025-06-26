a = [1, 2, 3]
b = a
b.append(4)
print(a)

empty1 = []
empty2 = list()
print(empty2)

chars = list('abcde')
nums = list(range(5))
print(chars)
print(nums)

evens = [x for x in range(10) if x % 2 == 0]
print(evens)

pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)
