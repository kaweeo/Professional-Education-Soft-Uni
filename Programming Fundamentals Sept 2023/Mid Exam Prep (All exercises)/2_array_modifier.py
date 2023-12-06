
seq_of_ints = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        seq_of_str_for_print = list(map(str, seq_of_ints))
        print(", ".join(seq_of_str_for_print))
        break
    else:
        command = command.split()
        action = command[0]
        if action == "swap":
            index1 = int(command[1])
            index2 = int(command[2])
            seq_of_ints[index1], seq_of_ints[index2] = seq_of_ints[index2], seq_of_ints[index1]
        elif action == "multiply":
            index1 = int(command[1])
            index2 = int(command[2])
            product = seq_of_ints[index1] * seq_of_ints[index2]
            seq_of_ints[index1] = product
        elif action == "decrease":
            seq_of_ints = [n - 1 for n in seq_of_ints]
