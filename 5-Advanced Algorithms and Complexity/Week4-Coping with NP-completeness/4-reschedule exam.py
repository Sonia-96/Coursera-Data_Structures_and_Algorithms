# python3


import sys
import threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class Node:
    def __init__(self, i):
        self.r = 3 * i - 2
        self.g = 3 * i - 1
        self.b = 3 * i


def ReduceToTwoSAT(colors, edges):
    n = len(colors)
    C = []
    for i in range(1, n + 1):
        node = Node(i)
        if colors[i - 1] == 'R':
            # C.append((-node.r))
            C.append((node.g, node.b))
            C.append((-node.g, -node.b))
        elif colors[i - 1] == 'G':
            # C.append((-node.g))
            C.append((node.r, node.b))
            C.append((-node.r, -node.b))
        elif colors[i - 1] == 'B':
            # C.append((-node.b))
            C.append((node.r, node.g))
            C.append((-node.r, -node.g))
    for a, b in edges:
        u, v = Node(a), Node(b)
        C.append((-u.r, -v.r))
        C.append((-u.g, -v.g))
        C.append((-u.b, -v.b))
    return C


def TwoSATtoGraph(n, C):
    graph = [[] for _ in range(2 * n + 1)]  # 共3n个变量
    rev_graph = [[] for _ in range(2 * n + 1)]
    for a,b in C:
        if a > 0 and b > 0:
            graph[a + n].append(b)
            graph[b + n].append(a)
            rev_graph[b].append(a + n)
            rev_graph[a].append(b + n)
        elif a < 0 and b < 0:
            graph[-a].append(-b + n)
            graph[-b].append(-a + n)
            rev_graph[-b + n].append(-a)
            rev_graph[-a + n].append(-b)
        elif a < 0 and b > 0:
            graph[-a].append(b)
            graph[b + n].append(-a + n)
            rev_graph[b].append(-a)
            rev_graph[-a + n].append(b + n)
        elif a > 0 and b < 0:
            graph[a + n].append(-b + n)
            graph[-b].append(a)
            rev_graph[-b + n].append(a + n)
            rev_graph[a].append(-b)
    return graph, rev_graph


def PostOrder(i, graph, visited, post):
    global clock
    visited[i] = True
    for v in graph[i]:
        if not visited[v]:
            PostOrder(v, graph, visited, post)
    post[i] = clock
    clock += 1


def DFS(n, graph):
    global clock
    visited = [False] * (2 * n + 1)
    post = [0] * (2 * n + 1)
    for v in range(1, 2 * n + 1):
        if not visited[v]:
            PostOrder(v, graph, visited, post)
    post = list(enumerate(post[1:], start=1))
    post.sort(key=lambda x: x[1], reverse=True)
    post_vertex = []
    for v, order in post:
        post_vertex.append(v)
    return post_vertex


def Explore(i, graph, visited, SCC, SCC_number, u):
    visited[i] = True
    SCC.append(i)
    SCC_number[i] = u
    for v in graph[i]:
        if not visited[v]:
            Explore(v, graph, visited, SCC, SCC_number, u)


def FindSCCs(n, rev_graph, graph):
    global clock
    post_vertex = DFS(n, rev_graph)
    visited = [False] * (2 * n + 1)
    SCCs = []
    SCC_number = [0] * (2 * n + 1)
    u = 1
    for i in post_vertex:
        if not visited[i]:
            SCC = []
            Explore(i, graph, visited, SCC, SCC_number, u)
            SCCs.append(SCC)
            u += 1
    return SCCs, SCC_number


def SolveTwoSAT(n, rev_graph, graph):
    SCCs, SCC_number = FindSCCs(n, rev_graph, graph)
    for i in range(1, n + 1):
        if SCC_number[i] == SCC_number[i + n]:
            return False
    solution = [[] for _ in range(2 * n + 1)]
    assigned = [False] * (2 * n + 1)
    for SCC in SCCs:
        for v in SCC:
            if not assigned[v]:
                assigned[v] = True
                solution[v] = 1
                if v > n:
                    solution[v - n] = 0
                    assigned[v - n] = True
                else:
                    solution[v + n] = 0
                    assigned[v + n] = True
    return solution


clock = 1
def main():
    n, m = map(int, input().split())
    colors = input()
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))
    C = ReduceToTwoSAT(colors, edges)
    graph, rev_graph = TwoSATtoGraph(3 * n, C)
    result = SolveTwoSAT(3 * n, rev_graph, graph)
    if not result:
        print('Impossible')
    else:
        for i in range(1, 3 * n + 1):
            if result[i] == 1:
                if i % 3 == 1:
                    print('R', end='')
                elif i % 3 == 2:
                    print('G', end='')
                elif i % 3 == 0:
                    print('B', end='')


threading.Thread(target=main).start()
