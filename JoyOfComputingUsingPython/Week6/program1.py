L = list(map(int, input().split()))
modL = []
for item in L:
    if modL.count(item) == 0:
        modL.append(item)
for item in modL:
    print(item, end=" ")
