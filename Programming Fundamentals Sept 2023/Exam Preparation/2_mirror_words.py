import re

text_input = input()

pattern = r'([@#])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})'

matches = re.findall(pattern, text_input)

mirror_tupples = []
for match in matches:
    if match[1] == match[2][::-1]:
        mirror_tupples.append(match)
# print(matches)
# print(mirror_tupples)
valid_pairs_count = len(matches)
mirror_words = len(mirror_tupples)

if valid_pairs_count == 0:
    print("No word pairs found!")
else:
    print(f"{valid_pairs_count} word pairs found!")
if mirror_words == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    for tupple in mirror_tupples:
        word1 = tupple[1]
        word2 = tupple[2]
        if tupple == mirror_tupples[-1]:
            print(word1 + " <=> " + word2, end='')
        else:
            print(word1 + " <=> " + word2, end=', ')
