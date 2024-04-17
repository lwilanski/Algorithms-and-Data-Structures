import heapq
from kol2testy import runtests
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
        return True

def beautree(G):
    n = len(G)
    edges = [(u, v, w) for u in range(n) for v, w in G[u]]
    edges.sort(key=lambda x: x[2])
    m = len(edges)
    for i in range(m):
        uf = UnionFind(n)
        tree_edges = 0
        tree_weight = 0
        for j in range(i, m):
            u, v, w = edges[j]
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                tree_edges += 1
                tree_weight += w
            if tree_edges == n - 1:
                break
        if tree_edges == n - 1 and all(uf.find(u) == uf.find(v) for u in range(n) for v in G[u]):
            return tree_weight
    return None



runtests(beautree, all_tests=True)
