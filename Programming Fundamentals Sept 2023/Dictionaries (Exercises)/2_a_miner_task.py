counter = 2
resources = {}
while True:
    input_line = input()
    if input_line == "stop":
        break
    counter += 1
    if counter % 2 != 0:
        resource = input_line
        if not resource in resources.keys():
            resources[resource] = None
    elif counter % 2 == 0:
        quantity = int(input_line)
        if resources[resource] == None:
            resources[resource] = quantity
        else:
            resources[resource] += quantity

for k, v in resources.items():
    print(f"{k} -> {v}")
