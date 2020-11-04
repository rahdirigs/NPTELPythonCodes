n = int(input())


def func(m):
    d, m_cp = 0, m
    s = 0

    if m == 0:
        return 0

    while m_cp != 0:
        d += 1
        s += (m_cp % 10)
        m_cp = m_cp // 10

    if d == 1:
        return m
    else:
        return func(s)


ans = func(n)
print(ans)
