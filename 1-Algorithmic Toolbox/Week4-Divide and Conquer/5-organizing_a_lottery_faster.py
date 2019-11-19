# Use Python3
import sys

input = sys.stdin.read()
data = list(map(int, input.split()))
s = data[0]
k = data[1]
starts = data[2:2 * s + 2:2]
ends = data[3:2 * s + 2:2]
points = data[2 * s + 2:]

lst = []
for point in points:
    lst.append((point, 'p'))
for start in starts:
    lst.append((start, 'l'))
for end in ends:
    lst.append((end, 'r'))
lst.sort()

counts = []
left = 0
right = 0
for pair in lst:
    if pair[1] == 'p':
        counts.append(pair)
        continue
    if pair[1] == 'l':
        left += 1
    if pair[1] == 'r':
        right += 1
    counts.append((left, right))

dic = {}
l = 0
r = 0
for pair in counts:
    if pair[1] == 'p':
        segs = l + right - r - s
        dic[pair[0]] = segs
    else:
        l = pair[0]
        r = pair[1]

for point in points:
    print(dic[point], end=' ')
