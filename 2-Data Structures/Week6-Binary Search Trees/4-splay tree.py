# python 3


class Vertex:
    def __init__(self, key, sum, left, right, parent):
        (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)


def update(v):
    if v is None:
        return
    v.sum = v.key + (v.left.sum if v.left is not None else 0) + (v.right.sum if v.right is not None else 0)
    if v.left is not None:
        v.left.parent = v
    if v.right is not None:
        v.right.parent = v


def smallRotation(v):
    parent = v.parent
    if parent is None:
        return
    grandparent = v.parent.parent
    # rotate right
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    # rotate left
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent is not None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v


def bigRotation(v):
    # zig-zig right: RotateRight 2 times
    if v.parent.left == v and v.parent.parent.left == v.parent:
        smallRotation(v.parent)
        smallRotation(v)
    # zig-zig left: RotateLeft 2 times
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        smallRotation(v.parent)
        smallRotation(v)
    # zig-zag: RotateRight
    else:
        smallRotation(v)
        smallRotation(v)
    # 把zig和单独放在small rotation里是因为zig的情况没有grandparent，如果直接使用big rotation会报错。


# Makes splay of the given vertex and makes it the new root.
def splay(v):
    if v is None:
        return None
    while v.parent is not None:
        if v.parent.parent == None:
            smallRotation(v)
            break
        bigRotation(v)
    return v # 最后v.parent = None


# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key): # key是一个int，不是node
    v = root
    last = root
    next = None
    while v is not None:
        if v.key >= key and (next is None or v.key < next.key):
            next = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    if next is not None:
        root = splay(next)
    return (next, root)


def split(root, key):
    (result, root) = find(root, key)
    # 根据find()，可知result一定>=key，所以我们把result放到右边的子树上，即CutLeft()
    if result is None:
        return (root, None)
    right = splay(result)
    left = right.left
    right.left = None
    if left is not None:
        left.parent = None
    update(left)  # important!!
    update(right)  # important!!
    return (left, right)


def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    # find the smallest node in the right tree, splay the node,
    # (Method 2：node = find(right, -inf), splay(node))
    # then merge left tree and right tree
    while right.left is not None:
        right = right.left
    right = splay(right)
    right.left = left
    left.parent = right # starter file里忘掉了
    update(right)  # important!!
    return right


root = None


def insert(x):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right is None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)
    root = merge(merge(left, new_vertex), right)


def erase(x):
    global root
    (left, middle) = split(root, x)
    (middle, right) = split(middle, x + 1)
    root = merge(left, right)


def search(x):
    global root
    (result, root) = find(root, x)
    if result is None or result.key != x:
        return False
    else:
        return True


def sum(fr, to):
    global root
    (left, middle) = split(root, fr)
    (middle, right) = split(middle, to + 1)
    ans = 0
    if middle is not None:
        ans += middle.sum
    root = merge(merge(left, middle), right)
    return ans


MODULO = 1000000001
n_operations = int(input())
last_sum_result = 0
for _ in range(n_operations):
    line = list(input().split())
    if line[0] == '+':
        x = int(line[1])
        insert((x + last_sum_result) % MODULO)
    elif line[0] == '-':
        x = int(line[1])
        erase((x + last_sum_result) % MODULO)
    elif line[0] == '?':
        x = int(line[1])
        if search((x + last_sum_result) % MODULO):
            print('Found')
        else:
            print('Not found')
    elif line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
        print(res)
        last_sum_result = res % MODULO
