name = input()
rev_name = name[::-1]

if name == rev_name:
    print("YES", end="")
else:
    print("NO", end="")
