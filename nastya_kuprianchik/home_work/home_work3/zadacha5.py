dohod = float(input('Введите свой доход: '))

if dohod <= 20000 :
    tax = dohod * 0.10
    print("Налог составит:", tax)
elif 20000 < dohod <= 50000:
    tax = (dohod - 20000)  * 0.20
    print("Налог составит:", tax)
else :
    tax = 5000 + (dohod - 50000) * 0.30
    print("Налог составит:", tax)
