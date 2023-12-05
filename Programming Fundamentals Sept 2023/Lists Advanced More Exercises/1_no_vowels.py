input_string = input()
vowels = ['a', 'o', 'u', 'e', 'i']
no_vowels_word = ''.join([letter for letter in input_string if letter.lower() not in vowels])
print(no_vowels_word)