
raw_activation_key = input()

command_input = input()
while command_input != "Generate":
    command_input_list = command_input.split(">>>")
    command = command_input_list[0]
    if command == "Contains":
        substring = command_input_list[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command == "Flip":
        case = command_input_list[1]
        startIndex = int(command_input_list[2])
        endIndex = int(command_input_list[3])
        if case == "Upper":
            raw_activation_key = raw_activation_key[0:startIndex] + raw_activation_key[startIndex:endIndex].upper() + raw_activation_key[endIndex:]
        elif case == "Lower":
            raw_activation_key = raw_activation_key[0:startIndex] + raw_activation_key[startIndex:endIndex].lower() + raw_activation_key[endIndex:]
        print(raw_activation_key)
    elif command == "Slice":
        startIndex = int(command_input_list[1])
        endIndex = int(command_input_list[2])
        raw_activation_key = raw_activation_key[0:startIndex] + raw_activation_key[endIndex:]
        print(raw_activation_key)

    command_input = input()
print(f"Your activation key is: {raw_activation_key}")