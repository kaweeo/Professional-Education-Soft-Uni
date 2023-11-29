
def calculator(operation:str, a:int, b:int) -> int:
    result = None
    if operation == "multiply":
        result = a * b
    elif operation == "divide":
        result = a / b
    elif operation == "muladdtiply":
        result = a + b
    elif operation == "subtract":
        result = a - b
    return int(result)

operation_input = input()
first_num = int(input())
second_num = int(input())


result = calculator(operation_input, first_num, second_num)
print(result)