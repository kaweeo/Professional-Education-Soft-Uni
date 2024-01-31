from collections import deque

def math_operations(*floats, **floats_to_operate):
    
    deque_of_floats = deque(floats)
    
    while deque_of_floats:
        for key, value in floats_to_operate.items():
            if len(deque_of_floats) == 0:
                break

            current_float = deque_of_floats.popleft()
            if key == "a":
                floats_to_operate[key] += current_float
            elif key == "s":
                floats_to_operate[key] -= current_float
            elif key == "d":
                if current_float != 0:
                    floats_to_operate[key] = floats_to_operate[key] / current_float
            elif key == "m":
                floats_to_operate[key] *= current_float

    sorted_floats_to_operate = dict(sorted(floats_to_operate.items(), key=lambda x: (-x[1], x[0])))

    result = "\n".join([f'{key}: {value:.1f}' for key, value in sorted_floats_to_operate.items()])

    return result

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))



# def math_operations(*numbers, **kwargs):
#     keys = list(kwargs.keys())  # [a, s, d, m]
#
#     for i in range(len(numbers)):
#         key = keys[i % 4]  # 0, 1, 2, 3
#
#         if key == "a":
#             kwargs[key] += numbers[i]
#         elif key == "s":
#             kwargs[key] -= numbers[i]
#         elif key == "d":
#             if numbers[i] != 0:
#                 kwargs[key] /= numbers[i]
#         elif key == "m":
#             kwargs[key] *= numbers[i]
#
#     kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
#
#     return "\n".join(f"{k}: {v:.1f}" for k, v in kwargs)
#
#
# print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))