
wagons_count = int(input())
wagons = [0] * wagons_count

while True:
    command = input()
    if command == "End":
        break
    elif command.split(" ")[0] == "add":
        wagons[-1] += int(command.split(" ")[1])
    elif command.split(" ")[0] == "insert":  #you should add the number of people at the given wagon
        wagons[int(command.split(" ")[1])] += int(command.split(" ")[2])
    elif command.split(" ")[0] == "leave":
        wagons[int(command.split(" ")[1])] -= int(command.split(" ")[2])
print(wagons)