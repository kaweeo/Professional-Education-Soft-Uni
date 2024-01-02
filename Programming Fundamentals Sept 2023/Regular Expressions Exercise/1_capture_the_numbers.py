import re

input_line = input()
while input_line:
    pattern = "\d+"
    matches = re.findall(pattern, input_line)
    if matches:
        print(" ".join(matches), end=" ")
    input_line = input()