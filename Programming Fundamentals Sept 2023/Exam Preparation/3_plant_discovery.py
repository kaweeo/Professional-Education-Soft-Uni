

plants = {}
count_input_lines = int(input())
for plant_rarity in range(count_input_lines):
    plant_rarity = input()
    plant, rarity = plant_rarity.split("<->")
    if not plant in plants.keys():
        plants[plant] = {"rarity": rarity}
        plants[plant]["ratings"] = []
    else:
        plants[plant]["rarity"] = rarity

command_input = input()
while command_input != "Exhibition":
    command_input = command_input.split(": ")
    command_input[1] = command_input[1]
    command = command_input[0]
    if command == "Rate":
        plant, rating = command_input[1].split(" - ")
        if plant in plants.keys():
            plants[plant]["ratings"].append(int(rating))
        else:
            print("error")
    elif command == "Update":
        plant, new_rarity = command_input[1].split(" - ")
        if plant in plants.keys():
            plants[plant]["rarity"] = new_rarity
        else:
            print("error")
    elif command == "Reset":
        plant = command_input[1]
        if plant in plants.keys():
            plants[plant]["ratings"] = []
        else:
            print("error")
    command_input = input()
#print(plants)

print("Plants for the exhibition:")
for plant, items in plants.items():
    if len(plants[plant]["ratings"]) == 0:
        avg_rating = 0
    else:
        avg_rating = sum(plants[plant]["ratings"]) / len(plants[plant]["ratings"])
    print(f"- {plant}; Rarity: {plants[plant]['rarity']}; Rating: {avg_rating:.2f}")