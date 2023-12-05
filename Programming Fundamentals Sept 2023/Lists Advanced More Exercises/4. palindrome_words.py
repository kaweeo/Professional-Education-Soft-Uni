def is_palindrome(some_word: str) -> bool:
    return some_word == some_word[::-1]

some_words = input().split(" ")
specific_palindrome = input()
counter = 0
palindromes = []
for word in some_words:
    if word == specific_palindrome:
        counter += 1
    if is_palindrome(word):
        palindromes.append(word)

print(palindromes)

print(f"Found palindrome {counter} times")

