# python3


from collections import deque


# edges[a]: [(end, weight), ...]
# H = [[node1, distance1], [node2, distance2],...]
class MinimumCost:
    def __init__(self, n, edges, start, end):
        self.edges = edges
        self.H = deque()
        for i in range(n):
            self.H.append([i + 1, float('inf')])
        self.dist = [float('inf')] * (n + 1)
        self.processed = [False] * (n + 1)
        self.start = start
        self.end = end

    def SiftDown(self, i):
        min_index = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < len(self.H) and self.H[left_child][1] < self.H[min_index][1]:
            min_index = left_child
        if right_child < len(self.H) and self.H[right_child][1] < self.H[min_index][1]:
            min_index = right_child
        if min_index != i:
            self.H[i], self.H[min_index] = self.H[min_index], self.H[i]
            self.SiftDown(min_index)

    def SiftUp(self, i):
        while i > 0 and self.H[i][1] < self.H[(i - 1) // 2][1]:
            self.H[i], self.H[(i - 1) // 2] = self.H[(i - 1) // 2], self.H[i]
            i = (i - 1) // 2

    def _SiftUp(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.H[i][1] < self.H[parent][1]:
                self.H[i], self.H[parent] = self.H[parent], self.H[i]
                i = parent

    def ExtractMin(self):
        result = self.H[0]
        self.H[0] = self.H[len(self.H) - 1]
        self.H.pop()
        self.SiftDown(0)
        return result

    def Insert(self, node, p):
        self.H.append([node, p])
        self.SiftUp(len(self.H) - 1)

    def ChangePriority(self, i, new):
        self.H[i][1] = new
        self.SiftUp(i)

    # edges[a]: [(end, weight), ...]
    # H = [[node1, distance1], [node2, distance2],...]
    def Dijkstra(self):
        self.dist[self.start] = 0
        self.ChangePriority(self.start - 1, 0)
        while self.H:
            u, dist_u = self.ExtractMin()
            if not self.processed[u]:
                self.processed[u] = True
                for v, weight in self.edges[u]:
                    if self.dist[v] > self.dist[u] + weight:
                        self.dist[v] = self.dist[u] + weight
                        self.Insert(v, self.dist[v])
        if self.dist[self.end] != float('inf'):
            return self.dist[self.end]
        else:
            return -1


if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    edges = [[] for _ in range(n_vertices + 1)]
    for i in range(n_edges):
        a, b, w = map(int, input().split())
        edges[a].append((b, w))
    s, e = map(int, input().split())
    flights = MinimumCost(n_vertices, edges, s, e)
    min_cost = flights.Dijkstra()
    print(min_cost)
