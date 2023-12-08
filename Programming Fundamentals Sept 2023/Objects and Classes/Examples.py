# 1

class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


# 2

class Party:
    def __init__(self):
        self.people = []


party = Party()
name = input()
while name != "End":
    party.people.append(name)
    name = input()
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")


# 3

class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails_objects = []
info = input()
while info != "Stop":
    sender, receiver, content = info.split()
    email_info = Email(sender, receiver, content)
    emails_objects.append(email_info)
    info = input()
indexes = [int(index) for index in input().split(", ")]
for index in indexes:
    emails_objects[index].send()
for current_email in emails_objects:
    print(current_email.get_info())


# 4

class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        string_for_print = ""
        if species == "mammal":
            string_for_print += f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            string_for_print += f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == "bird":
            string_for_print += f"Birds in {self.name}: {', '.join(self.birds)}"
        string_for_print += f"\nTotal animals: {Zoo.__animals}"
        return string_for_print


zoo_name = input()
zoo_object = Zoo(zoo_name)
count_of_animals = int(input())
for animals in range(count_of_animals):
    species, name = input().split()
    zoo_object.add_animal(species, name)
searched_species = input()
print(zoo_object.get_info(searched_species))


