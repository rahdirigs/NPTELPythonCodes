n = int(input())
matrix = []

for r in range(n):
    matrix.append(list(map(int, input().rstrip().split())))

for r in range(n):
    for c in range(n):
        if c > r:
            matrix[r][c] = 0

for r in range(n):
    atr = " "
    for c in range(n):
        if c == n - 1:
            atr = ""
        print(matrix[r][c], end=atr)
    if r < n - 1:
        print()
