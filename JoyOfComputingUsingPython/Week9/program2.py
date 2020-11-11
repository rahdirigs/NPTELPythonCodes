inp = input()
n = len(inp)

ans = ''
possible = True

for i in range(n // 2):
    c1, c2 = inp[i], inp[n - i - 1]
    if c1 == c2 and c1 == '.':
        ans += 'a'
    elif c1 == c2:
        ans += c1
    elif c1 == '.':
        ans += c2
    elif c2 == '.':
        ans += c1
    else:
        possible = False
        break

if possible:
    rev_ans = ans[::-1]
    if n & 1:
        mid = 'a' if inp[n // 2] == '.' else inp[n // 2]
        ans = ans + mid + rev_ans
    else:
        ans += rev_ans
    print(ans, end="")
else:
    print("-1", end="")
