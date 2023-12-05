numbers = input().split(", ")
index_of_even_numbrs = [numbers.index(number) for number in numbers if int(number) % 2 == 0]
print(index_of_even_numbrs)