#def name(name):
 #   print(f'Имя мое, {name}')
#name('Nastya')


#def calculate_tax(price):
 #   return price * 0.2

#calculate_tax(1000)

#total = calculate_tax(1000) + 1000
#print(total)

#def process_data(data):
   # cleaned = clean(data)
  #  analized = analize(cleaned)
 #   return report(analized)

#process_data(1000)


#def mat(num):
 #   return num * 1000

#def deli(num):
 #   return num / 10

#def calculator(num):
   # perremenay1 = mat(num)
  #  perremenay2 = deli(perremenay1)
 #   print(perremenay2)

#calculator(1000)


#def name(name):
 #   return name

#def fam(fam):
 #   return fam

#def full():
   # first = name("Nastya")
  #  last = fam("Кuprianchik")
 #   print(f'Меня зовут, {first} {last} !')
#full()



#import math
#print(math.sqrt(25))
#print(math.pi)
#print(math.factorial(5))
#print(math.log(1))
#print(math.sin(60))

#import random
#print(random.randint(1, 10))
#print(random.choice(['a', 'b', 'c']))
#results = [1, 2, 3]
#random.shuffle(results)
#print(results)

#def имя_функции(фргумент):
 #   """Документация описание функции"""
  #  тело функции
   # return результат

#def power(base, exponent):
 #   return base ** exponent
#power(2, 3)

#power(exponent=3, base=2)

#def power_2(base, exponent):
 #   return base ** exponent
#power_2(3)

#def min_max(numbers):
 #   return min(numbers), max(numbers)
#min_val, max_val = min_max([1, 2, 3])


from datetime import datetime
now = datetime.now()
print(now.strftime('%d, %m, %Y'))
now_h = datetime.now().minute
print(now_h)

#import requests
#response = requests.get('http://hoster.by')
#print(response.status_code)

