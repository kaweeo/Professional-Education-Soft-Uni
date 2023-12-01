user_input = input()
numbers = user_input.split(" ")
numbers = [int(number) for number in numbers]
def is_even(x):
    return x % 2 == 0
even_numbers = filter(is_even, numbers)
print(list(even_numbers))