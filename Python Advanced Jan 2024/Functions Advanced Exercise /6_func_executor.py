
def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    results = []
    for func, inner_args in args:
        results.append(f"{func.__name__} - {func(*inner_args)}")

    return "\n".join(results)

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))


#
# def func_executor(*funcs_data):
#     return "\n".join(f"{func.__name__} - {func(*args)}" for func, args in funcs_data)