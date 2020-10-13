t = int(input())
x = 0
y = 0
for tc in range(t):
    direction, steps = input().split()
    move = int(steps)
    if direction == 'UP':
        y += move
    elif direction == 'DOWN':
        y -= move
    elif direction == 'LEFT':
        x -= move
    else:
        x += move
dist = (x ** 2 + y ** 2) ** (1 / 2)
ans = int(round(dist))
print(ans)
