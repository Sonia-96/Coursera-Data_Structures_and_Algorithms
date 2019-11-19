# Use Python3

# d - distance; m - most m miles on a full tank; n - n gas stations
#i - 每个stations和A的距离；stored in list x

d = int(input())
m = int(input())
n = int(input())
i = input()
x = [0] + list(map(int, i.split())) + [d]

def MinRefill(x, m, n):
    current = 0
    count = 0
    while current <= n:
        last = current
        while current <= n and x[current + 1] - x[last] <= m:
            current = current + 1
        if current == last:
            return -1
        if current <= n:
            count = count + 1
    return count


print(MinRefill(x, m, n))
