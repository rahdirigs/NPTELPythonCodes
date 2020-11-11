inp = input()

holes = {'A': 1, 'B': 2, 'D': 1, 'O': 1, 'P': 1, 'R': 1, 'Q': 1}
total_holes = 0

for c in inp:
    if c in holes.keys():
        total_holes += holes[c]

print(total_holes, end="")
