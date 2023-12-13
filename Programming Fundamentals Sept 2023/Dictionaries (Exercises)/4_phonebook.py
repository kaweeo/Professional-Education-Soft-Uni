
phone_book = {}

while True:
    input_line = input()
    if "-" in input_line:
        record = input_line.split("-")
        name = record[0]
        phone_book[name] = record[1]
    else:
        break

number = int(input_line)

for name in range(number):
    searching_name = input()
    if searching_name in phone_book.keys():
        print(f"{searching_name} -> {phone_book[searching_name]}")
    else:
        print(f"Contact {searching_name} does not exist.")