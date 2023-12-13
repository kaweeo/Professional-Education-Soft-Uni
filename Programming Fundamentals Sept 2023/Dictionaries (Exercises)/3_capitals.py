# Using a dictionary comprehension

countries = input().split(", ")
capitals = input().split(", ")

dictionary = dict(zip(countries, capitals))

for k, v in dictionary.items():
    print(f"{k} -> {v}")
