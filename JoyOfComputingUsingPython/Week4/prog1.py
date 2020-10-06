r, c = map(int, input().split())
for row in range(1, r + 1):
    for col in range(1, c + 1):
        en = " "
        if col == c:
            en = ""
        print((row - 1) * c + col, end=en)
    print()
