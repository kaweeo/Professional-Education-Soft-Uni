

string1 = input()
string2 = input()
transformed = ""


for i in range(len(string1)):
    if string1[i] != string2[i]:
        transformed += string2[i]
    else:
        transformed += string1[i]
print(transformed)

###################################### 

first_string = input()
second_string = input()
last_printed_string = first_string
for character_index in range(len(first_string)):
    left_part = second_string[:character_index + 1]
    right_part = first_string[character_index + 1:]
    new_string = left_part + right_part
    if new_string != last_printed_string:
        print(new_string)
        last_printed_string = new_string