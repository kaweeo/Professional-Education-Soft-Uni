from collections import deque
water_queue = deque()
water_quantity = int(input())

command = input()
while command != "Start":
    name = command
    water_queue.append(name)
    command = input()
    if command == "Start":
        break

command = input()
while command != "End":
    if command == "End":
        break
    if "refill" in command:
        command_list = command.split(" ")
        refilled_liters = int(command_list[1])
        water_quantity += refilled_liters
    else:
        liters_to_deduct = int(command)
        if water_quantity >= liters_to_deduct:
            water_quantity -= liters_to_deduct
            print(f"{water_queue.popleft()} got water")
        else:
            print(f"{water_queue.popleft()} must wait")
    command = input()
print(f"{water_quantity} liters left")