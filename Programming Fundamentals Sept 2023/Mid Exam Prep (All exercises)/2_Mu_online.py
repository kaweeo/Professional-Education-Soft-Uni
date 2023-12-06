
dungeon_input_list = input().split("|")
health = 100
bitcoins = 0
flag = False

for room in dungeon_input_list:
    room = room.split(" ")
    command = room[0]
    number = int(room[1])

    if command == "potion":
        current_health = health
        health += number
        if health > 100:    # 90 + 30 = 120
            print(f"You healed for {100 - current_health} hp.")
            health = 100
        else:
            print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        monster = command
        attack = number
        health -= attack
        if health <= 0:
            room_merged = monster + " " + str(attack)
            room_number = dungeon_input_list.index(room_merged) + 1
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {room_number}")
            flag = True
            break
        else:
            print(f"You slayed {monster}.")

if flag == False:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")