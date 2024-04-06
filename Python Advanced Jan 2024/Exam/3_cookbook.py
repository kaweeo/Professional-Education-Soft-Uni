def cookbook(*cook_data):
    result = ""
    cookbook_dict = {}

    for data in cook_data:
        recipe = data[0]
        cuisine = data[1]
        ingridients_list = data[2]

        if cuisine not in cookbook_dict.keys():
            cookbook_dict[cuisine] = {}
        cookbook_dict[cuisine][recipe] = ingridients_list

    for cuisine in cookbook_dict.keys():
        cookbook_dict[cuisine] = dict(sorted(cookbook_dict[cuisine].items()))

    sorted_coobook_dict = dict(sorted(cookbook_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    for cuisine, recepe_ingridients in sorted_coobook_dict.items():
        result += f"\n{cuisine} cuisine contains {len(recepe_ingridients)} recipes:"
        for recepe, ingridienets in sorted_coobook_dict[cuisine].items():
            result += f"\n  * {recepe} -> Ingredients: {', '.join(ingridienets)}"

    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))