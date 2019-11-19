# python3
# 增加了无解和多解情况

EPS = 1e-6
PRECISION = 6

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

def ReadData():
    size = int(input())
    a = []
    b = []
    for _ in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

def SelectPivotElement(pivot, a, used_rows):
    while pivot.row < len(a) and (used_rows[pivot.row] or a[pivot.row][pivot.col] == 0):
        pivot.row += 1
    print(pivot.row)
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


def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)
    used_rows = [False] * size
    for i in range(size):
        pivot = Position(0, i)
        pivot = SelectPivotElement(pivot, a, used_rows)
        if not pivot:
            return None
        else:
            print(pivot.row, pivot.col)
            SwapLines(a, b, used_rows, pivot)
            ProcessPivotElement(a, b, pivot, used_rows)
            print(a, b)
    return b

def PrintColumn(column):
    for e in column:
        print("{0:.6f}".format(e), end=' ')


if __name__ == '__main__':
    matrix = ReadData()
    solution = SolveEquation(matrix)
    PrintColumn(solution)
    exit(0)
