
class Email():
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
line = input()
while line != "Stop":
    sender, receiver, content = line.split()
    email = Email(sender, receiver, content)
    emails_objects.append(email)
    line = input()

indexes = [int(index) for index in input(" ").split(", ")]
for email in emails_objects:
    for index in indexes:
        emails_objects[index].is_sent = True
    print(email.get_info())

