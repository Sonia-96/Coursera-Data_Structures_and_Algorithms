# python 3


import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self, root):
        if root == -1:
            return []
        self.inOrder(self.left[root])
        print(self.key[root], end=' ')
        self.inOrder(self.right[root])

    def preOrder(self, root):
        if root == -1:
            return []
        print(self.key[root], end=' ')
        self.preOrder(self.left[root])
        self.preOrder(self.right[root])

    def postOrder(self, root):
        if root == -1:
            return []
        self.postOrder(self.left[root])
        self.postOrder(self.right[root])
        print(self.key[root], end=' ')


def main():
    tree = TreeOrders()
    tree.read()
    tree.inOrder(0)
    print()
    tree.preOrder(0)
    print()
    tree.postOrder(0)
    print()


threading.Thread(target=main).start()
