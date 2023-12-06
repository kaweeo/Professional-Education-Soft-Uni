

targets = [int(target) for target in input().split()]

while True:
    command = input()

    if command == "End":
        targets = "|".join(list(map(str, targets)))
        print(targets)
        break
    else:
        command = command.split(" ")
        action = command[0]
        index = int(command[1])

        if action == "Shoot":
            power = int(command[2])
            if 0 <= index and index < len(targets):
                targets[index] -= power
                if targets[index] <= 0:
                    targets.remove(targets[index])
        elif action == "Add":
            value = int(command[2])
            if 0 <= index and index < len(targets):
                targets.insert(index, value)
            else:
                print("Invalid placement!")
        elif action == "Strike":
            radius = int(command[2])
            range = radius + index
            if 0 > index or index > len(targets):
                print("Strike missed!")
                continue                                      # 5, 2 ->
            elif range > len(targets) or index - radius < 0:  # 2 + 2; 2 -4
                print("Strike missed!")
                continue
            else:
                removed_sub_list = targets[index-radius:index+radius+1]
            #    targets = [x for x in targets if not x in removed_sub_list]
                if removed_sub_list[0] in targets and removed_sub_list[-1] in targets:
                    start_index = targets.index(removed_sub_list[0])
                    end_index = targets.index(removed_sub_list[-1]) + 1
                    targets = targets[:start_index] + targets[end_index:]