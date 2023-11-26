
start = int(input())
stop = int(input())
result = ""
for char in range(start, stop + 1):
    char_string = str(chr(char))
    result += char_string
    result += " "
print(result)
