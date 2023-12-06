pirate_ship = input().split(">")
pirate_ship = [int(section) for section in pirate_ship]
warship = input().split(">")
warship = [int(section) for section in warship]
max_health_cap = int(input())
flag = False

while True:
    command = input()
    action = command.split()
    if command == "Retire":
        break

    if action[0] == "Fire":
        index = int(action[1])
        if 0 <= index < len(warship):
            warship[int(action[1])] -= int(action[2])
            if warship[int(action[1])] <= 0:
                print("You won! The enemy ship has sunken.")
                flag = True
                break
    elif action[0] == "Defend":
        damage = int(action[3])
        start_index = int(action[1])
        end_index = int(action[2])
        if 0 <= start_index < len(pirate_ship) and start_index <= end_index < len(pirate_ship):
            taking_damage_elements = pirate_ship[start_index:end_index + 1]
            damaged_elements = [element - damage for element in taking_damage_elements]
            pirate_ship = pirate_ship[:start_index] + damaged_elements + pirate_ship[end_index + 1:]
            for section in pirate_ship:
                if section < 0:
                    print("You lost! The pirate ship has sunken.")
                    flag = True
                    break
        if flag:
            break

    elif action[0] == "Repair":
        health = int(action[2])
        if 0 <= int(action[1]) < len(pirate_ship):
            pirate_ship[int(action[1])] += health
            if pirate_ship[int(action[1])] > max_health_cap:
                pirate_ship[int(action[1])] = max_health_cap

    elif action[0] == "Status":
        section_counter = 0
        for section in pirate_ship:
            if section < 0.2 * max_health_cap:
                section_counter += 1
        print(f"{section_counter} sections need repair.")

if flag == False:
    pirateShipSum = sum(pirate_ship)
    warshipSum = sum(warship)

    print(f"Pirate ship status: {pirateShipSum}")
    print(f"Warship status: {warshipSum}")

