# python3


from collections import deque


def HasPath(Gf, path):
    n = len(Gf)
    visited = [False] * n
    visited[0] = True
    queue = deque([0])
    while queue:
        temp = queue.popleft()
        if temp == n - 1:
            return True
        for i in range(n):
            if not visited[i] and Gf[temp][i] > 0:
                queue.append(i)
                visited[i] = True
                path[i] = temp
    return visited[n-1]


def MaxFlow(Gf):
    flow = 0
    n = len(Gf)
    path = list(range(n))
    while HasPath(Gf, path):
        min_flow = float('inf')
        # find cf(p)
        v = n - 1
        while v != 0:
            u = path[v]
            min_flow = min(min_flow, Gf[u][v])
            v = u
        # add flow in every edge of the augument path
        v = n - 1
        while v != 0:
            u = path[v]
            Gf[u][v] -= min_flow
            Gf[v][u] += min_flow
            v = u
        flow += min_flow
    return flow


if __name__ == '__main__':
    n_city, n_edges = map(int, input().split())
    residual_graph = [[0] * n_city for i in range(n_city)]
    for _ in range(n_edges):
        u, v, capacity = map(int, input().split())
        residual_graph[u - 1][v - 1] += capacity
    print(residual_graph)
    max_flow = MaxFlow(residual_graph)
    print(max_flow)
