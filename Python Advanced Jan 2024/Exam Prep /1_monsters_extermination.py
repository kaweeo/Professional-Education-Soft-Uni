from collections import deque

monsters = deque([int(x) for x in input().split(",")])
attack_damage = [int(x) for x in input().split(",")]

killed_monsters = 0

while monsters and attack_damage:

    current_monster = monsters.popleft()
    current_atack = attack_damage.pop()

    if current_atack > current_monster:
        killed_monsters += 1
        attack_damage_left = current_atack - current_monster
        if attack_damage:
            attack_damage[-1] += attack_damage_left
        else:
            attack_damage.append(attack_damage_left)
    elif current_atack == current_monster:
        killed_monsters += 1
    else:
        monsters.append(current_monster - current_atack)

if not monsters:
    print("All monsters have been killed!")
if not attack_damage:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")