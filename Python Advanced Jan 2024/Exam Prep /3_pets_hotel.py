
def accommodate_new_pets(capacity, maximum_weight_limit, *pets):
    available_capacity = capacity
    pets_dict = {}
    no_room = False

    for pet in pets:
        pet_type = pet[0]
        pet_weight = float(pet[1])
        if available_capacity <= 0:
            no_room = True
            break
        if pet_weight > maximum_weight_limit:
            continue
        available_capacity -= 1
        if not pet_type in pets_dict.keys():
            pets_dict[pet_type] = 0
        pets_dict[pet_type] += 1

    if not no_room:
        result = f"All pets are accommodated! Available capacity: {available_capacity}."
    else:
        result = f"You did not manage to accommodate all pets!"


    result += f"\nAccommodated pets:"

    sorted_pets_dict = dict(sorted(pets_dict.items(), key=lambda x: x[0]))
    for pet_type, count_pets in sorted_pets_dict.items():
        result += f"\n{pet_type}: {count_pets}"

    return result



print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

# SOLUTION 2
# def accommodate_new_pets(capacity, max_weight, *pets_data):
#     accommodated_pets = {}
#     result = []
#
#     for pet_type, pet_weight in pets_data:
#         if capacity <= 0:
#             result.append('You did not manage to accommodate all pets!')
#             break
#         if pet_weight > max_weight:
#             continue
#         if pet_type not in accommodated_pets:
#             accommodated_pets[pet_type] = 0
#         accommodated_pets[pet_type] += 1
#         capacity -= 1
#     else:
#         result.append(f'All pets are accommodated! Available capacity: {capacity}.')
#
#     result.append('Accommodated pets:')
#     [result.append(f'{pet_type}: {pet_number}') for pet_type, pet_number in sorted(accommodated_pets.items())]
#     return '\n'.join(result)
#
