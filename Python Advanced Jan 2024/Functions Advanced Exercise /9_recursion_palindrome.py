def palindrome(word, idx):
    if idx == len(word) // 2:
        return f"{word} is a palindrome"

    if word[idx] != word[-idx-1]:
        return f"{word} is not a palindrome"

    result = palindrome(word, idx+1)

    return result


print(palindrome("abcba", 0))


# def palindrome(word, index):
#     original_word = word[:]
#     if len(word) <= 1:
#         return f"{original_word} is a palindrome"
#     if word[0] != word[-1]:
#         return f"{original_word} is not a palindrome"
#
#     return palindrome(word, index+1)
#
#
# print(palindrome("abcba", 0))