text = input().split()
chars = {}

for word in text:
    for char in word:
        if char in chars.keys():
            chars[char] += 1
        else:
            chars[char] = 1

for k, v in chars.items():
    print(f"{k} -> {v}")
