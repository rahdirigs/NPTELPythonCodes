inp = input()
one, zero = 0, 0

for i in range(len(inp)):
    if inp[i] == '0':
        zero += 1
    else:
        one += 1

if zero == 1 or one == 1:
    print("YES", end="")
else:
    print("NO", end="")
