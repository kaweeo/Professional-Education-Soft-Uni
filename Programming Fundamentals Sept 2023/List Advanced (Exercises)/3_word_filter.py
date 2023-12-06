
text_list = input().split(" ")

valids = [word for word in text_list if not len(word) % 2]
for valid in valids:
    print(valid)