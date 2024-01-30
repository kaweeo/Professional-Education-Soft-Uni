def concatenate(*args, **kwargs):
    result = ""

    for arg in args:
        result += arg

    for k, v in kwargs.items():
        if k in result:
            result = result.replace(k, v)

    return result

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
