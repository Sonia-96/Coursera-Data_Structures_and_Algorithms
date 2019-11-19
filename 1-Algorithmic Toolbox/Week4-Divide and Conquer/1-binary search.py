# Use Python3

def BinarySearch(A, low, high, key):
    if high < low:
        return -1
    mid = (high + low) // 2
    if key == A[mid]:
        return mid
    if key < A[mid]:
        return BinarySearch(A, low, mid - 1, key)
    if key > A[mid]:
        return BinarySearch(A, mid + 1, high, key)


array = input()
n = int(array.split()[0])
an = list(map(int, array.split()[1:]))
keys = input()
k = int(keys.split()[0])
bn = list(map(int, keys.split()[1:]))7


for b in bn:
    index = BinarySearch(an, 0, n - 1, b)
    print(index, end = ' ')

