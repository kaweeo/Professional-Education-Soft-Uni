from functools import reduce


def operate(operator, *args):
    if operator == "+":
        return reduce(lambda x, y: x + y, args)
    elif operator == "-":
        return reduce(lambda x, y: x - y, args)
    elif operator == "*":
        return reduce(lambda x, y: x * y, args)
    elif operator == "/":
        if not 0 in args:
            return reduce(lambda x, y: x / y, args)


print(operate("*", 3, 4))