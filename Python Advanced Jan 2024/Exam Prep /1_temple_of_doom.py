from collections import deque

tools_deque = deque([int(x) for x in (input().split())])
substances_stack = [int(x) for x in (input().split())]
temple_challenges = [int(x) for x in (input().split())]

while True:
    if not temple_challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break
    elif not tools_deque or not substances_stack:
        print("Harry is lost in the temple. Oblivion awaits him.")
        break
    first_tool = tools_deque.popleft()
    last_substance = substances_stack.pop()

    power = first_tool * last_substance

    if power in temple_challenges:
        temple_challenges.remove(power)
    else:
        first_tool += 1
        tools_deque.append(first_tool)
        last_substance -= 1
        if not last_substance == 0:
            substances_stack.append(last_substance)

if tools_deque:
    print(f"Tools: " + ', '.join(str(x) for x in tools_deque))
if substances_stack:
    print(f"Substances: " + ', '.join(str(x) for x in substances_stack))
if temple_challenges:
    print("Challenges: " + ', '.join(str(x) for x in temple_challenges))
