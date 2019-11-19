# Use Python3

n = int(input())
F = [0, 1]
for i in range(2, n + 1):
    F.append(F[i - 1] + F[i - 2])
print(F[n])

