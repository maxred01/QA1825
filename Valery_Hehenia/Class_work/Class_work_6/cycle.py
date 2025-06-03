for _ in range(3):
    print('Привет')


words = ['яблоко', 'банан', 'вишня']
for word in words:
    print(word)




# while условие:
#     тело_цикла


count =0
while count <3:
    print(f'счет {count}')
    count+=1

for char in 'Python':
    print(char)


for num in range(1,101):
    print(num*10)


for num in range(10):
    if num == 5:
        break
    print(num)\



for num in range(3):
    if num == 1:
        continue
    print(num)
    print('break')


for num in range(3):
    print(num+1)
else:   # else выполнится всегда только в конце цикла
    print('done')


total = 0
for i in range(3):
    x=i*2
    total+=x
print(total)
print(x)

total = 0
num = int(input('vvedite chislo:'))
while num != 0:
    total += num
    num = int(input('sled. chislo:'))
print(f'Итого {total}')

names = ['Anna', 'Petr', 'Maria']
for name in names:
    if name == 'Petr':
        print('done')
        break


range1 = float(input('1: '))
range2 = float(input('2: '))
proc = 1.1
day=1

distance = range1

while distance <= range2:
    distance*=proc
    day+=1
print(day)


summa = float(input('summa1= '))
summa1 = float(input('summa2= '))
pricent = float(input('proc= '))

dist=0
year=0

while dist < summa1:
    year += 1
    result= (dist*pricent)/100
    dist+=result
    dist=int(dist)

print(year)
