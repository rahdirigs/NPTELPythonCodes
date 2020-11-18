inplist = list(map(int, input().split()))

n = len(inplist)

modlist = []

for i in range(n):
    if inplist.count(i) != 0:
        modlist.append(i)
    else:
        modlist.append(-1)

for e in modlist:
    print(e, end=" ")
