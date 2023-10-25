import sys
biggest = sys.maxsize
smallest = -sys.maxsize

n = int(input())
for i in range(0, n):
    number = int(input())
    if number > smallest:
        smallest = number
    if number < biggest:
        biggest = number

print(f"Max number: {smallest}")
print(f"Min number: {biggest}")