user_input = input()
numbers = user_input.split(", ")
numbers = [int(number) for number in numbers]

for number in numbers:
    str_check = str(number)
    length = len(str_check)
    mid = length // 2
    first_half = str_check[:mid]

    # Determine where to start the second half based on the string length
    if length % 2 == 0:
        second_half = str_check[mid:]
    else:
        second_half = str_check[mid + 1:]

    second_half = second_half[::-1]

    if first_half == second_half:
        print(True)
    else:
        print(False)


###############################

def is_palindrome(some_number: str) -> bool:
    return some_number == some_number[::-1]

numbers = input().split(", ")
for number in numbers:
    print(is_palindrome(number))