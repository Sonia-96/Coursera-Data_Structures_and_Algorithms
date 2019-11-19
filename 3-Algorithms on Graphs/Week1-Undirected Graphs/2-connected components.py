# python3


def explore(adj, visited, x):
    visited[x] = True
    for vertex in adj[x]:
        if not visited[vertex]:
            explore(adj, visited, vertex)


def number_of_components(n_vertices, adj, visited):
    n_cc = 0
    for i in range(1, n_vertices + 1):
        if not visited[i]:
            explore(adj, visited, i)
            n_cc += 1
            # print('vertex:', i, n_cc)
    return n_cc



if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    edges = []
    adjacency_list = [[] for _ in range(n_vertices + 1)]
    for i in range(n_edges):
        edges.append(tuple(map(int, input().split())))
    for (a, b) in edges:
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)
    visited = [False] * (n_vertices + 1)
    n_components = number_of_components(n_vertices, adjacency_list, visited)
    print(n_components)
