def abs_converter(sequence_numbers: list) -> list:
    return [abs(float(number)) for number in sequence_numbers]

seq_numbers_input = input().split(" ")
result = abs_converter(seq_numbers_input)
print(result)