# python3


def PrefixFunction(p):
    s = [0] * len(p)
    border = 0
    for i in range(1, len(p)):
        while border > 0 and p[i] != p[border]:
            border = s[border - 1]
        if p[i] == p[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return s


def KMP(p, t):
    s = p + '$' + t
    pre_func = PrefixFunction(s)
    result = []
    for i in range(len(p) + 1, len(s)):
        if pre_func[i] == len(p):
            result.append(i - 2 * len(p))
    return result


if __name__ == '__main__':
    pattern = input()
    text = input()
    positions = KMP(pattern, text)
    for pos in positions:
        print(pos, end=' ')
