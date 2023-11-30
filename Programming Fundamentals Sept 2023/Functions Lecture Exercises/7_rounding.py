
input_list = input().split()

input_list = list(map(float, input_list))

round_list = [round(x) for x in input_list]

print(round_list)