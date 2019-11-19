# python3



def PrefixTrieMatching(text, trie):
    v = 0
    for i in range(len(text)):
        symbol = text[i]
        if trie[v].__contains__(symbol):
            v = trie[v][symbol]
            if not trie.__contains__(v):  # v is a leaf in Trie
                return True
        else:
            return False


def TrieMatching(text, trie):
    positions = []
    n = len(text)
    for k in range(n):
        check = PrefixTrieMatching(text[k:], trie)
        if check:
            positions.append(k)
    return positions


def BuildTrie(patterns):
    tree = {}
    new_node = 0
    for pattern in patterns:
        current_node = 0
        for i in range(len(pattern)):
            current_symbol = pattern[i]
            if tree.__contains__(current_node) and tree[current_node].__contains__(current_symbol):
                current_node = tree[current_node].get(current_symbol)
            else:
                new_node += 1
                if not tree.__contains__(current_node):
                    tree[current_node] = {}
                    tree[current_node][current_symbol] = new_node
                else:
                    tree[current_node][current_symbol] = new_node
                current_node = new_node
    return tree


if __name__ == '__main__':
    text = input()
    n_patterns = int(input())
    patterns = list(input() for _ in range(n_patterns))
    tree = BuildTrie(patterns)
    result = TrieMatching(text, tree)
    for pos in result:
        print(pos, end=' ')
