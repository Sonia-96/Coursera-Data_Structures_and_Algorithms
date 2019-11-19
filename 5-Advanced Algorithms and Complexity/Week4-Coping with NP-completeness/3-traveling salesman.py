# python3


from itertools import permutations
from itertools import combinations
from collections import deque

INF = 10 ** 9

def read_data():
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]  # adjacent matrix
    for _ in range(m):
        u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    return graph


def print_answer(path_weight, path):
    print(path_weight)
    if path_weight == -1:
        return
    print(' '.join(map(str, path)))


def optimal_path(graph):
    n = len(graph)
    C = [[INF for _ in range(n)] for __ in range(1 << n)]  # 纵坐标是1~2^n（因为共2^n个子集S）， 横坐标是1~n
    backtrack = [[(-1, -1) for _ in range(n)] for __ in range(1 << n)]
    C[1][0] = 0
    for size in range(1, n):
        for S in combinations(range(1, n), size):
            S = (0,) + S
            k = sum([1 << i for i in S])
            for i in S:
                if i != 0:
                    for j in S:
                        if j != i:
                            m = k ^ (1 << i)
                            curr = C[m][j] + graph[j][i]
                            if curr < C[k][i]:
                                C[k][i] = curr
                                backtrack[k][i] = (m, j)
    best_ans, index2 = min([(C[-1][i] + graph[i][0], i) for i in range(n)])

    if best_ans >= INF:
        return -1, []

    path = deque()
    index1 = (1 << n) - 1
    while index1 != -1:
        path.appendleft(index2 + 1)
        index1, index2 = backtrack[index1][index2]
    return best_ans, path


if __name__ == '__main__':
    print_answer(*optimal_path(read_data()))
