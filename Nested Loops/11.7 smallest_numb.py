import sys

smallest_number = sys.maxsize
while True:
    number = input()
    if number == "Stop":
        break
    if int(number) < smallest_number:
        smallest_number = int(number)
print(smallest_number)