import math

c, h = 50, 30
D = list(map(int, input().split(",")))

Q=[]

for d in D:
    q = round(math.sqrt((2 * c * d) / h))
    Q.append(q)

for i in range(len(Q)):
    if i == len(Q) - 1:
        print(Q[i], end="")
    else:
        print(Q[i], end=",")
