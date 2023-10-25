import math

word = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
ascii_code_sum = 0
current_value = 0

while word != "End of words":
    ascii_code_sum = 0
    for letter in word:
        ascii_code_sum += ord(letter)
    if word[0] in vowels:
        ascii_code_sum = ascii_code_sum * len(word)
    else:
        ascii_code_sum = ascii_code_sum / len(word)
        ascii_code_sum = math.floor(ascii_code_sum)
    if ascii_code_sum > current_value:
        current_value = ascii_code_sum
        current_word = word
    word = input()
    if word == "End of words":
        break
print(f"The most powerful word is {current_word} - {current_value}")

