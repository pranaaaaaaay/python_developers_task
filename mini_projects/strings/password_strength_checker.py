# Password Strength Checker

password = input("Enter your password: ")

upper = False
lower = False
digit = False
special = False

for i in password:
    if i.isupper():
        upper = True
    elif i.islower():
        lower = True
    elif i.isdigit():
        digit = True
    else:
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("Strong Password")
elif len(password) >= 6 and (upper or lower) and digit:
    print("Medium Password")
else:
    print("Weak Password")
