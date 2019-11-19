# use Python3

ipt = input()
n_seg, n_point = map(int, ipt.split())
segs = []
for i in range(n_seg):
    ipt = input()
    segs.append(list(map(int, ipt.split())))
ipt = input()
points_origin = list(map(int, ipt.split()))
segs.sort()
points = sorted(points_origin)


def covered_segs(points, segs):
    p = len(points)
    s = len(segs)
    counts = {}
    j = 0
    for i in range(p):
        count = 0
        if i > 0 and counts[points[i - 1]] != 0:
            for j in range(j, j + counts[points[i - 1]]):
                if segs[j][0] <= points[i] <= segs[j][1]:
                    count += 1
            j += 1
        while j < s and segs[j][0] <= points[i] <= segs[j][1]:
            j += 1
            count += 1
        counts[points[i]] = count
        j = j - count
    return counts


counts = covered_segs(points, segs)
for point in points_origin:
    print(counts[point], end=' ')
