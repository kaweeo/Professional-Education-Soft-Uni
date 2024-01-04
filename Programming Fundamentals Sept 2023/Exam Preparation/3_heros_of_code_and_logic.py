
number_of_heros = int(input())

heroes = {}

for hero in range(number_of_heros):
    input_line = input().split(" ")
    hero = input_line[0]
    hp = int(input_line[1])
    mp = int(input_line[2])
    heroes[hero] = {}
    heroes[hero]["health"] = hp
    heroes[hero]["mana"] = mp

command_input = input()
while command_input != "End":
    command_input_list = command_input.split(" - ")
    command = command_input_list[0]
    hero = command_input_list[1]
    if command == "CastSpell":
        mp_needed = int(command_input_list[2])
        spell_name = command_input_list[3]
        if heroes[hero]["mana"] >= mp_needed:
            mana_left = heroes[hero]["mana"] - mp_needed
            heroes[hero]["mana"] = mana_left
            print(f"{hero} has successfully cast {spell_name} and now has {mana_left} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")
    elif command == "TakeDamage":
        damage_taken = int(command_input_list[2])
        attacker = command_input_list[3]
        if damage_taken >= heroes[hero]["health"]:
            heroes.pop(hero)
            print(f"{hero} has been killed by {attacker}!")
        else:
            left_hp = heroes[hero]["health"] - damage_taken
            heroes[hero]["health"] -= damage_taken
            print(f"{hero} was hit for {damage_taken} HP by {attacker} and now has {left_hp} HP left!")
    elif command == "Recharge":
        amount = int(command_input_list[2])

        if heroes[hero]["mana"] + amount > 200:
            amount_recovered = 200 - heroes[hero]["mana"]
            heroes[hero]["mana"] = 200
            print(f"{hero} recharged for {amount_recovered} MP!")
        else:
            heroes[hero]["mana"] += amount
            amount_recovered = amount
            print(f"{hero} recharged for {amount_recovered} MP!")
    elif command == "Heal":
        amount = int(command_input_list[2])
        if heroes[hero]["health"] + amount > 100:
            healed_amount = 100 - heroes[hero]["health"]
            print(f"{hero} healed for {healed_amount} HP!")
            heroes[hero]["health"] = 100
        else:
            heroes[hero]["health"] += amount
            print(f"{hero} healed for {amount} HP!")
    command_input = input()

for hero, stats in heroes.items():
    print(f"{hero}")
    print(f"  HP: {stats['health']}")
    print(f"  MP: {stats['mana']}")
