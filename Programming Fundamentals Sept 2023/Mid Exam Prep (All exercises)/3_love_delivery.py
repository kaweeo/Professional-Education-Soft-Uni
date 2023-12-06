neightborhood = input().split("@")  # needed hearts by house
neightborhood = [int(house) for house in neightborhood]

starting_position_index = 0
mission_successful = False

while True:
    command = input()
    if command == "Love!":
        break
    else:
        command = command.split(" ")
        jump = command[0]
        jump_lenght = int(command[1])
        current_index = starting_position_index + jump_lenght
        if current_index >= len(neightborhood):
            current_index = 0
        starting_position_index = current_index
        house = neightborhood[current_index]

        if house == 0:
            print(f"Place {current_index} already had Valentine's day.")
        else:
            neightborhood[current_index] = house - 2
            if neightborhood[current_index] == 0:
                print(f"Place {current_index} has Valentine's day.")

print(f"Cupid's last position was {current_index}.")

mission_successful = all(item == 0 for item in neightborhood)
if mission_successful:
    print("Mission was successful.")
else:
    count_non_zeros = 0
    for house in neightborhood:
        if house != 0:
            count_non_zeros += 1
    print(f"Cupid has failed {count_non_zeros} places.")
