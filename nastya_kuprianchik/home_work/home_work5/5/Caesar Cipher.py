import string

def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char in string.ascii_lowercase:
            index = (string.ascii_lowercase.index(char) + shift) % 26
            result.append(string.ascii_lowercase[index])
        elif char in string.ascii_uppercase:
            index = (string.ascii_uppercase.index(char) + shift) % 26
            result.append(string.ascii_uppercase[index])
        else:
            result.append(char)
    return ''.join(result)
print(caesar_cipher("Hello, World!", 3))   # Khoor, Zruog!
print(caesar_cipher("XYZ", 4))             # BCD
print(caesar_cipher("Khoor, Zruog!", -3))  # Hello, World!
