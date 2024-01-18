# from math import floor
# from collections import deque
# from functools import reduce
#
# possible_operators = ["*", "+", "-", "/"]
#
# functions = {
#     "*": lambda data: reduce(lambda x, y: x * y, data), # result1 = reduce((lambda x, y: x * y), list1)
#     "+": lambda data: reduce(lambda x, y: x + y, data),
#     "-": lambda data: reduce(lambda x, y: x - y, data),
#     "/": lambda data: reduce(lambda x, y: floor(x / y), data),
# }
#
# expression = deque(input().split())
# sub_expression = []
#
# while len(expression) > 0:
#
#     current_symbol = expression.popleft()
#
#     if current_symbol not in possible_operators:
#         sub_expression.append(int(current_symbol))
#     else:
#         expression.appendleft(functions[current_symbol](sub_expression))
#         if len(expression) == 1:
#             break
#         sub_expression = []
#
# print(*expression)



from collections import deque
from math import floor

expression = deque(input().split())
idx = 0

while idx < len(expression):
    element = expression[idx]

    if element in "/*+-":
        for _ in range(idx - 1):
            expression.appendleft(eval(f"{expression.popleft()} {element} {expression.popleft()}"))

        del expression[1]
        idx = 1

    idx += 1

print(floor(int(expression[0])))