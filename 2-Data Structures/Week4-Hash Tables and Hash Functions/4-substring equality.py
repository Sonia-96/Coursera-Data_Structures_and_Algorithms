# python3


def HashTable(s, prime, x):
    hash_table = list([] for _ in range(len(s) + 1))
    hash_table[0] = 0
    for i in range(1, len(s) + 1):
        hash_table[i] = (hash_table[i - 1] * x + ord(s[i - 1])) % prime
    return hash_table


def HashValue(hash_table, prime, x, start, length):
    y = pow(x, length, prime)
    hash_value = (hash_table[start + length] - y * hash_table[start]) % prime
    return hash_value


def AreEqual(table1, table2, prime1, prime2, x, a, b, l):
    a_hash1 = HashValue(table1, prime1, x, a, l)
    a_hash2 = HashValue(table2, prime2, x, a, l)
    b_hash1 = HashValue(table1, prime1, x, b, l)
    b_hash2 = HashValue(table2, prime2, x, b, l)
    if a_hash1 == b_hash1 and a_hash2 == b_hash2:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    string = input()
    n_queries = int(input())
    m = 1000000007
    m2 = 1000000009
    x = 263
    hash_table1 = HashTable(string, m, x)
    hash_table2 = HashTable(string, m2, x)
    print(hash_table1, hash_table2)
    for i in range(n_queries):
        a, b, l = map(int, input().split())
        print(AreEqual(hash_table1, hash_table2, m, m2, x, a, b, l))
