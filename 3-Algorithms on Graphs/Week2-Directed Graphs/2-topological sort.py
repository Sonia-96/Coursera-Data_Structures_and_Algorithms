# python 3


def explore(graph, vertex, visited, post):
    global clock
    visited[vertex] = True
    for v in graph[vertex]:
        if not visited[v]:
            explore(graph, v, visited, post)
    post[vertex] = clock
    clock += 1


def topoSort(n, graph, visited, post):
    global clock
    for i in range(1, n + 1):
        if not visited[i]:
            explore(graph, i, visited, post)
    post = list(enumerate(post[1:], start=1))
    post.sort(key=lambda x:x[1], reverse=True)
    return post


if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    edges = [[] for _ in range(n_vertices + 1)]
    for i in range(n_edges):
        a, b = map(int, input().split())
        edges[a].append(b)
    visited = [False] * (n_vertices + 1)
    postorder = [0] * (n_vertices + 1)
    clock = 1
    postorder = topoSort(n_vertices, edges, visited, postorder)
    for v, post in postorder:
        print(v, end=' ')
