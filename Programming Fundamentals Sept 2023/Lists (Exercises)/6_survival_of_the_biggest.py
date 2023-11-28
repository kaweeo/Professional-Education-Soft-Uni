
input_string = input()
n = int(input())


numbers_list = input_string.split()
numbers_list = [int(number) for number in numbers_list]

for _ in range(n):
    lowest_number = min(numbers_list)
    numbers_list.remove(lowest_number)

for i, num in enumerate(numbers_list):
    if i < len(numbers_list) - 1:
        print(num, end=', ')
    else:
        print(num)