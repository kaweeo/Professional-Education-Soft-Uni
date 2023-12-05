names = input().split(", ")

# Sort the names by length in descending order, and then by the name itself in ascending order.
sorted_names = sorted(names, key=lambda x: (-len(x), x))

print(sorted_names)