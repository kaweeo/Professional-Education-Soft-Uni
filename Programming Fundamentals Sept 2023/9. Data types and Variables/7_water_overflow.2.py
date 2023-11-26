
capacy = 255
n = int(input())
filled = 0

for _ in range(n):
    sip = int(input())
    filled += sip
    if filled > capacy:
        print("Insufficient capacity!")
        filled -= sip
print(filled)
