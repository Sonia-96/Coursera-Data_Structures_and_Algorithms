# python3


from collections import deque


def DAG(n, stock):
    adj = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            above = all([x < y for x, y in zip(stock[i], stock[j])])
            below = all([x > y for x, y in zip(stock[i], stock[j])])
            if above:
                adj[i][j] = 1
            elif below:
                adj[j][i] = 1
    return adj


def MakeNetwork(n, adj):
    graph = [[0] * (2 * n + 2) for _ in range(2 * n + 2)]
    for i in range(1, n + 1):
        graph[0][i] = 1
        for j in range(n):
            graph[i][n + 1 + j] = adj[i - 1][j]
    for k in range(n + 1, 2 * n + 1):
        graph[k][-1] = 1
    return graph


def HasPath(Gf, path):
    k = len(Gf)  # network中一共k个结点
    visited = [False] * k
    queue = deque([0])
    visited[0] = True
    while queue:
        u = queue.pop()
        if u == k - 1:
            return True
        for v in range(k):
            if not visited[v] and graph[u][v] > 0:
                queue.append(v)
                visited[v] = True
                path[v] = u
    return visited[-1]


def MaxFlow(Gf):
    k = len(Gf)
    path = [-1] * k
    flow = 0
    while HasPath(Gf, path):
        min_flow = float('inf')
        v = k - 1
        while v > 0:
            u = path[v]
            min_flow = min(min_flow, graph[u][v])
            v = u
        v = k - 1
        while v > 0:
            u = path[v]
            graph[u][v] -= min_flow
            graph[v][u] += min_flow
            v = u
        flow += min_flow
    return flow


if __name__ == '__main__':
    n, m = map(int, input().split())
    stock_data = [list(map(int, input().split())) for _ in range(n)]
    adj_matrix = DAG(n, stock_data)
    graph = MakeNetwork(n, adj_matrix)
    max_flow = MaxFlow(graph)
    min_charts = n - max_flow
    print(min_charts)
