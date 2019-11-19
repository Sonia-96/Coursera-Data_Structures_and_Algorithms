# python3


def reach(adj, visited, x, y):
    visited[x] = True
    for vertex in adj[x]:
        if not visited[vertex]:
            reach(adj, visited, vertex, y)


if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    edges = []
    adjacency_list = [[] for _ in range(n_vertices + 1)]
    for i in range(n_edges):
        edges.append(tuple(map(int, input().split())))
    for (a, b) in edges:
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)
    u, v = map(int, input().split())
    visited = [False] * (n_vertices + 1)
    reach(adjacency_list, visited, u, v)
    if visited[v]:
        print(1)
    else:
        print(0)
