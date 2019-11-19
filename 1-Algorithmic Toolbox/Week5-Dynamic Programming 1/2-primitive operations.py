#Use Python3

def minOperations(n):
    min_operations = [float("inf")]*(n + 1)
    min_operations[0: 2] = 0, 0
    prev = [0] * (n+1)
    for i in range(2, n + 1):
        if i % 3 != 0:
            temp_3 = float("inf")
        else:
            temp_3 = min_operations[int(i / 3)]
        if i % 2 != 0:
            temp_2 = float("inf")
        else:
            temp_2 = min_operations[int(i / 2)]
        min_operations[i] = min(min_operations[i - 1], temp_2, temp_3) + 1
        if min_operations[i] == temp_3 + 1:
            prev [i] = int(i / 3)
            continue
        if min_operations[i] == temp_2 + 1:
            prev[i] = int(i / 2)
            continue
        if min_operations[i] == min_operations[i - 1] + 1:
            prev[i] = i - 1
    return min_operations, prev


n = int(input())
min_operations, prev = minOperations(n)
result = min_operations[n]
print(result)

sequence = [n]
i = n
while i > 1:
    prev_number = prev[i]
    sequence.append(prev_number)
    i = prev_number
sequence.sort()
for number in sequence:
    print(number, end = ' ')


