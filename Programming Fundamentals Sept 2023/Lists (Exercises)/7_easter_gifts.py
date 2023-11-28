
input_string = input()
string_list = input_string.split(" ")

while True:
    command = input()
    if command == "No Money":
        break
    else:
        command = command.split(" ")
        if command[0] == "OutOfStock":
            item = command[1]
            for element in string_list:
                if element == item:
                    index_to_replace = string_list.index(element)
                    string_list[index_to_replace] = "None"
        elif command[0] == "Required":
            item = command[1]
            index_check = int(command[2])
            if 0 < index_check < len(string_list):
                index_change = index_check
                string_list[index_change] = item
        elif command[0] == "JustInCase":
            item = command[1]
            string_list[-1] = item

for item in string_list:
    if item != "None":
        print(item, end=" ")