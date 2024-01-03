
init_string = input()

command_input = input()
while command_input != "Done":
    command_input_list = command_input.split(" ")
    command = command_input_list[0]
    if command_input == "TakeOdd":
        new_raw_string = []
        for i in range(len(init_string)):
            if i % 2 != 0:
                new_raw_string.append(init_string[i])
        init_string = ""
        for char in new_raw_string:
            init_string += char
        print(init_string)
    if command == "Cut":
        index = int(command_input_list[1])
        length = int(command_input_list[2])
        init_string = init_string[:index] + init_string[index + length:]
        print(init_string)
    elif command == "Substitute":
        substring = command_input_list[1]
        substitute = command_input_list[2]
        if substring in init_string:
            init_string = init_string.replace(substring, substitute)
            print(init_string)
        else:
            print("Nothing to replace!")
    command_input = input()
print(f"Your password is: {init_string}")