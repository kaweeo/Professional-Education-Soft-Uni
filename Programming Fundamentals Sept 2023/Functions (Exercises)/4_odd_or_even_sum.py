def odd_or_eve_sum():
    user_input = input()
    list_of_digits = []
    even_sum = 0
    odd_sum = 0

    for digit in user_input:
        list_of_digits.append(int(digit))

    for value in list(list_of_digits):
        if value % 2 == 0:
            even_sum += value
        else:
            odd_sum += value

    return print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

odd_or_eve_sum()