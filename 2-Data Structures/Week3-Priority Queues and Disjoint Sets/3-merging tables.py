# python3


class DataBases:
    def __init__(self, row_counts):
        self.max_row_count = max(row_counts)
        self.row_counts = row_counts
        n_tables = len(row_counts)
        self.parent = list(range(n_tables))
        self.rank = [0] * n_tables

    def FindParent(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.FindParent(self.parent[i])
        return self.parent[i]

    def MergeTables(self, dst, src):
        src_parent = self.FindParent(src)
        dst_parent = self.FindParent(dst)
        if src_parent == dst_parent:
            return
        if self.rank[src_parent] > self.rank[dst_parent]:
            self.parent[dst_parent] = src_parent
            self.row_counts[src_parent] += self.row_counts[dst_parent]
            self.row_counts[dst_parent] = 0
            self.max_row_count = max(self.max_row_count, self.row_counts[src_parent])
        else:
            self.parent[src_parent] = dst_parent
            self.row_counts[dst_parent] += self.row_counts[src_parent]
            self.row_counts[src_parent] = 0
            self.max_row_count = max(self.max_row_count, self.row_counts[dst_parent])
            if self.rank[src_parent] == self.rank[dst_parent]:
                self.rank[dst_parent] += 1


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert(n_tables == len(counts))
    db = DataBases(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.MergeTables(dst - 1, src - 1)
        print('parent: ', db.parent)
        print('row counts: ', db.row_counts)
        print(db.max_row_count)



if __name__ == "__main__":
    main()
