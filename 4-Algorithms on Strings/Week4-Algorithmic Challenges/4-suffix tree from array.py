# python3


import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class SuffixTree:
    class Node:
        def __init__(self, node, depth, start, end):
            self.parent = node
            self.children = {}
            self.depth = depth  # string depth
            self.start = start
            self.end = end
            self.visited = False

    def __init__(self, s, order, LCP):
        self.s = s
        self.ele = ['$', 'A', 'C', 'G', 'T']
        self.order = order
        self.LCP = LCP
        self.root = self.Node(None, 0, -1, -1)

    def CreateNewLeaf(self, node, suffix):
        leaf = self.Node(node, len(self.s) - suffix, suffix + node.depth, len(self.s))
        node.children[self.s[leaf.start]] = leaf
        return leaf

    def BreakEdge(self, node, mid_start, offset):
        mid_char = self.s[mid_start]
        left_char = self.s[mid_start + offset]
        mid = self.Node(node, node.depth + offset, mid_start, mid_start + offset)
        mid.children[left_char] = node.children[mid_char]
        node.children[mid_char].parent = mid
        node.children[mid_char].start += offset
        node.children[mid_char] = mid
        return mid

    def STFromSA(self):
        lcp_prev = 0
        cur = self.root
        for i in range(len(self.s)):
            suffix = self.order[i]
            while cur.depth > lcp_prev:
                cur = cur.parent
            if cur.depth == lcp_prev:
                cur = self.CreateNewLeaf(cur, suffix)
            else:
                # break edge and got 3 nodes: mid, left(exist already), right(new suffix)
                mid_start = self.order[i - 1] + cur.depth  # the start of mid-node
                offset = lcp_prev - cur.depth  # the number of characters of mid-node
                mid = self.BreakEdge(cur, mid_start, offset)
                cur = self.CreateNewLeaf(mid, suffix)
            if i < len(self.s) - 1:
                lcp_prev = self.LCP[i]

    def PrintEdges(self, cur):
        cur.visited = True
        if cur != self.root:
            print(cur.start, cur.end)
        for i in range(5):
            child = cur.children.get(self.ele[i], None)
            if child is not None and not child.visited:
                self.PrintEdges(child)


def main():
    text = input()
    suffix_array = list(map(int, input().split()))
    lcp = list(map(int, input().split()))
    print(text)
    suffix_tree = SuffixTree(text, suffix_array, lcp)
    suffix_tree.STFromSA()
    suffix_tree.PrintEdges(suffix_tree.root)


threading.Thread(target=main).start()
