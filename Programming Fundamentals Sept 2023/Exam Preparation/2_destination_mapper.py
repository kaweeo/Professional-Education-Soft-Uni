import re

text = input()

pattern = r'([=\/])([A-Z][a-zA-Z]{2,})(\1)'

destinations = []
matches = re.findall(pattern, text)
for match in matches:
    destination = match[1]
    destinations.append(destination)

total_points = 0
dest_for_print = ", ".join(destinations)
print(f"Destinations: {dest_for_print}")
for destination in destinations:
    total_points += len(destination)
print(f"Travel Points: {total_points}")