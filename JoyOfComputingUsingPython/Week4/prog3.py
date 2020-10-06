import random


def swap(list_cp, idx1, idx2):
    list_cp[idx1], list_cp[idx2] = list_cp[idx2], list_cp[idx1]
    return list_cp


list_1 = []
n = int(input())
for i in range(n):
    list_1.append(int(input()))
while sorted(list_1) != list_1:
    i = random.randrange(0, n)
    j = random.randrange(0, n)
    swap(list_1, i, j)
for item in list_1:
    print(item, end=" ")
