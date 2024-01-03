
initial_stops = input()

while True:
    command = input()
    if command == "Travel":
        print(f"Ready for world tour! Planned stops: {initial_stops}")
        break
    else:
        action_command = command.split(":")
        action = action_command[0]
        if action == "Add Stop":
            index = int(action_command[1])
            string = action_command[2]
            if index <= len(initial_stops):     # migh be outside care
                 initial_stops = initial_stops[:index] + string + initial_stops[index:]
            print(f"{initial_stops}")
        elif action == "Remove Stop":
            start_index = int(action_command[1])
            end_index = int(action_command[2])
            # care this check
            if (start_index >= 0 and start_index < len(initial_stops)) and (end_index >= 0 and end_index < len(initial_stops)):
                initial_stops = initial_stops[:start_index] + initial_stops[end_index + 1:]
            print(f"{initial_stops}")
        elif action == "Switch":
            old_string = action_command[1]
            new_string = action_command[2]
            if old_string in initial_stops:
                initial_stops = initial_stops.replace(old_string, new_string)  # care must change old occurrences
            print(f"{initial_stops}")
