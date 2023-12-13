
forces = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    user_found = False
    side_found = False
    if "|" in command:
        force_side, force_user = command.split(" | ")
        for users in forces.values():
            if force_user in users:
                user_found = True
                break

        if force_side in forces.keys():
            side_found = True
        else:
            forces[force_side] = []

        if side_found == False and user_found == False:
            forces[force_side] = [force_user]

        elif side_found == True and user_found == False:
            forces[force_side].append(force_user)

    elif "->" in command:
        force_user, force_side = command.split(" -> ")

        for users in forces.values():
            if force_user in users:
                user_found = True
                break
        if force_side in forces.keys():
            side_found = True
        else:
            forces[force_side] = []

        if user_found:
            for key, value_list in forces.items():
                if force_user in value_list:
                    value_list.remove(force_user)
                    break
            forces[force_side].append(force_user)

        elif side_found == False and user_found == False:
            forces[force_side] = [force_user]

        elif user_found == False:
            forces[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")

for k, v in forces.items():
    if not len(v) == 0:
        print(f"Side: {k}, Members: {len(v)}")
        for user in v:
            print(f"! {user}")

