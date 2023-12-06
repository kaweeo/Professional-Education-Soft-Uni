
targets_list = input().split(" ")
targets_list = [int(target) for target in targets_list]

shot_targets_counter = 0

while True:
    command = input()
    if command == "End":
        state_of_targets = " ".join(map(str, targets_list))
        print(f"Shot targets: {shot_targets_counter} -> {state_of_targets}")
        break
    else:
        shot = int(command)
        if shot < 0 or shot >= len(targets_list):
            continue
        else:
            shot_taget_value = targets_list[shot]
            if shot_taget_value != -1:
                for index, target in enumerate(targets_list):
                    if target > shot_taget_value and target != -1:
                        targets_list[index] -= shot_taget_value
                    elif target <= shot_taget_value and target != -1:
                        targets_list[index] += shot_taget_value
                targets_list[shot] = -1
                shot_targets_counter += 1
            else:
                continue
