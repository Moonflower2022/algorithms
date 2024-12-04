# CREDIT: FRIEND FROM SCHOOL

from collections import defaultdict

n = 5
s = 12

values = [6, 10, 4, 11, 20]
weights = [1, 2, 3, 4, 5]

cs = defaultdict(lambda: defaultdict(lambda: -1))


def dp(i, r):
    if i == n or r == 0:
        return 0

    weight = weights[i]
    value = values[i]

    if weight > r:
        cs[i][r] = dp(i + 1, r)
        return cs[i][r]

    c = cs[i][r]

    if c != -1:
        return c

    c = max(dp(i + 1, r - weight) + value, dp(i + 1, r))

    cs[i][r] = c
    return c


print(dp(0, s))