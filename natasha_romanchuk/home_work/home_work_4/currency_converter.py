RATES = {
     "USD": 1.0,
     "EUR": 0.93,
     "GBP": 0.79,
     "JPY": 148.86
 }

def convert(amount, from_curr, to_curr):
    if from_curr not in RATES or to_curr not in RATES:
        raise ValueError("Неверный код валюты")
    return round(amount / RATES[from_curr] * RATES[to_curr], 2)
