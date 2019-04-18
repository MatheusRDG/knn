def calculateDistance(s, t):
    n, m = len(s), len(t)
    if n == 0:
        return m
    if m == 0:
        return n
    d = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        d[i][0] = i
    for i in range(1, m + 1):
        d[0][i] = i
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + cost)
    return d[n][m]