# python3


def BWT(s):
    matrix = [s]
    for i in range(1, len(s)):
        s = s[-1] + s[:-1]
        matrix.append(s)
    matrix.sort()
    bwt = ''
    for t in matrix:
        bwt += t[-1]
    return bwt


if __name__ == '__main__':
    text = input()
    print(BWT(text))
