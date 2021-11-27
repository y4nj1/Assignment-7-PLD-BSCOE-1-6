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
password = input("Enter your password here: ")

# 2. check for capital letters, numbers, special characters
charcount = len(password)

upper, lower, digit, special = 0, 0, 0, 0

if (len(password) >= 15):
    for i in password:
        if(i.isupper()):
            upper += 1
        if(i.islower()):
            lower += 1
        if(i.isdigit()):
            digit += 1
        if(i == "!" or i == "#" or i == "$" or i == "%" or i == "&" or i == "'" or i == "()" or i == "*" or i== "+ " or i == "." \
        or i == "/" or i == "`" or i == "," or i == ":" or i == ";" or i == "<" or i == "=" or i == ">" or i == "?" or i == "@" \
        or i == """^""" or i == """|""" or i == "~" or i == "{" or i == "}" or i == "_" ):
            special += 1
else:
    if (lower >= 1 and upper >= 1 and special >= 1 and digit >= 1):
        print("Valid Password")
    else:
        print("Invalid Password")             


