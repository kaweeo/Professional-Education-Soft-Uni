import re

text = input()
pattern = r'\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b'
fount_emails = re.findall(pattern, text)
for mail in fount_emails:
    print(mail[0])