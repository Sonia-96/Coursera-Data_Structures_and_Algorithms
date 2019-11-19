# python3


n, m = list(map(int, input().split()))
A = []
for i in range(n):
    A += [list(map(int, input().split()))]
b = list(map(int, input().split()))

lst1 = [0, 1]
lst2 = [[0, 0], [1, 0], [0, 1], [1, 1]]
lst3 = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1], [0, 1, 1], [1, 1, 1]]

clauses = []
for i in range(n):
    # find non-zero coefficients
    C = []  # non-zero coefficients
    for j in range(m):
        if A[i][j] != 0:
            C.append(j)
    if len(C) == 0:
        if b[i] < 0:
            clauses = [[1], [-1]]
            break
        else:
            continue
    # add clauses which make inequalities unsatisfiable
    elif len(C) == 1:
        for u in lst1:
            if A[i][C[0]] * u > b[i]:
                if u == 0:
                    clauses.append([C[0] + 1])
                else:
                    clauses.append([- C[0] - 1])
    elif len(C) == 2:
        for u, v in lst2:
            if A[i][C[0]] * u + A[i][C[1]] * v > b[i]:
                temp = []
                for k in range(2):
                    if [u, v][k] == 0:
                        temp += [C[k] + 1]
                    else:
                        temp += [- C[k] - 1]
                clauses.append(temp)
    elif len(C) == 3:
        for u, v, w in lst3:
            if A[i][C[0]] * u + A[i][C[1]] * v + A[i][C[2]] * w > b[i]:
                temp = []
                for k in range(3):
                    if [u, v, w][k] == 0:
                        temp += [C[k] + 1]
                    else:
                        temp += [- C[k] - 1]
                clauses.append(temp)

if len(clauses) == 0:
    clauses = [[1, -1]]
    n_variables = 1
elif clauses == [[1], [-1]]:
    n_variables = 1
else:
    n_variables = m

print(len(clauses), n_variables)
for clause in clauses:
    for i in clause:
        print(i, end=' ')
    print(0)
