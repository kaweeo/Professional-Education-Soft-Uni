
input_string = input()

splited_string_turns_into_list = input_string.split(" ")

inverted_values = []
for element in splited_string_turns_into_list:
    element = -int(element)
    inverted_values.append(element)

print(inverted_values)