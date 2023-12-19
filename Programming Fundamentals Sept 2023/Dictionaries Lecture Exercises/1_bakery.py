
input_line = input().split()

my_bakery_dict = {}
for i in range(0, len(input_line), 2):
    key = input_line[i]
    value = input_line[i + 1]
    my_bakery_dict[key] = int(value)

print(my_bakery_dict)