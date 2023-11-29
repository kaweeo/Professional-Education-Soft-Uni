
# def string_repeater(str_to_repeat: str, n: int) -> str:
#     return str_to_repeat * n

string = input()
n = int(input())

repet_string = lambda a, b: a * b
result = repet_string(string, n)
print(result)