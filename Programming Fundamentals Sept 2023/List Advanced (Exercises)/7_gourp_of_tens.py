#
# user_input = input()
# numbers = user_input.split(", ")
#
# # Create groups using list comprehensions
# groups = {
#     'Group of 10\'s': [int(num) for num in numbers if 0 < int(num) <= 10],
#     'Group of 20\'s': [int(num) for num in numbers if 10 < int(num) <= 20],
#     'Group of 30\'s': [int(num) for num in numbers if 20 < int(num) <= 30],
#     'Group of 40\'s': [int(num) for num in numbers if 30 < int(num) <= 40],
#     'Group of 50\'s': [int(num) for num in numbers if 40 < int(num) <= 50]
# }
#
# # Print the groups
# for group_name, group_numbers in groups.items():
#     if group_numbers:
#         print(f"{group_name}: {group_numbers}")
#     elif group_name == 'Group of 50\'s':
#         pass
#     else:
#         print(f"{group_name}: []")


user_input = input()
numbers = user_input.split(", ")
numbers = [int(num) for num in numbers]

# Initialize the group boundary and groups dictionary
group_boundary = 10
groups = {}

# Create groups based on the hints
while numbers:
    group_name = f"Group of {group_boundary}'s"
    groups[group_name] = [num for num in numbers if num <= group_boundary]
    numbers = [num for num in numbers if num > group_boundary]
    group_boundary += 10

# Print the groups
for group_name, group_numbers in groups.items():
    print(f"{group_name}: {group_numbers}")
