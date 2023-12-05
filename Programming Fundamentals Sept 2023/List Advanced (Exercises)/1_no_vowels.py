vowels = "a, o, u, e, i"
vowels_list = vowels.split(", ")
#print(vowels_list)

string = input()

output = "".join(char for char in string if char.lower() not in vowels_list)
print(output)