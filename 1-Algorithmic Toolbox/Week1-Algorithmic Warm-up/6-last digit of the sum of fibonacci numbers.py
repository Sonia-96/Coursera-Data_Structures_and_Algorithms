# Use Python3

# last digit of the fibonacci numbers, 0 ~ 59 a cycle
F = [0, 1]
last = [0, 1]
for i in range(2, 60):
    F.append(F[i - 1] + F[i - 2])
    last.append(int(str(F[i])[-1]))

# Sn = 2 * F[n] + F[n-1] - 1
n = int(input())
result = 2 * last[n % 60] + last[(n - 1) % 60] - 1
print(result % 10)
