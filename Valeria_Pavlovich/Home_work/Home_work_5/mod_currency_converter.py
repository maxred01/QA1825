RATES = {
    "USD": 1.0,
    "EUR": 0.93,
    "GBP": 0.79,
    "JPY": 148.86
}
def convert(amount, from_curr, to_curr):
    if from_curr not in RATES or to_curr not in RATES:
        return None
    usd_amount = amount / RATES[from_curr]
    converted_amount = usd_amount * RATES[to_curr]
    return converted_amount
