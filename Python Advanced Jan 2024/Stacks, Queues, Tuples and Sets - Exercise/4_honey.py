from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

tot_honey_made = 0

while working_bees and nectar:
    first_bee = working_bees.popleft()
    last_nectar = nectar.pop()

    if last_nectar >= first_bee:
        collected_nectar = last_nectar
        first_symbol = symbols.popleft()
        if first_symbol == "/" and collected_nectar == 0:
            continue
        else:
            made_honey = eval(f"{first_bee} {first_symbol} {collected_nectar}")
            tot_honey_made += abs(made_honey)
    else:
        working_bees.appendleft(first_bee)

print(f"Total honey made: {tot_honey_made}")

if working_bees:
    print(f"Bees left: {', '.join(map(str, working_bees))}")
if nectar:
    print(f"Bees left: {', '.join(map(str, nectar))}")



# from collections import deque
#
# bees = deque(int(x) for x in input().split())
# nectar = [int(x) for x in input().split()]
# symbols = deque(input().split())
#
# total_honey = 0
#
# functions = {
#     "*": lambda a, b: a * b,
#     "/": lambda a, b: a / b if b != 0 else 0,
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a - b,
# }
#
# while bees and nectar:
#     curr_bee = bees.popleft()
#     curr_nectar = nectar.pop()
#
#     if curr_nectar < curr_bee:
#         bees.appendleft(curr_bee)
#     else:
#         total_honey += abs(functions[symbols.popleft()](curr_bee, curr_nectar))
#
# print(f"Total honey made: {total_honey}")
#
# if bees:
#     print(f"Bees left: {', '.join(str(x) for x in bees)}")
#
# if nectar:
#     print(f"Nectar left: {', '.join(str(x) for x in nectar)}")