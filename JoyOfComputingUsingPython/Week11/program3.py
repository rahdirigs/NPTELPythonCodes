def getList(start, end):
    nums = []
    for i in range(start, end + 1):
        num = i
        ok = True
        while num > 0:
            d = num % 10
            if d % 2 != 0:
                ok = False
                break
            num = num // 10
        if not ok:
            continue
        else:
            nums.append(i)
    return nums
    

start, end = map(int, input().split(','))
nums = getList(start, end)

for i in range(len(nums)):
    if i == len(nums) - 1:
        print(nums[i], end='')
    else:
        print(nums[i], end=',')
