pack = 1
width = int(input())
length = int(input())
height = int(input())

total_room = width * length * height
total_room_used = 0

done_or_pack = input()

while done_or_pack != "Done":
    done_or_pack = int(done_or_pack)
    total_room_used += done_or_pack

    if total_room_used >= total_room:
        not_enough_room = total_room_used - total_room
        print(f"No more free space! You need {not_enough_room} Cubic meters more.")
        break

    done_or_pack = input()

if done_or_pack == "Done":
    free_room = total_room - total_room_used
    print(f"{free_room} Cubic meters left.")
