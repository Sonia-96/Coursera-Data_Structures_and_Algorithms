# Use Python3

n = int(input())

prize = []
i = 0
while n > 0:
    i = i + 1
    if n - i <= i:
        i = n
    prize.append(i)
    n = n - i

print(len(prize))
for x in prize:
    print(x, end =' ')



