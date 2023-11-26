n = int(input())

for str in range(n):
    str = input()
    pure_string = True
    if "," in str:
        pure_string = False
    if "." in str:
        pure_string = False
    if "_" in str:
        pure_string = False
    if pure_string == True:
        print(f"{str} is pure.")
    elif pure_string == False:
        print(f"{str} is not pure!")