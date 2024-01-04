import re

piece_of_string = input()

cool_threshold = 1
for char in piece_of_string:
    if char.isdigit():
        cool_threshold *= int(char)

#pattern = r'([:*]{2})(\b[A-Z][a-z]{2,})\1'
#pattern = r'([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)'
pattern = r'([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})\1'   #explicitly one sign 2 times or the other 2 times
matches = re.findall(pattern, piece_of_string)

valid_imot_icons = []
for match in matches:
    valid_imot_icons.append(match[1])

print(f"Cool threshold: {cool_threshold}")
print(f"{len(valid_imot_icons)} emojis found in the text. The cool ones are:")

if matches:
    for match in matches:
        coolness = 0
        for char in match[1]:
            coolness += ord(char)
        if coolness >= cool_threshold:
            print(f"{match[0]}{match[1]}{match[0]}")
