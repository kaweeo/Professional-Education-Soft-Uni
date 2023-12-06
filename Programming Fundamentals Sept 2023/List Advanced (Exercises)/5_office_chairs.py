
number_rooms = int(input())
free_chairs = 0
flag = False

for room in range(1, number_rooms + 1):
    data = input().split(" ")
    free_chairs += len(data[0]) - int(data[1])
    if int(data[1]) > len(data[0]):
        diff = int(data[1]) - len(data[0])
        print(f"{diff} more chairs needed in room {room}")
        flag = True
if flag == False:
    print(f"Game On, {free_chairs} free chairs left")

