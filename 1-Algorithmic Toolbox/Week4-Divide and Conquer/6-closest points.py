# Use Python3
import math

n = int(input())
points = []
for i in range(n):
    ipt = input()
    coordinate = tuple(map(int, ipt.split()))
    points.append(coordinate)
points_x_sorted = sorted(points)


def getDistance(point1, point2):
    d = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    return d


def bruteForce(points):
    n = len(points)
    d = getDistance(points[0], points[1])
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = min(d, getDistance(points[i], points[j]))
    return d


def stripMin(points_x_sorted, min_d):
    len_p = len(points_x_sorted)
    mid = len_p //2 # 分割线的位置
    mid_value = points_x_sorted[mid][0] # 分割线的x坐标
    points_y_sorted = []
    for point in points_x_sorted:
        if abs(point[0] - mid_value) < min_d:
            points_y_sorted.append(point)
    points_y_sorted.sort(key=lambda p:p[1])
    len_strip = len(points_y_sorted)
    if len_strip < 2:
        return min_d
    else:
        min_d2 = getDistance(points_y_sorted[0], points_y_sorted[1])
        for i in range(len_strip - 1):
            for j in range(i + 1, min(i + 7, len_strip)): # 用min可以包含数列长度<6的情况
                min_d2 = min(min_d2, getDistance(points_y_sorted[i], points_y_sorted[j]))
        return min_d2


def minDistance(points_x_sorted):
    len_p = len(points_x_sorted)
    if len_p <= 3:
        return bruteForce(points_x_sorted)
    else:
        mid = len_p // 2
        min_d_l = minDistance(points_x_sorted[:mid])
        min_d_r = minDistance(points_x_sorted[mid:])
        min_d = min(min_d_l, min_d_r)
        min_d2 = stripMin(points_x_sorted, min_d)
        result = min(min_d, min_d2)
    return result


result = minDistance(points_x_sorted)
print("{0:.9f}".format(result))

