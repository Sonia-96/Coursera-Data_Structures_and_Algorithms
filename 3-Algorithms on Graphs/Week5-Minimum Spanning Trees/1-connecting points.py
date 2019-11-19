# python 3

import math


class MinimumLength:
    def __init__(self, n, edges):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.edges = edges

    def Find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.Find(self.parent[i])
        return self.parent[i]

    def Union(self, i, j):
        i_parent = self.Find(i)
        j_parent = self.Find(j)
        if i_parent == j_parent:
            return
        else:
            if self.rank[i_parent] > self.rank[j_parent]:
                self.parent[j_parent] = i_parent
            else:
                self.parent[i_parent] = j_parent
                if self.rank[i_parent] == self.rank[j_parent]:
                    self.rank[j_parent] += 1

    def Kruskal(self):
        dist = 0
        self.edges.sort(key=lambda i: i[2])
        for u, v, w in edges:
            if self.Find(u) != self.Find(v):
                dist += w
                self.Union(u, v)
        return dist


if __name__ == '__main__':
    n_vertices = int(input())
    points = [None] * n_vertices # 0-based index
    for i in range(n_vertices):
        a, b = map(int, input().split())
        points[i] = (a, b)
    edges = [] # (start, end, weight)

    for i in range(n_vertices):
        (x0, y0) = points[i]
        for j in range(i + 1, n_vertices):
            (x, y) = points[j]
            distance = math.sqrt((x - x0) ** 2 + (y - y0) ** 2)
            edges.append((i, j, distance))
    graph = MinimumLength(n_vertices, edges)
    min_length = graph.Kruskal()
    print("{0: .9f}".format(min_length))

