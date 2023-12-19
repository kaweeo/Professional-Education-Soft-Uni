
n = int(input())
vocal_dict = {}

for _ in range(n):
    word = input()
    synonim = input()
    if word in vocal_dict.keys():
        vocal_dict[word] += f", {synonim}"
    else:
        vocal_dict[word] = synonim

for k, v in vocal_dict.items():
    print(f"{k} – {v}")