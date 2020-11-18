inp = list(map(int, input().split()))

n = len(inp)
inp.sort()

flag = False
for i in range(n):
    if inp[i] != i + 1:
        print(i + 1, end="")
        flag = True
        break

if not flag:
    print(n + 1, end="")
