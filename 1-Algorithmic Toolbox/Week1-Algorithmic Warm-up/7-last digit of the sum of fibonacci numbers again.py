# Use Python3

# last digit of the fibonacci numbers, 0 ~ 59 a cycle
F = [0, 1]
last = [0, 1]
for i in range(2, 60):
    F.append(F[i - 1] + F[i - 2])
    last.append(int(str(F[i])[-1]))

a = input()
m, n = map(int, a.split())
q = int( (n - m + 1) / 60 )

total = 0
for i in range((m + q * 60), (n + 1)):
    total = total + last[i % 60]

print(total % 10)
