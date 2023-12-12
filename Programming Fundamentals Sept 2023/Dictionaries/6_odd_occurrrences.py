
elements_list = input().split(" ")

dict = {}

for word in elements_list:
    word_lower = word.lower()
    if word_lower not in dict:
        dict[word_lower] = 0
    dict[word_lower] += 1

for (k, v) in dict.items():
    if v % 2 != 0:
        print(k, end=" ")