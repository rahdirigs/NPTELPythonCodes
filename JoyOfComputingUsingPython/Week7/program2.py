n = int(input())

matrix = []
matrix_rot = []
for r in range(n):
    matrix.append(list(map(int, input().rstrip().split())))


def rotateMatrix(mat):
    if not len(mat):
        return

    top = 0
    bottom = len(mat) - 1

    left = 0
    right = len(mat[0]) - 1

    while left < right and top < bottom:
        prev = mat[top + 1][left]

        for k in range(left, right + 1):
            curr = mat[top][k]
            mat[top][k] = prev
            prev = curr
        top += 1

        for k in range(top, bottom + 1):
            curr = mat[k][right]
            mat[k][right] = prev
            prev = curr
        right -= 1

        for k in range(right, left - 1, -1):
            curr = mat[bottom][k]
            mat[bottom][k] = prev
            prev = curr

        bottom -= 1
        for k in range(bottom, top - 1, -1):
            curr = mat[k][left]
            mat[k][left] = prev
            prev = curr

        left += 1

    return mat


matrix_rot = rotateMatrix(matrix)

for i in range(n):
    atr = " "
    for j in range(n):
        if j == n - 1:
            atr = ""
        print(matrix_rot[i][j], end=atr)
    if i < n - 1:
        print()
