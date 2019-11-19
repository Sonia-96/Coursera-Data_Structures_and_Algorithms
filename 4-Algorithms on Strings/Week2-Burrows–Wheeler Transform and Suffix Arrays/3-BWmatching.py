# python3


def Process(s):
    freq = {'$': 0, "A": 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        freq[char] += 1
    ele = ['$', 'A', 'C', 'G', 'T']
    first_occur = {'$': 0}
    for i in range(1, 5):
        first_occur[ele[i]] = first_occur[ele[i-1]] + freq[ele[i-1]]
    count = {}
    for e in ele:
        count[e] = [0] * (len(s) + 1)
    for i in range(len(s)):
        temp = {s[i]: 1}
        for e in ele:
            count[e][i+1] = count[e][i] + temp.get(e, 0)
    return first_occur, count


def BWMatching(s, p, first_occur, count):
    top = 0
    bottom = len(s) - 1
    while top <= bottom:
        if p:
            symbol = p[-1]
            p = p[:-1]
            top = first_occur[symbol] + count[symbol][top]
            bottom = first_occur[symbol] + count[symbol][bottom + 1] - 1
        else:
            return bottom - top + 1
    return 0  # pattern not in string


if __name__ == '__main__':
    bwt = input()
    n_patterns = int(input())
    patterns = list(input().split())
    first_occur, count = Process(bwt)
    for pattern in patterns:
        result = BWMatching(bwt, pattern, first_occur, count)
        print(result, end=' ')
