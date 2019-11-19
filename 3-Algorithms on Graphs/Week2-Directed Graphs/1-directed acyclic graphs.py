# python3


def explore(edges, vertex, visited, stack, is_dag):
    visited[vertex] = True
    stack.append(vertex)
    for v in edges[vertex]:
        if v in stack:
            is_dag[0] = False
        if not visited[v]:
            explore(edges, v, visited, stack, is_dag)
    stack.pop()


def is_DAG(edges, visited, n):
    is_dag = [True]
    stack = []
    for i in range(1, n + 1):
        if not visited[i]:
            explore(edges, i, visited, stack, is_dag)
            if not is_dag[0]:
                return False
    return True


if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    edges = [[] for _ in range(n_vertices + 1)]
    for i in range(n_edges):
        a, b = map(int, input().split())
        edges[a].append(b)
    visited = [False] * (n_vertices + 1)
    check = is_DAG(edges, visited, n_vertices)
    if check:
        print(0)
    else:
        print(1)
