list_1 = []
for i in range(50):
    list_1.append(i + 1)
a = int(input())
list_1.remove(a)
ans = 0
for item in list_1:
    if item % a == 0:
        ans = ans + 1
print(ans)
