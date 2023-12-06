
user_input = input()

list_of_string =  user_input.split(" ")
characterized_string = []
for string in list_of_string:
    digits = ""
    only_char_str = ""
    for char in string:
        if char.isdigit():
            digits += char
        else:
            only_char_str += char
    char_digit = chr(int(digits))
    char_string = char_digit + only_char_str
    characterized_string.append(char_string)

swapped_strings = [''.join([s[0]] + [s[-1]] + list(s[2:-1]) + [s[1]]) if len(s) > 2 else s for s in characterized_string]  #
[print(item, end=" ") for item in swapped_strings]