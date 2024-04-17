
# Algorytm Kruskala służy do znajdywania najlżejszego drzewa rozpinającego w grafie.

# Algorytm wykonuje następujące kroki:

# Sortuje krawędzie po wagach

# Wrzuca po kolei krawędzie do msp, i sprawdza czy nie tworzą cyklu korzystając ze struktury UnionFind.

# Jak wrzuci już n - 1 krawędzi to wiemy że na pewno mamy drzewo i możemy przerwać.

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1

        return True


def kruskal(G, n):
    msp = []
    vertices = UnionFind(n)
    G.sort(key=lambda x: x[2])

    for edge in G:
        if vertices.union(edge[0], edge[1]):
            msp.append((edge[0], edge[1]))

    return msp


def main():
    G = [(0, 1, 1), (1, 2, 3), (2, 3, 6), (3, 4, 2), (4, 5, 7), (0, 5, 8), (0, 4, 5), (2, 4, 4)]
    print(kruskal(G, 6))


if __name__ == "__main__":
    main()
