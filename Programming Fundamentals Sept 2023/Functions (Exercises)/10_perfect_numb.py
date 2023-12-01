user_input = input()
number = int(user_input)

def is_perfect_number(number):
    if number <= 1:
        return False  # Perfect numbers are positive integers

    divisors = [1]  # 1 is always a divisor
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors.extend([i, number // i])

    return sum(divisors) == number

is_perfect_number(number)

if is_perfect_number(number):
    print("We have a perfect number!")
else:
    print(f"It's not so perfect.")