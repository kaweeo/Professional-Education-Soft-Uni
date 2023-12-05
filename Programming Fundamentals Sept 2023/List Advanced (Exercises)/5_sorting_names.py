
names_input = input()
names_list = names_input.split(", ")

sorted_list = sorted(names_list, key=lambda x: (-len(x), x))
print(sorted_list)