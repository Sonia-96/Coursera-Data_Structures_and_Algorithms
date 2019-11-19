# Use Python3

i = input()
n, m = map(int, i.split())

F = [0, 1]
remain = [0, 1]

i = 2
last = 0
now = 1
while True:
    F.append(F[i - 1] + F[i - 2])
    r = F[i] % m
    remain.append(r)
    last = now
    now = r
    i = i + 1
    if [last, now] == [0, 1]:
        break

print(remain[n % (i-2)])
