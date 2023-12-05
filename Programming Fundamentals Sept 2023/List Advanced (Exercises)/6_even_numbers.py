user_input = input()

numbers_list = list(map(int, user_input.split(", ")))

found_indeces_or_no = map(
    lambda x: x if numbers_list[x] % 2 == 0 else "no",
    range(len(numbers_list))
)

even_indeces = list(filter(lambda a: a != "no", found_indeces_or_no))
print(even_indeces)