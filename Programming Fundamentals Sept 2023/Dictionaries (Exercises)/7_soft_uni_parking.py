n = int(input())

su_datebase = {}

for command in range(n):
    command = input().split(" ")
    action = command[0]
    username = command[1]
    if action == "register":
        license_plate_number = command[2]
        if username in su_datebase.keys():
            print(f"ERROR: already registered with plate number {su_datebase[username]}")
        else:
            su_datebase[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    else:
        if username not in su_datebase.keys():
            print(f"ERROR: user {username} not found")
        else:
            del su_datebase[username]
            print(f"{username} unregistered successfully")

for k, v in su_datebase.items():
    print(f"{k} => {v}")
