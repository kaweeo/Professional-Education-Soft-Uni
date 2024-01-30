def even_odd_filter(**kwargs):
    result = {}

    for k, v in kwargs.items():
        result[k] = []
        if k == "odd":
            result[k] = [num for num in v if num % 2 != 0]
        elif k == "even":
            result[k] = [num for num in v if num % 2 == 0]

    return dict(sorted(result.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))