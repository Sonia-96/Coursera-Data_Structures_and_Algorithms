# python3


def LastToFirst(s):
    counts = {'$': 0, "A": 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        counts[char] += 1
    temp = -1
    position = {}
    for t in ['$', 'A', 'C', 'G', 'T']:
        temp += counts[t]
        position[t] = temp
    array = [0] * len(s)
    for i in range(len(s)-1, -1, -1):
        array[i] = position[s[i]]
        position[s[i]] -= 1
    return array


def invertBWT(s):
    last_to_first = LastToFirst(s)
    result = '$'
    pos = 0
    for i in range(len(s) - 1):
        result += s[pos]
        pos = last_to_first[pos]
    result = result[::-1]
    return result


if __name__ == '__main__':
    bwt = input()
    print(invertBWT(bwt))
