# currency_converter.py

RATES = {
    "USD": 1.0,
    "EUR": 0.93,
    "GBP": 0.79,
    "JPY": 148.86
}

def convert(amount, from_curr, to_curr):
    if from_curr not in RATES:
        raise ValueError(f"Неверный код валюты: {from_curr}")
    if to_curr not in RATES:
        raise ValueError(f"Неверный код валюты: {to_curr}")
    usd_amount = amount / RATES[from_curr]
    result = usd_amount * RATES[to_curr]
    return round(result, 2)
