def even_odd(*args):
    result = []
    command = args[-1]
    if command == "even":
        result = [num for num in args[:-1] if num % 2 == 0]
    elif command == "odd":
        result = [num for num in args[:-1] if num % 2 != 0]
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
