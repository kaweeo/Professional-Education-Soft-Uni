
concealed_message = input()

command_line = input()

while command_line != "Reveal":
    command_line_list = command_line.split(":|:")
    command = command_line_list[0]
    if command == "InsertSpace":
        index = int(command_line_list[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif command == "Reverse":
        substring = command_line_list[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message = concealed_message + substring[::-1]
            print(concealed_message)
        else:
            print("error")
    elif command == "ChangeAll":
        substring = command_line_list[1]
        replacement = command_line_list[2]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
    command_line = input()

print(f"You have a new text message: {concealed_message}")