from currency_converter import convert

print(convert(100, "USD", "EUR"))     # 93.0
print(convert(5000, "JPY", "GBP"))    # ≈26.54
print(convert(100, "USD", "ABC"))     # вызывает ошибку
