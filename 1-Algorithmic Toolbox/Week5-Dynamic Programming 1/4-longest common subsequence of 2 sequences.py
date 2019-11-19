# Use Python3


def LCS(a,b):
    m = len(a)
    n = len(b)
    T = [[float('-inf') ] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        T[i][0] = 0
    for j in range(n + 1):
        T[0][j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
    print(T)
    return T[m][n]


na = int(input())
an = input()
a = an.split()
nb = int(input())
bn = input()
b = bn.split()
print(LCS(a, b))
