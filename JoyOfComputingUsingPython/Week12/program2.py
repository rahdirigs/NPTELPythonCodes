str = input()

up, low = 0, 0

for i in str:
    if (i.isupper()):
        up += 1
    elif (i.islower()):
        low += 1

print(up, low)
