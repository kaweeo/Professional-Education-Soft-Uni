string_input = input()
count = int(input())

output_list = string_input.split(", ")
output_list = [int(i) for i in output_list]
sums = [sum(output_list[i::count]) for i in range(count)]

print(sums)