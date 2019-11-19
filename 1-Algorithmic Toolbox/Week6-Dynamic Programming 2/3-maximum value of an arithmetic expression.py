# Use Python3
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def MinAndMax(i, j, m, M, operation):
    minimum = float("+inf")
    maximum = float("-inf")
    for k in range(i, j):
        a = ops[operation[k - 1]](M[i][k], M[k+1][j])
        b = ops[operation[k - 1]](M[i][k], m[k+1][j])
        c = ops[operation[k - 1]](m[i][k], M[k+1][j])
        d = ops[operation[k - 1]](m[i][k], m[k+1][j])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return minimum, maximum


def maxValue(digit):
    n = len(digit)
    m = [[0]* (n + 1) for _ in range(n + 1)]
    M = [[0]* (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        m[i][i] = digit[i - 1]
        M[i][i] = digit[i - 1]
    for s in range(1, n): # i和j不能相等
        for i in range(1, n + 1 - s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j, m, M, operation)
    return M[1][n]


expression = input()
n = len(expression)
digit = [int(expression[i]) for i in range(0, n + 1, 2)]
operation = [expression[i] for i in range(1, n, 2)]
print(maxValue(digit))
