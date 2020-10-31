n = int(input())

matrix = []
ans = []
for r in range(n):
    matrix.append(list(map(int, input().rstrip().split())))


def createList(mat):
    m = len(mat)
    ret = []

    for pp in range(m // 2):
        for i in range(pp, m - pp):
            ret.append(mat[i][pp])

        for i in range(pp + 1, m - pp):
            ret.append(mat[m - pp - 1][i])

        for i in range(m - pp - 2, pp - 1, -1):
            ret.append(mat[i][m - pp - 1])

        for i in range(m - pp - 2, pp, -1):
            ret.append(mat[pp][i])

    if m % 2 == 1:
        ret.append(mat[m // 2][m // 2])

    return ret


ans = createList(matrix)
for item in ans:
    print(item, end=" ")
