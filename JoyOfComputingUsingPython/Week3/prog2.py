list_1 = []
for i in range(50):
    list_1.append(i + 1)
a, b = map(int, input().split())
ans = list_1[a:b]
for item in ans:
    print(item)
