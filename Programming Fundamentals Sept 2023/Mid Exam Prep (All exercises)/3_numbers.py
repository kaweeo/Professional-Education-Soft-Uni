def average_finder(list: list) -> int:
    return int(sum(list) / len(list))

def above_avg_finder(avg: int, list: list) -> list:
    return [num for num in sequence if num > avarage]

sequence = list(map(int, input().split()))

avarage = average_finder(sequence)
above_avarage = above_avg_finder(avarage, sequence)

if len(above_avarage) == 0:
    print("No")
else:
    above_avarage.sort(reverse=True)
    result_printing = list(map(str, above_avarage[0:5]))
    print(" ".join(result_printing))