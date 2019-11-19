# Use Python3

n = int(input())
F = [0, 1]
last = [0, 1]
for i in range(2, 60):
    F.append(F[i - 1] + F[i - 2])
    last.append(int(str(F[i])[-1]))

print(last[n % 60])


