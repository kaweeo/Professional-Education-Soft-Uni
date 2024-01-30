def sorting_cheeses(**kwargs):

    result = ""
    result_sorted = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for cheese, pieces in result_sorted:
        result += f"{cheese}\n"
        result += "\n".join(map(str, sorted(pieces, reverse=True)))
        result += "\n"

    return result

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)