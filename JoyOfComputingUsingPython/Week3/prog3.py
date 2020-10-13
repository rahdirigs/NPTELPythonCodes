list_1 = list(range(1, 51))
a = int(input())
list_1.remove(a)
ans = 0
for item in list_1:
    if item % a == 0:
        ans = ans + 1
print(ans)
