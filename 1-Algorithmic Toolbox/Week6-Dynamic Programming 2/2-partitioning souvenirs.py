# Use Python3


def maxWeight(capacity, items):
    n = len(items)
    T = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            T[i][w] = T[i - 1][w]
            if w >= items[i - 1]:
                weight = T[i - 1][w - items[i - 1]] + items[i - 1]
                if weight > T[i][w]:
                    T[i][w] = weight
    return T


def optimalSolution(T, capacity, items):
    n = len(items)
    i = n
    w = capacity
    used_items = []
    while i > 0 and w > 0:
        if T[i][w] == T[i - 1][w]:
            i = i - 1
        else:
            used_items.append(i - 1)
            w = w - items[i - 1]
            i = i - 1
    return used_items


def partitionK(capacity, items,k):
    if capacity % k != 0:
        return 0
    else:
        capacity = capacity // k
    for bag in range(k - 1):
        T = maxWeight(capacity, items)
        print('weight = ', T[len(items)][capacity])
        if T[len(items)][capacity] != capacity:
            return 0
        else:
            used_items = optimalSolution(T, capacity, items)
            for index in used_items:
                items.pop(index)
        print('items = ', items)
    return 1


n = int(input())
ipt = input()
nums = list(map(int, ipt.split()))
total = sum(nums)
print(partitionK(total, nums, 3))
