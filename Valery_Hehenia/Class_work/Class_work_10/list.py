a = [1,2,3]
b=a
b.append(4)
print(a)

empty = []
empty1 = list()

numbers = [1,2,3]
mixed = [10,"hello", True, 32.2]

chars = list("abcdefghij")  #[a,b,c,d....]
nums = list(range(5)) #[0,1,2,3,4]

squares = [x**2 for x in range(5)] # [0,1,4,9,16]

evens = [x for x in range(10) if x%2==0] #[0,2,4,6,8]

pairs = [(x,y) for x in [1,2] for y in [3,4]] # [(1,3),(1,4),(2,3),(2,4)]

