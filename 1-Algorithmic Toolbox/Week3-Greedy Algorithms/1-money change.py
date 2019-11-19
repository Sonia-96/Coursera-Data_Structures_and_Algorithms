# Use Python3

m = int(input())
changes = [10, 5, 1]
count = 0
for i in range(3):
    n = int(m / changes[i])
    count = count + n
    m = m - n * changes[i]

print(count)
