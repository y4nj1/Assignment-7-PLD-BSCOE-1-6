# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex.
# input: P@ssw0rd+P@ssw0rd
# output: Valid
# Tip: loop through each character of the input then process it letter by letter

# steps:
# 1. ask for password
password = input("\33[1m\33[3m\33[35mEnter your password here:\33[0m ")

# 2. check for capital letters, numbers, special characters
charcount = len(password)

upper, lower, digit, special = 0, 0, 0, 0


if charcount >= 15:
    for i in password:
        if(i.isupper()):
            upper += 1
        if(i.islower()):
            lower += 1
        if(i.isdigit()):
            digit += 1
        if(i == "!" or i == "#" or i == "$" or i == "%" or i == "&" or i == "'" or i == "(" or i == """)""" or i == "*" or i== "+ " or i == "." \
        or i == "/" or i == "`" or i == "," or i == ":" or i == ";" or i == "<" or i == "=" or i == ">" or i == "?" or i == "@" \
        or i == """^""" or i == """|""" or i == "~" or i == "{" or i == "}" or i == "_" or i == """+""" or i == " " or i == "-"):
            special += 1

    if (lower >= 1 and upper >= 1 and special >= 1 and digit >= 1):
        print("\33[1m\33[3m\33[32mValid Password\33[0m")
    if (upper < 1):
        print("\33[1m\33[3m\33[33mYour password must have at least 1 capital letter.\33[0m")     
    if (special < 1):
        print("\33[1m\33[3m\33[34mYour password must have at least 1 special character.\33[0m")
    if (digit < 1): 
        print("\33[1m\33[3m\33[36mYour password must have at least 1 number.\33[0m")
    if (lower < 1 or upper < 1 or special < 1 or digit < 1):
        print("\33[1m\33[3m\33[31mInvalid Password\33[0m")
else:    
    for i in password:
        if(i.isupper()):
            upper += 1
        if(i.islower()):
            lower += 1
        if(i.isdigit()):
            digit += 1
        if(i == "!" or i == "#" or i == "$" or i == "%" or i == "&" or i == "'" or i == "(" or i == """)""" or i == "*" or i== "+ " or i == "." \
        or i == "/" or i == "`" or i == "," or i == ":" or i == ";" or i == "<" or i == "=" or i == ">" or i == "?" or i == "@" \
        or i == """^""" or i == """|""" or i == "~" or i == "{" or i == "}" or i == "_" or i == """+""" or i == " " or i == "-"):
            special += 1
    print("\33[1m\33[3mYour password must have at least 15 characters.\33[0m")
    if (upper < 1):
        print("\33[1m\33[3m\33[33mYour password must have at least 1 capital letter.\33[0m")     
    if (special < 1):
        print("\33[1m\33[3m\33[34mYour password must have at least 1 special character.\33[0m")
    if (digit < 1): 
        print("\33[1m\33[3m\33[36mYour password must have at least 1 number.\33[0m")
    print("\33[1m\33[3m\33[31mInvalid Password\33[0m")