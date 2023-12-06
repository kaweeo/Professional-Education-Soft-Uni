initial_loot_list = input().split("|")

while True:
    command = input().split(" ")

    if command[0] == "Yohoho!":
        break

    if command[0] == "Loot":
        for item in command[1:]:
            if item not in initial_loot_list:
                initial_loot_list.insert(0, item)
    elif command[0] == "Drop":
        index = int(command[1])
        if 0 <= index < len(initial_loot_list):
            popped = initial_loot_list.pop(index)
            initial_loot_list.append(popped)
    elif command[0] == "Steal":
        count = int(command[1])
        if len(initial_loot_list) < count:
            stolen_items = initial_loot_list
            initial_loot_list = []
        else:
            stolen_items = initial_loot_list[-count:]
            initial_loot_list = initial_loot_list[:-count]
        print(", ".join(stolen_items))

if len(initial_loot_list) == 0:
    print("Failed treasure hunt.")
else:
    sum_items_length = sum(len(item) for item in initial_loot_list)
    avg_treasure_gain = sum_items_length / len(initial_loot_list)
    print(f"Average treasure gain: {avg_treasure_gain:.2f} pirate credits.")
