# Use Python3


def mergeSort(a, n):
    temp_a = [0] * n
    return _mergeSort(a, temp_a, 0, n - 1)


def _mergeSort(a, temp_a, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += _mergeSort(a, temp_a, left, mid)
        inv_count += _mergeSort(a, temp_a, mid + 1, right)
        inv_count += merge(a, temp_a, left, mid, right)
    return inv_count


def merge(a, temp_a, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0
    while i <= mid and j <= right:
        if a[i] <= a[j]:
            temp_a[k] = a[i]
            k += 1
            i += 1
        else:
            inv_count += (mid - i + 1)
            temp_a[k] = a[j]
            k += 1
            j += 1
    while i <= mid:
        temp_a[k] = a[i]
        k += 1
        i += 1
    while j <= right:
        temp_a[k] = a[j]
        k += 1
        j += 1
    for i in range(left, right + 1):
        a[i] = temp_a[i]
    return inv_count


n = int(input())
ipt = input()
A = list(map(int, ipt.split()))
print(mergeSort(A, n))
