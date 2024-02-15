from collections import deque

textiles_deque = deque([int(x) for x in input().split()])
medicaments_stack = [int(x) for x in input().split()]

created_items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0
}

healing_items = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100
    }

while textiles_deque and medicaments_stack:
    first_textile = textiles_deque.popleft()
    last_medicament = medicaments_stack.pop()

    sum_of_components = first_textile + last_medicament
    created_item = next((item for item, value in healing_items.items() if sum_of_components == value), None)
    if created_item:
        created_items[created_item] += 1
    elif sum_of_components > healing_items["MedKit"]:
        created_items["MedKit"] += 1
        remaining_resource = sum_of_components - healing_items["MedKit"]
        medicaments_stack[-1] += remaining_resource
    else:
        last_medicament += 10
        medicaments_stack.append(last_medicament)

if not textiles_deque and not medicaments_stack:
    print("Textiles and medicaments are both empty.")
elif not textiles_deque:
    print("Textiles are empty.")
elif not medicaments_stack:
    print("Medicaments are empty.")

sorted_created_items = dict(sorted(created_items.items(), key=lambda kvp: (-kvp[1], kvp[0])))

for k, v in sorted_created_items.items():
    if not v == 0:
        print(f"{k} - {v}")

if medicaments_stack:
    print(f"Medicaments left: {', '.join(str(el) for el in medicaments_stack[::-1])}")
if textiles_deque:
    print(f"Textiles left: {', '.join(str(el) for el in textiles_deque)}")
