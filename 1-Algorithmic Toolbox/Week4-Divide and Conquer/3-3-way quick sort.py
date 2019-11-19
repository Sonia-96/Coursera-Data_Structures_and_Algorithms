# Use Python 3

def QuickSort3(A, l, r):
    if r <= l:
        return
    j, i = Partition3(A, l, r)
    QuickSort3(A, l, j)
    QuickSort3(A, i, r)


def Partition3(A, l, r):
    x = A[r]
    i = l - 1
    p = l - 1
    j = r
    q = r

    while True:
        while A[i + 1] < x:
            i = i + 1
        i = i + 1
        while A[j - 1] > x:
            j = j - 1
        j = j - 1
        if i >= j:
            break
        A[i], A[j] = A[j], A[i]
        if A[i] == x:
            p = p + 1
            A[i], A[p] = A[p] , A[i]
        if A[j] == x:
            q = q - 1
            A[j], A[q] = A[q], A[j]

    A[i], A[r] = A[r], A[i]

    j = i - 1
    k = l
    while k <= p:
        A[k], A[j] = A[j], A[k]
        j = j - 1
        k = k + 1

    i = i + 1
    k = r - 1
    while k >= q:
        A[k], A[i] = A[i], A[k]
        i = i + 1
        k = k - 1

    return j, i


n = int(input())
ipt = input()
a = list(map(int, ipt.split()))
QuickSort3(a, 0, n - 1)
for e in a:
    print(e, end = ' ')
