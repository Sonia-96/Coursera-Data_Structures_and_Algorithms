# Use Python3


def LCS3(a, b, c):
    m = len(a)
    n = len(b)
    l = len(c)
    T = [[[float("-inf")] * (l + 1) for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(l + 1):
                if i == 0 or j == 0 or k == 0:
                    T[i][j][k] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, l + 1):
                if a[i - 1] == b[j - 1] and a[i - 1] == c[k - 1]:
                    T[i][j][k] = T[i - 1][j - 1][k - 1] + 1
                else:
                    T[i][j][k] = max(T[i-1][j][k], T[i][j - 1][k], T[i][j][k - 1], T[i - 1][j - 1][k], T[i - 1][j][k - 1], T[i][j - 1][k - 1])
    return T[m][n][l]


na = int(input())
an = input()
a = an.split()
nb = int(input())
bn = input()
b = bn.split()
nc = int(input())
cn = input()
c = cn.split()
print(LCS3(a, b, c))

