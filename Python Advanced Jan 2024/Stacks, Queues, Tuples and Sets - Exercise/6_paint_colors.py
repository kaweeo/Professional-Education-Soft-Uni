from collections import deque

words = deque(input().split())

colors = {"red", "yellow", "blue", "purple", "orange", "green"}
req_colors = {
    "orange": {"red", "yellow"},
    "purple": {"blue", "red"},
    "green": {"yellow", "blue"},
}

result = []

while words:
    first_word = words.popleft()
    second_word = words.pop() if words else ''

    for color in (first_word + second_word, second_word + first_word):
        if color in colors:
            result.append(color)
            break
    else:
        for el in (first_word[:-1], second_word[:-1]):  # 'd' 'redd' -> '', 'red'
            if el:
                words.insert(len(words) // 2, el)

for color in set(req_colors.keys()).intersection(result):
    if not req_colors[color].issubset(result):
        result.remove(color)

print(result)


# from collections import deque
#
# string = deque(input().split())
#
# colors_dict = {
#     "Main colors": ["red", "yellow", "blue"],
#     "Secondary colors": ["orange", "purple", "green"],
# }
#
# found_colors = []
# substring_is_last = False
#
# while string:
#     if len(string) == 1:
#         string_to_check_one = string.pop()
#         substring_is_last = True
#     else:
#         first_to_check = string.popleft()
#         last_to_check = string.pop()
#         string_to_check_one = first_to_check + last_to_check
#         string_to_check_two = last_to_check + first_to_check
#
#     if string_to_check_one in colors_dict["Main colors"]:
#         found_colors.append(string_to_check_one)
#     elif string_to_check_two in colors_dict["Main colors"]:
#         found_colors.append(string_to_check_two)
#     elif string_to_check_one in colors_dict["Secondary colors"]:
#         found_colors.append(string_to_check_one)
#     elif string_to_check_two in colors_dict["Secondary colors"]:
#         found_colors.append(string_to_check_two)
#     else:
#         if substring_is_last:
#             break
#         middle_index = len(string) // 2
#         if first_to_check[:-1]:
#             string.insert(middle_index, first_to_check[:-1])
#         if last_to_check[:-1]:
#             string.insert(middle_index, last_to_check[:-1])
#
# if "orange" in found_colors:
#     if not ("red" in found_colors and "yellow" in found_colors):
#         found_colors.remove("orange")
#
# if "purple" in found_colors:
#     if not ("red" in found_colors and "blue" in found_colors):
#         found_colors.remove("purple")
#
# if "green" in found_colors:
#     if not ("blue" in found_colors and "yellow" in found_colors):
#         found_colors.remove("orange")
#
# print(found_colors)
