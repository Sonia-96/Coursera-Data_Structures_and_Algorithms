# Use Python3

n = int(input())
ipt = input()
an = list(map(int, ipt.split()))
ipt = input()
bn = list(map(int, ipt.split()))

an.sort()
bn.sort()
cn = []
for i in range(n):
    cn.append(an[i] * bn[i])

print(sum(cn))
