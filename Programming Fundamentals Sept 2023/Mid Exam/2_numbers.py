
numbers = input().split(" ")

while True:
    command = input()
    if command == "Finish":
        break
    else:
        command = command.split(" ")
        action = command[0]
        value = command[1]

        if action == "Add":
            numbers.append(value)

        elif action == "Remove":
            if value in numbers:
                numbers.remove(value)

        elif action == "Replace":
            replacement = command[2]
            if value in numbers:
                index = numbers.index(value)
                numbers[index] = replacement

        elif action == "Collapse":
            numbers = [number for number in numbers if int(number) >= int(value)]

print(" ".join(numbers))
