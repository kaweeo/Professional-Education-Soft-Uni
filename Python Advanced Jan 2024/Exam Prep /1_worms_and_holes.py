from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])

matches = 0
flag = False
while worms and holes:
    first_hole = holes.popleft()
    last_worm = worms.pop()

    if not first_hole == last_worm:
        last_worm -= 3
        if last_worm > 0:
            worms.append(last_worm)
        else:
            flag = True
    else:
        matches += 1

if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms and not flag:
    print("Every worm found a suitable hole!")
elif not worms and flag:
    print("Worms left: none")
else:
    print("Worms left: " + ', '.join(str(x) for x in worms))

if not holes:
    print("Holes left: none")
else:
    print("Holes left: " + ', '.join(str(x) for x in holes))