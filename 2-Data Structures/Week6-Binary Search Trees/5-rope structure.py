# python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


# Splay tree implementation

# Vertex of a splay tree
class Vertex:
    def __init__(self, key, size, char, left, right, parent):
        (self.key, self.size, self.char, self.left, self.right, self.parent) = (key, size, char, left, right, parent)


class Rope:
    def __init__(self, s):
        global root
        self.s = s
        for idx, char in enumerate(self.s):
            v = Vertex(idx, 1, char, None, None, None)
            root = self.merge(root, v)

    def get_size(self, v):
        if v == None:
            return 0
        return v.size

    def update(self, v):
        # print("updating")
        if v == None:
            return
        v.size = self.get_size(v.left) + self.get_size(v.right) + 1
        if v.left != None:
            v.left.parent = v
        if v.right != None:
            v.right.parent = v

    def smallRotation(self, v):
        parent = v.parent
        if parent == None:
            return
        grandparent = v.parent.parent
        if parent.left == v:
            # rotate to the right; so the previous right child of v is now the left child
            # of v's parent (which is now v's right child)
            m = v.right
            v.right = parent
            parent.left = m
        else:
            # similarly, rotate v to the left; so now its parent becomes its left child
            # and any left child of v becomes the former parent's right child
            m = v.left
            v.left = parent
            parent.right = m
        self.update(parent)
        self.update(v)
        v.parent = grandparent
        if grandparent != None:
            if grandparent.left == parent:
                grandparent.left = v
            else:
                grandparent.right = v

    def bigRotation(self, v):
        # if "straight" up either left or right, zig-zig
        if v.parent.left == v and v.parent.parent.left == v.parent:
            # Zig-zig
            self.smallRotation(v.parent)
            self.smallRotation(v)
        elif v.parent.right == v and v.parent.parent.right == v.parent:
            # Zig-zig
            self.smallRotation(v.parent)
            self.smallRotation(v)
        # otherwise zig-zag -- see slides for pictures
        else:
            # Zig-zag
            self.smallRotation(v)
            self.smallRotation(v)

    def splay(self, v):
        if v == None:
            return None
        while v.parent != None:
            # as long as grandparent exists, bigRotation is always called
            # -- small rotation gets called once at the end, followed by loop break
            if v.parent.parent == None:
                self.smallRotation(v)
                break
            self.bigRotation(v)
        # return the new root node after splay
        return v

    def find(self, root, order_stat):
        v = root
        if v is None:
            return None
        if v.left is None:
            s = 0
        else:
            s = self.get_size(v.left)
        if order_stat == s + 1:
            return v
        elif order_stat < s + 1:
            return self.splay(self.find(v.left, order_stat))
        else:
            return self.splay(self.find(v.right, order_stat - s - 1))

    def split(self, root):
        # (result, root) = self.find(root, key)
        # if find returned result = None, there are no nodes in the tree with keys above
        # the given key, so just return the root node for the single tree and do no
        # updates
        if root == None:
            return (root, None)

        # otherwise, splay the next bigger node and set right new tree node to that node
        right = root
        # left is a temp var for the child to the left of the splayed node
        left = right.left
        # then set right.left = None to split the trees effectively
        right.left = None
        # and ensure that left is now root node for its own tree too
        if left != None:
            left.parent = None
        # update the values on these two nodes
        self.update(left)
        self.update(right)
        # return pointers to the root nodes for two new trees
        return (left, right)

    def merge(self, left, right):
        # if either of the nodes don't exist, just return the one that does

        if left == None:
            # print("cond1")
            return right
        if right == None:
            # print("cond2")
            return left

        while right.left != None:
            right = right.left
        # splay the leftmost node on the "right" tree being merged -- so, the smallest
        # value on the bigger tree is now root
        right = self.splay(right)
        # the right side of the right tree is still good, need to set its left side to
        # be the left tree
        right.left = left
        # update the whole tree (this will take care of sum and settings its chidlrens
        # parent pointers) and return
        self.update(right)
        return right

    def in_order(self):
        # print pre-order tree traversal for debugging
        def _in_order(r):
            if r is None:
                return
            _in_order(r.left)

            # key_result.append(r.key)
            char_result.append(r.char)
            # size_result.append(r.size)
            _in_order(r.right)
            return

        global root
        # key_result = []
        char_result = []
        # size_result = []
        _in_order(root)
        # return key_result, char_result, size_result
        return char_result

    def insert(self, x):
        # print("inserting value: %f" % x)
        global root
        # split the tree starting at root for value x
        (left, right) = self.split(root, x)
        new_vertex = None
        # if x is bigger than the whole tree, or if the right tree doesn't happen to have
        # key=x, need to create a new vertex with key (and current sum) of x
        if right == None or right.key != x:
            new_vertex = Vertex(x, x, None, None, None)
        # then merge left with the new_vertex if it was created, then merge again with right
        # -- NOTE, this means that if right.key == x aobve, you just merge the two trees
        # without creating a new vertex
        root = self.merge(self.merge(left, new_vertex), right)

    def result(self):
        # pos_list, char_list, size_list = self.in_order()
        char_list = self.in_order()
        self.s = ''.join(char_list)
        return self.s

    def process(self, i, j, k):
        i = i + 1
        j = j + 1
        k = k + 1
        global root
        result = self.find(root, j + 1)
        left, right = self.split(result)
        if i == 1:
            if result == None:
                return
            tmp = self.find(right, k)
            if tmp is not None:
                mid, right = self.split(tmp)
                left = self.merge(mid, left)
                root = self.merge(left, right)
            else:
                root = self.merge(right, left)
        else:
            if result is not None:
                tmp = self.find(left, i)
                if tmp is None:
                    print("gotcha")
                left, mid = self.split(tmp)
                left = self.merge(left, right)
                tmp2 = self.find(left, k)
                if tmp2 is not None:
                    left, right = self.split(tmp2)
                    left = self.merge(left, mid)
                    root = self.merge(left, right)
                else:
                    root = self.merge(left, mid)
            else:
                tmp = self.find(root, i)
                left, right = self.split(tmp)
                tmp2 = self.find(left, k)
                if tmp2 is not None:
                    left, mid = self.split(tmp2)
                    left = self.merge(left, right)
                    root = self.merge(left, mid)
                else:
                    root = self.merge(left, right)


def main():
    # if __name__ == "__main__":
    global root
    root = None
    rope = Rope(sys.stdin.readline().strip())
    q = int(sys.stdin.readline())
    for _ in range(q):
        i, j, k = map(int, sys.stdin.readline().strip().split())
        rope.process(i, j, k)
    print(rope.result())


root = None
threading.Thread(target=main).start()
