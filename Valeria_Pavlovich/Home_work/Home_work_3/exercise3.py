import re
password = input("Enter your password: ")
is_valid = True
if len(str(password)) < 8:
    print("Password must be at least 8 characters long")
    is_valid = False
if not re.search(r'\d', password):
    print("Password must contain at least one digit")
    is_valid = False
if not re.search("[A-Z]", password):
    print("Password must contain at least one uppercase letter")
    is_valid = False
if not re.search("[!@#$%^&*]", password):
    print("Password must contain at least one special character")
    is_valid = False
if is_valid:
    print("Your password is correct")
