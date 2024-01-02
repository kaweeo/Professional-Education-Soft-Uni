import re

string = input()
searched_word = input()

pattern = fr'(?i)\b{searched_word}\b'
matches = re.findall(pattern, string)

print(len(matches))