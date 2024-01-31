def age_assignment(*args, **kwargs):
    result_dict = {}
    copy_kwargs = kwargs.copy()

    for arg in args:
        for letter in kwargs.keys():
            if arg[0] == letter:
                result_dict[arg] = copy_kwargs.pop(letter)

    sorted_result_dict = dict(sorted(result_dict.items(), key=lambda x: x[0]))
    result_dict = '\n'.join([f"{k} is {v} years old." for k, v in sorted_result_dict.items()])
    return result_dict

print(age_assignment("Peter", "George", G=26, P=19))

# def age_assignment(*names, **age_data):
#     result = []
#
#     for letter, age in age_data.items():
#         for name in names:
#             if name.startswith(letter):
#                 result.append(f"{name} is {age} years old.")
#                 break
#
#     return "\n".join(sorted(result))
#
#
# print(age_assignment("Peter", "George", G=26, P=19))