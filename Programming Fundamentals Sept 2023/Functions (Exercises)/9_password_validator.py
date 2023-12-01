def password_validator():

    user_input = input()
    flag1 = False
    flag2 = False
    flag3 = False

    if len(user_input) < 6 or len(user_input) > 10:
        print(f"Password must be between 6 and 10 characters")
    else:
        flag1 = True
    is_alphanumeric = all(char.isalpha() or char.isdigit() for char in user_input)
    if not is_alphanumeric:
        print(f"Password must consist only of letters and digits")
    digits = []
    for char in user_input:
        if char.isdigit():
            digits.append(char)
    else:
        flag2 = True
    if len(digits) < 2:
        print(f"Password must have at least 2 digits")
    else:
        flag3 = True
    if flag1 and flag2 and flag3 == True:
        print("Password is valid")

password_validator()


#######################################


def password_validator(some_password:str) -> list:
    list_of_errors = []
    if len(some_password) < 6 or len(some_password) > 10:
        list_of_errors.append("Password must be between 6 and 10 characters")
    if not some_password.isalnum():
        list_of_errors.append("Password must consist only of letters and digits")
    digits = []
    for char in password:
        if char.isdigit():
            digits.append(char)
    if len(digits) < 2:
        list_of_errors.append("Password must have at least 2 digits")
    return list_of_errors


password = input()

errors_in_password = password_validator(password)
if len(errors_in_password) == 0:
    print("Password is valid")
else:
    print("\n".join(errors_in_password))