# python3


class Node:
    def __init__(self, i):
        self.r = 3 * i - 2
        self.g = 3 * i - 1
        self.b = 3 * i


n_vertices, n_edges = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(n_edges)]

V = []
for i in range(1, n_vertices + 1):
    node = Node(i)
    V.append([node.r, node.g, node.b])
    V.append([-node.r, -node.g])
    V.append([-node.r, -node.b])
    V.append([-node.g, -node.b])

E = []
for a, b in edges:
    u = Node(a)
    v = Node(b)
    E.append([-u.r, -v.r])
    E.append([-u.g, -v.g])
    E.append([-u.b, -v.b])

n_clauses = len(V) + len(E)
n_variables = n_vertices * 3
print(n_clauses, n_variables)

for clause in V:
    for i in clause:
        print(i, end=' ')
    print(0)

for clause in E:
    for i in clause:
        print(i, end=' ')
    print(0)


