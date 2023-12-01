user_input = input()
numbers = user_input.split(" ")
numbers = [int(number) for number in numbers]

print(sorted(numbers))