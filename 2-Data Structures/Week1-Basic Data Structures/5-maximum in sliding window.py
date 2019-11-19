# python3


from collections import deque


def maxSlidingWindow(sequence, m):
    dq = deque()
    max_nums = []
    length = len(sequence)
    for i in range(length):
        while dq and sequence[i] >= sequence[dq[-1]]:
            dq.pop()
        dq.append(i)
        if i >= m and dq and dq[0] == i - m:
            dq.popleft()
        if i >= m - 1:
            max_nums.append(sequence[dq[0]])
    return max_nums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    print(*maxSlidingWindow(input_sequence, window_size))

