# python3

from collections import deque


class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == "check":
            self.index = int(query[1])
        else:
            self.word = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.hash_table = list(deque() for _ in range(self.bucket_count))

    def HashFunction(self, word):
        hash_value = 0
        for char in reversed(word):
            hash_value = (hash_value * self._multiplier + ord(char)) % self._prime
        return hash_value % self.bucket_count

    def ProcessQuery(self, query):
        if query.type == 'check':
            if self.hash_table[query.index]:
                print(' '.join(self.hash_table[query.index]))
            else:
                print()
        else:
            hash_value = self.HashFunction(query.word)
            if query.type == "add":
                if query.word not in self.hash_table[hash_value]:
                    self.hash_table[hash_value].appendleft(query.word)
            elif query.type == "del":
                if query.word in self.hash_table[hash_value]:
                    self.hash_table[hash_value].remove(query.word)
            elif query.type == "find":
                if query.word in self.hash_table[hash_value]:
                    print('yes')
                else:
                    print('no')


if __name__ == '__main__':
    n_buckets = int(input())
    hash_table = QueryProcessor(n_buckets)
    n_queries = int(input())
    for _ in range(n_queries):
        command = Query(input().split())
        hash_table.ProcessQuery(command)







