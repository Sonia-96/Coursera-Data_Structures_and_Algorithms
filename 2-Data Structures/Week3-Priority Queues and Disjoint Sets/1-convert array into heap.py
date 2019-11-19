# python3


class MinHeap:
    def __init__(self, array):
        self.A = array
        self.size = len(self.A)
        self.swaps = []


    def SiftDown(self, i):
        min_index = i
        left = 2 * i + 1  # left child
        right = 2 * i + 2  # right child
        if left < self.size and self.A[left] < self.A[min_index]:
            min_index = left
        if right < self.size and self.A[right] < self.A[min_index]:
            min_index = right
        if min_index != i:
            self.swaps.append((i, min_index))
            self.A[i], self.A[min_index] = self.A[min_index], self.A[i]
            self.SiftDown(min_index)

    def BuildHeap(self):
        n = self.size
        for i in range(n // 2 - 1, -1, -1):
            self.SiftDown(i)


def main():
    n = int(input())
    array = list(map(int, input().split()))
    assert len(array) == n

    heap = MinHeap(array)
    MinHeap.BuildHeap(heap)
    swaps = heap.swaps
    print(len(swaps))
    for swap in swaps:
        print(*swap)


if __name__ == "__main__":
    main()
