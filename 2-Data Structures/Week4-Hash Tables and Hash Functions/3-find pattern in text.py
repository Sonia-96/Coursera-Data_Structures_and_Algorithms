# python3


def PolyHash(string, prime, multiplier):
    hash_value = 0
    for i in range(len(string) - 1, -1, -1):
        hash_value = (hash_value * multiplier + ord(string[i])) % prime
    return hash_value


def PrecomputedHashes(text, pattern, prime, multiplier):
    t = len(text)
    p = len(pattern)
    s = text[t - p:]
    H = list([] for _ in range(t - p + 1))
    H[t - p] = PolyHash(s, prime, multiplier)
    y = 1
    for i in range(1, p + 1):
        y = (y * multiplier) % prime
    for i in range(t - p - 1, -1, -1):
        H[i] = (multiplier * H[i + 1] + ord(text[i]) - y * ord(text[i + p])) % prime
    return H


def RabinKarp(text, pattern):
    t = len(text)
    p = len(pattern)
    prime = 1000000007
    multiplier = 236
    result = []
    pattern_hash = PolyHash(pattern, prime, multiplier)
    hash_substrings = PrecomputedHashes(text, pattern, prime, multiplier)
    for i in range(t - p + 1):
        if pattern_hash == hash_substrings[i]:
            result.append(i)
    return result


if __name__ == '__main__':
    pattern = input()
    text = input()
    positions = RabinKarp(text, pattern)
    for pos in positions:
        print(pos, end=' ')
