
user_input = input()
palindrome = input()

my_list = user_input.split(" ")
palinrdomes = []

for word in my_list:
    if word == "".join(reversed(word)):
        palinrdomes.append(word)

print(palinrdomes)
print(f"Found palinrdome {palinrdomes.count(palindrome)} times")