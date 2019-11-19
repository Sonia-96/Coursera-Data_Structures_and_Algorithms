# Use Python3

n = input()
a, b = map(int, n.split())

def GCD(a, b):
    if b == 0:
        return a
    else:
         r = a % b
         return GCD(b, r)

def LCM(a, b):
    return int(a * b / GCD(a, b))

print(LCM(a, b))
