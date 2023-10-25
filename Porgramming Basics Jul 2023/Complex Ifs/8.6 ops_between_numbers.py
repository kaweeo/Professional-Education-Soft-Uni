N1 = int(input())
N2 = int(input())
op = input()

if op == "+":
    result = N1 + N2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{N1} {op} {N2} = {result} - {even_or_odd}")
elif op == "-":
    result = N1 - N2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{N1} {op} {N2} = {result} - {even_or_odd}")
elif op == "*":
    result = N1 * N2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{N1} {op} {N2} = {result} - {even_or_odd}")
elif op == "/":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 / N2
        print(f"{N1} / {N2} = {result:.2f}")
elif op == "%":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        leftover = N1 % N2
        print(f"{N1} % {N2} = {leftover}")