n = int(input())

for r in range(1, n + 1):
    for c in range(1, r + 1):
        atr = " "
        if c == r:
            atr = ""
        print(c, end=atr)
    if r < n:
        print()
