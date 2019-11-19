# python3


import itertools


n, m = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(m)]

V = []
for i in range(1, n + 1):
    # each node must appear in the path
    Xij = list(j for j in range((i-1) * n + 1, i * n + 1))
    V.append(Xij)
    # each node can only appear once in the path
    lst = list(-x for x in Xij)
    subsets = list(map(list, itertools.combinations(lst, 2)))
    V += subsets

E = []
for i in range(1, n + 1):
    # every position in the path must be occupied
    pos = list(k for k in range(i, n * n + i, n))
    E.append(pos)
    # every position in the path can only have one node
    lst = list(-x for x in pos)
    subsets = list(map(list, itertools.combinations(lst, 2)))
    E += subsets

lst = list(i for i in range(1, n + 1))
subsets = list(map(list, itertools.combinations(lst, 2)))
C = []
# Nonadjacent nodes can't be adjacent in the path
for a, b in subsets:
    if [a,b] not in edges and [b,a] not in edges:
        for i in range(1, n):
            C.append([-((a - 1) * n + i), -((b - 1) * n + i + 1)])
            C.append([-((b - 1) * n + i), -((a - 1) * n + i + 1)])

n_clauses = len(V) + len(E) + len(C)
n_variables = n * n
print(n_clauses, n_variables)

for clause in V:
    for i in clause:
        print(i, end=' ')
    print(0)

for clause in E:
    for i in clause:
        print(i, end=' ')
    print(0)

for clause in C:
    for i in clause:
        print(i, end=' ')
    print(0)
