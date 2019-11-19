# Use Python3

n = int(input())
seg = []
for i in range(n):
    ipt = input()
    seg.append(list(map(int, ipt.split())))
seg.sort()
# seg:[[start1, end1], [start2, end2], ... ]

def min_points(seg):
    n = len(seg)
    current = 0
    ends = []
    while current < n:
        last = current
        while current < n - 1 and seg[current + 1][0] <= seg[last][1]:
            current = current + 1
            if seg[current][1] < seg[last][1]:
                last = current
        ends.append(seg[last][1])
        current = current + 1
    return ends

ends = min_points(seg)
print(len(ends))
for end in ends:
    print(end, end = ' ')
