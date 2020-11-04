nums = list(map(int, input().split()))
z, c = 0, 0

for i in range(len(nums)):
    if nums[i] == 0:
        z += 1
    else:
        atr = " "
        if c == 0:
            atr = ""
        print(atr, end="")
        print(nums[i], end="")
        c += 1

for i in range(z):
    print(" 0", end="")
