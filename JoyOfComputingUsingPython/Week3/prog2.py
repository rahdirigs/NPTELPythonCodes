list_1 = list(range(1, 51))
a, b = map(int, input().split())
ans = list_1[a:b]
for item in ans:
    print(item)
