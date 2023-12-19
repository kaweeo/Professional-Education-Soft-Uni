
char_list = input().split(", ")

dict = {char: ord(char) for char in char_list}

print(dict)