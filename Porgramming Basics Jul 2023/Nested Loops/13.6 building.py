floors = int(input())
rooms = int(input())

for i in range(floors, 0, -1):
    for j in range(0, rooms):
        if i == floors:
            print("L{0}{1} ".format(i,j), end = "")
        elif i % 2 == 0:
            print(f"O{i}{j} ".format(i, j), end= "")
        else:
            print(f"A{i}{j} ".format(i, j), end= "")
    print()