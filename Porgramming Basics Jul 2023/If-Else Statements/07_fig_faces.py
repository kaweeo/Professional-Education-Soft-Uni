import math
type = input()

if type == "square":
    weight = float(input())
    s = weight * weight
    print(round(s, 3))
elif type == "rectangle":
    weight = float(input())
    height = float(input())
    s = weight * height
    print(round(s, 3))
elif type == "circle":
    r = float(input())
    s = math.pi * r ** 2
    print(round(s, 3))
elif type == "triangle":
    side = float(input())
    m = float(input())
    s = side * m / 2
    print(round(s, 3))