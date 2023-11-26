
n = int(input())
result = 0

for char in range(n):
    char = input()
    ascii_char = ord(char)
    result += ascii_char

print(f"The sum equals: {result}")