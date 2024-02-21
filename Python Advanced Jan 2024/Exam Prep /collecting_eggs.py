from collections import deque

BOX_SIZE = 50

sizes_of_eggs_deque = deque(int(x) for x in input().split(", "))
sizes_of_papers_deque = deque(int(x) for x in input().split(", "))

boxed_eggs = 0

while sizes_of_papers_deque and sizes_of_eggs_deque:
    first_egg = sizes_of_eggs_deque.popleft()
    last_paper = sizes_of_papers_deque.pop()
    sum_egg_paper = first_egg + last_paper

    if first_egg <= 0:
        sizes_of_papers_deque.append(last_paper)
        continue
    if first_egg == 13:
        first_to_swap = sizes_of_papers_deque.popleft()
        sizes_of_papers_deque.appendleft(last_paper)
        sizes_of_papers_deque.append(first_to_swap)

    elif sum_egg_paper <= BOX_SIZE:
        boxed_eggs += 1

if boxed_eggs:
    print(f"Great! You filled {boxed_eggs} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if sizes_of_eggs_deque:
    print(f"Eggs left: {', '.join(str(x) for x in sizes_of_eggs_deque)}")

if sizes_of_papers_deque:
    print(f"Pieces of paper left: {', '.join(str(x) for x in sizes_of_papers_deque)}")
