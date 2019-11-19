# python3


import itertools
import copy

EPS = 1e-18
PRECISION = 18


class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

def SelectPivotElement(pivot, a, used_rows):
    while pivot.row < len(a) and (used_rows[pivot.row] or a[pivot.row][pivot.col] == 0):
        pivot.row += 1
    if pivot.row == len(a):
        return False
    else:
        return pivot

# swap row to top of non-pivot rows
def SwapLines(a, b, used_rows, pivot):
    a[pivot.col], a[pivot.row] = a[pivot.row], a[pivot.col]
    b[pivot.col], b[pivot.row] = b[pivot.row], b[pivot.col]
    used_rows[pivot.col], used_rows[pivot.row] = used_rows[pivot.row], used_rows[pivot.col]
    pivot.row = pivot.col

def ProcessPivotElement(a, b, pivot, used_rows):
    scale = a[pivot.row][pivot.col]
    if scale != 1:
        for i in range(len(a)):
            a[pivot.row][i] /= scale
        b[pivot.row] /= scale
    for i in range(len(a)):
        if i != pivot.row:
            multiple = a[i][pivot.col]
            for j in range(len(a)):
                a[i][j] -= a[pivot.row][j] * multiple
            b[i] -= b[pivot.row] * multiple
    used_rows[pivot.row] = True

def FindSubsets(n, m):
    lst = list(range(n + m + 1))
    subsets = list(map(set, itertools.combinations(lst, m)))
    return subsets

def GaussianElimination(subset, A, B):
    # make equation
    a = []
    b = []
    for i in subset:
        a.append(copy.deepcopy(A[i]))
        b.append(copy.deepcopy(B[i]))
    # solve equation
    size = len(a)
    used_rows = [False] * size
    for i in range(size):
        pivot = Position(0, i)
        pivot = SelectPivotElement(pivot, a, used_rows)
        if not pivot:
            return None
        else:
            SwapLines(a, b, used_rows, pivot)
            ProcessPivotElement(a, b, pivot, used_rows)
    return b

def CheckSolution(solution, A, B, m):
    for i in range(len(A)):
        sum = 0
        for j in range(m):
            sum += A[i][j] * solution[j]
        if sum - B[i] > 0.00001:
            return False
    return True

def Solve(subsets, A, B, pleasure, m):
    solutions = []
    for subset in subsets:
        solution = GaussianElimination(subset, A, B)
        if solution is not None:
            if CheckSolution(solution, A, B, m):
                solutions.append(solution)
    if len(solutions) == 0:
        print('No solution')
    else:
        best = float('-inf')
        result = None
        for s in solutions:
            p = 0
            for i in range(m):
                p += pleasure[i] * s[i]
            if p > best:
                best = p
                result = s
        temp = 0
        for e in result:
            temp += e
        if temp > 1000000000:
            print('Infinity')
        else:
            print('Bounded solution')
            for e in result:
                print("{0:.18f}".format(e), end=' ')


if __name__ == '__main__':
    n_equations, n_variables = map(int, input().split())
    A = []
    for i in range(n_equations):
        A.append(list(map(int, input().split())))
    B = list(map(int, input().split()))
    pleasure = list(map(int, input().split()))
    for i in range(n_variables):
        lst = [0] * n_variables
        lst[i] = -1
        A.append(lst)
        B.append(0)
    A.append([1] * n_variables)
    B.append(1000000001)
    # print('A', A, 'B', B)
    sub = FindSubsets(n_equations, n_variables)
    # print('subsets', sub)

    Solve(sub, A, B, pleasure, n_variables)
    exit(0)




