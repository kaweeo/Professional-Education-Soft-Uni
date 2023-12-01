def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def divide_and_print_factorials(n1, n2):
    if n2 == 0:
        print("Division by zero is undefined.")
        return
    fact1 = factorial(n1)
    fact2 = factorial(n2)
    result = fact1 / fact2
    print(f"{result:.2f}")

n1 = int(input())
n2 = int(input())

divide_and_print_factorials(n1, n2)