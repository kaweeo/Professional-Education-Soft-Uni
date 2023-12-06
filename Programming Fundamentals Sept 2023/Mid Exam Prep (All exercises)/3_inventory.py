
inventory = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break
    else:
        command = command.split(" - ")
        action = command[0]
        item = command[1]
        if action == "Collect":
            if item not in inventory:
                inventory.append(item)
            else:
                continue
        elif action == "Drop":
            if item in inventory:
                inventory.remove(item)
        elif action == "Combine Items":
            item = item.split(":")
            old_item = item[0]
            new_item = item[1]
            if old_item in inventory:
                index_of_old_item = inventory.index(old_item)
                inventory.insert(index_of_old_item + 1, new_item)
            else:
                continue
        elif action == "Renew":
            if item in inventory:
                index_of_item = inventory.index(item)
                popped = inventory.pop(index_of_item)
                inventory.append(popped)

items_for_print = ", ".join(inventory)
print(items_for_print)
