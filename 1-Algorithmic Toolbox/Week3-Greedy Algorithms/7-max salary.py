# Use Python3

n = int(input())
digits = list(input().split())

def max_num(lst):
    n = len(lst)
    for i in range(n - 1):
        for i in range(n - 1 - i):
            if lst[i] + lst[i+1] < lst[i + 1] + lst[i]:
                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

digits = max_num(digits)
result = ''
for digit in digits:
    result = result + digit
print(result)

