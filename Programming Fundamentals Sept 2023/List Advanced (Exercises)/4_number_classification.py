
numbers = input().split(", ")
numbers = [int(number) for number in numbers]
positive = [number for number in numbers if number >= 0]
positive = ", ".join(map(str, positive))
negative = [number for number in numbers if number < 0]
negative = ", ".join(map(str, negative))
even = [number for number in numbers if number % 2 == 0]
even = ", ".join(map(str, even))
odd = [number for number in numbers if number % 2 != 0]
odd = ", ".join(map(str, odd))

print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even}")
print(f"Odd: {odd}")