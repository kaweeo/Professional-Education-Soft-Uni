
won_battles_counter = 0

initial_energy = int(input())

while True:
    command = input()
    if command == "End of battle":
        print(f"Won battles: {won_battles_counter}. Energy left: {initial_energy}" )
        break
    else:
        distance_to_reach = int(command)
        initial_energy -= distance_to_reach
        if initial_energy < 0:
            initial_energy += distance_to_reach
            print(f"Not enough energy! Game ends with {won_battles_counter} won battles and {initial_energy} energy")
            break
        won_battles_counter += 1
        if won_battles_counter % 3 == 0:
            initial_energy += won_battles_counter