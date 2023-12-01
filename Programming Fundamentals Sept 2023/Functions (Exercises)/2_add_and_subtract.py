
def add_and_subtract(num1, num2, num3):
    def sum_numbers():
        sum = num1 + num2
        return sum
    def subtract(sum):
        sub = sum - num3
        return print(sub)
    subtract(sum_numbers())
    
num1 = int(input())
num2 = int(input())
num3 = int(input())

add_and_subtract(num1, num2, num3)