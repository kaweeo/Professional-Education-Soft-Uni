forces = {}

while True:
    command = input()

    if command == "Lumpawaroo":
        break

    elif "|" in command:
        command = command.split(" | ")
        force_side = command[0]
        force_user = command[1]

        if force_side not in forces:
            forces[force_side] = []

        user_found = False

        for users in forces.values():
            if force_user in users:
                user_found = True
                break

        if not user_found:
            forces[force_side].append(force_user)

    elif "->" in command:
        command = command.split(" -> ")
        force_user = command[0]
        force_side = command[1]

        user_found = False

        for users in forces.values():
            if force_user in users:
                user_found = True
                break

        if user_found:
            for key, value_list in forces.items():
                if force_user in value_list:
                    value_list.remove(force_user)
            if force_side not in forces:
                forces[force_side] = []
            forces[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")

for k, v in forces.items():
    if v:
        print(f"Side: {k}, Members: {len(v)}")
        for user in v:
            print(f"! {user}")
