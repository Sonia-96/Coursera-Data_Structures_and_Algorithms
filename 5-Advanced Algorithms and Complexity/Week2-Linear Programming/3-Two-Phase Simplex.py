# python3


def ChoosePivotColumn(m, n, s, A):
    minimum = -0.001
    enter = - 1
    # choose pivot column
    for j in range(m + n + s + 2):
        if A[-1][j] < minimum:
            minimum = A[-1][j]
            enter = j  # pivot.column
    return enter


# Gauss-Jordan elimination
def Pivoting(depart, enter, m, n, s, A, b):
    pivot = A[depart][enter]
    if pivot != 1:
        for k in range(m + n + s + 2):
            A[depart][k] /= pivot
        b[depart] /= pivot
    for i in range(len(A)):
        if i != depart:
            a = A[i][enter]
            for j in range(m + n + s + 2):
                A[i][j] -= A[depart][j] * a
            b[i] -= b[depart] * a


def PhaseOne(m, n, s, A, b, basis):
    enter = ChoosePivotColumn(m, n, s, A)  # pivot column
    while enter != -1:
        # choose pivot
        depart = -1
        min_ratio = float('inf')
        for i in range(n):
            if A[i][enter] > 0:
                ratio = b[i]/A[i][enter]
                if ratio < min_ratio:
                    min_ratio = ratio
                    depart = i  # pivot.row
        basis[depart] = enter
        Pivoting(depart, enter, m, n, s, A, b)
        enter = ChoosePivotColumn(m, n, s, A)
    return b[-1]


def Transition(m, n, s, A, basis, b, arti):
    enter = -1
    for i in range(n):
        if basis[i] in arti:
            for j in range(m + n):
                if A[i][j] != 0:
                    enter = j
                    basis[i] = j
                    break
            Pivoting(i, enter, m, n, s, A, b)


def PhaseTwo(m, n, s, A, b, basis):
    ans = 0
    A.pop()
    b.pop()
    enter = ChoosePivotColumn(m, n, -2, A)  # pivot column
    while enter != -1:
        # choose pivot
        depart = -1
        min_ratio = float('inf')
        for i in range(n):
            if A[i][enter] > 0:
                ratio = b[i]/A[i][enter]
                if ratio < min_ratio:
                    min_ratio = ratio
                    depart = i  # pivot.row
        if depart == -1:
            ans = 1
            break
        else:
            basis[depart] = enter
            Pivoting(depart, enter, m, n, s, A, b)
            enter = ChoosePivotColumn(m, n, -2, A)
    return ans


def TwoPhaseSimplex(m, n, s, A, b, basis, arti_var):
    w = PhaseOne(m, n, s, A, b, basis)
    if w < -0.001:
        print('No solution')
    else:
        Transition(m, n, s, A, basis, b, arti_var)
        ans = PhaseTwo(m, n, s, A, b, basis)
        if ans == 1:
            print('Infinity')
        else:
            solution = [0] * (m + n)
            for i in range(n):
                solution[basis[i]] = b[i]
            print('Bounded solution')
            for k in range(m):
                print("{0:.18f}".format(solution[k]), end=' ')


if __name__ == '__main__':
    n, m = map(int, input().split())
    A = []
    for _ in range(n):
        A += [list(map(int, input().split()))]
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b.append(0)
    arti = []
    for i in range(n + 1):
        if b[i] < 0:
            arti.append(i)
    s = len(arti)
    basis = []
    arti_var = []
    count = 0
    for i in range(n):
        lst = [0] * (n + s + 2)
        lst[i] = 1
        if b[i] >= 0:
            A[i] += lst
            basis.append(m + i)
        else:
            b[i] = -b[i]
            temp = [-e for e in A[i]]
            temp += [-e for e in lst]
            temp[n + m + count] = 1
            basis.append(n + m + count)
            arti_var.append(n + m + count)
            count += 1
            A[i] = temp
    temp = [-e for e in c] + [0] * (n + s + 2)
    temp[-2] = 1
    A += [temp]
    # w
    temp = []
    for j in range(m + n):
        a = 0
        for e in arti:
            a += A[e][j]
        temp.append(-a)
    temp += [0] * (s + 2)
    temp[-1] = 1
    A += [temp]
    a = 0
    for e in arti:
        a += b[e]
    b.append(-a)
    TwoPhaseSimplex(m, n, s, A, b, basis, arti_var)
