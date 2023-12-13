items_dict = {}

is_end = False
while True:
    if is_end:
        break
    items_list = input().split(" ")
    items_list = [item.lower() for item in items_list]

    for i in range(0, len(items_list), 2):
        value = int(items_list[i])
        key = items_list[i + 1]
        if not key in items_dict.keys():
            items_dict[key] = value
        else:
            items_dict[key] += value

        if "shards" in items_dict and items_dict.get("shards") >= 250:
            legendary_item = "Shadowmourne"
            print(f"{legendary_item} obtained!")
            items_dict["shards"] -= 250
            is_end = True
            break
        elif "fragments" in items_dict and items_dict.get("fragments") >= 250:
            legendary_item = "Valanyr"
            print(f"{legendary_item} obtained!")
            items_dict["fragments"] -= 250
            is_end = True
            break
        elif "motes" in items_dict and items_dict.get("motes") >= 250:
            legendary_item = "Dragonwrath"
            print(f"{legendary_item} obtained!")
            items_dict["motes"] -= 250
            is_end = True
            break

if "shards" in items_dict.keys():
    print(f"shards: {items_dict['shards']}")
else:
    print(f"shards: 0")

if "fragments" in items_dict.keys():
    print(f"fragments: {items_dict['fragments']}")
else:
    print(f"fragments: 0")

if "motes" in items_dict.keys():
    print(f"motes: {items_dict['motes']}")
else:
    print(f"motes: 0")

for k, v in items_dict.items():
    if k != "shards" and k != "fragments" and k != "motes":
        print(f"{k}: {items_dict[k]}")
