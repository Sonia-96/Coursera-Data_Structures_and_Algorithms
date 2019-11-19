# Use Python3

import sys
import threading


def compute_height(n, parents):
    T = [None] * n
    root = parents.index(-1)
    T[root] = 1
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
            if T[current]:
                T[vertex] = T[current] + height
                break
    return max(T)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()
