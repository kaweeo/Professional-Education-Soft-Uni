def move(count_indexes: int, string: str)->str:
    sub_string_slice = string[0:count_indexes]
    string = string[count_indexes:]
    string += sub_string_slice
    return string


def inserter(index: int, value, string: str)->str:
    string = string[:index] + value + string[index:]
    return string


def changer(substring, replacement, string)->str:
    string = string.replace(substring, replacement)
    return string


encrypted_input = input()

while True:
    command = input()
    if command == "Decode":
        break
    else:
        action = command.split("|")
        if action[0] == "Move":
            first_n_letters = int(action[1])
            encrypted_input = move(first_n_letters, encrypted_input)
        elif action[0] == "Insert":
            index_to_insert = int(action[1])
            value_to_insert = action[2]
            encrypted_input = inserter(index_to_insert, value_to_insert, encrypted_input)
        elif action[0] == "ChangeAll":
            substr_to_replace = action[1]
            replacement_to_set = action[2]
            encrypted_input = changer(substr_to_replace, replacement_to_set, encrypted_input)

print(f"The decrypted message is: {encrypted_input}")