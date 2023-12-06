
substrings = input()
strings = input()

substrings_list = substrings.split(", ")
strings_list = strings.split(", ")

# valid_substrings = [substring for string in strings_list for substring in substrings_list if substring in string]
# valid_substrings = list(set(valid_substrings))

valid_substrings = []

for substring in substrings_list:
    for string in strings_list:
        if substring in string:
            valid_substrings.append(substring)
            break

print(valid_substrings)