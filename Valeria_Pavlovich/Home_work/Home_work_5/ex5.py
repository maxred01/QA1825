import string
def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                alphabet = string.ascii_lowercase
            else:
                alphabet = string.ascii_uppercase
            start_index = alphabet.find(char)
            shifted_index = (start_index + shift) % 26
            shifted_char = alphabet[shifted_index]
            result += shifted_char
        else:
            result += char
    return result
text = input('Enter the text: ')
shift = int(input('Enter the number: '))
print(caesar_cipher(text, shift))