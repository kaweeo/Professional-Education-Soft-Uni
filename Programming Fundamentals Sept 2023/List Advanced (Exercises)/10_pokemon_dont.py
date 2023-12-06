sequence = (input()).split(" ")

sequence = [int(num) for num in sequence]
sum_popped = 0
adjusted_sequence = sequence

for i in range(1, len(sequence) + 1):
    index = int(input())
    if index >= len(sequence):
        adjusted_sequence = adjusted_sequence[:-1] + [adjusted_sequence[0]]
    popped = adjusted_sequence.pop(index)
    sum_popped += popped
    adjusted_sequence = [num - popped if num > popped else num + popped for num in adjusted_sequence]
    # print(adjusted_sequence)
print(sum_popped)