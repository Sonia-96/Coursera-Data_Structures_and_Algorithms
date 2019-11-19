# python3


from collections import deque


def MakeNetwork(n, m, bip):
    graph = [[0] * (n + m + 2) for _ in range(n + m + 2)]
    for i in range(1, n + 1):
        graph[0][i] = 1
        for j in range(m):
            graph[i][n + 1 + j] = bip[i - 1][j]
    for k in range(n + 1, n + m + 1):
        graph[k][-1] = 1
    return graph


def HasPath(Gf, path):
    V = len(Gf)
    visited = [False] * V
    visited[0] = True
    queue = deque([0])
    while queue:
        u = queue.popleft()
        if u == V - 1:
            return True
        for v in range(V):
            if not visited[v] and Gf[u][v] > 0:
                queue.append(v)
                visited[v] = True
                path[v] = u
    return visited[V - 1]


def MaxFlow(Gf, n):
    V = len(Gf)
    path = list(range(V))
    while HasPath(Gf, path):
        min_flow = float('inf')
        v = V - 1
        while v != 0:
            u = path[v]
            min_flow = min(min_flow, Gf[u][v])
            v = u
        v = V - 1
        while v != 0:
            u = path[v]
            Gf[u][v] -= min_flow
            Gf[v][u] += min_flow
            v = u
    matches = [-1] * n
    for i in range(V):
        if Gf[V-1][i] == 1:
            person = i - n
            flight = Gf[i].index(1)
            matches[flight - 1] = person
    return matches


if __name__ == '__main__':
    n_flights, n_crew = map(int, input().split())
    bipartite = [list(map(int, input().split())) for i in range(n_flights)]

    residual_graph = MakeNetwork(n_flights, n_crew, bipartite)
    matching = MaxFlow(residual_graph, n_flights)

    for e in matching:
        print(e, end=' ')
