
initial_list = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break
    else:
        command = command.split(" ")
        action = command[0]
        item = command[1]

        if action == "Urgent":
            if item not in initial_list:
                initial_list.insert(0, item)

        elif action == "Unnecessary":
            if item in initial_list:
                initial_list.remove(item)

        elif action == "Correct":
            new_item = command[2]
            if item in initial_list:
                index_of_change = initial_list.index(item)
                initial_list[index_of_change] = new_item

        elif action == "Rearrange":
            if item in initial_list:
                index_of_change = initial_list.index(item)
                popped_item = initial_list.pop(index_of_change)
                initial_list.append(popped_item)
for item in initial_list:
    if item == initial_list[-1]:
        print(item)
    else:
        print(item, end=", ")