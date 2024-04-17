# Łukasz Wilański
from kol2testy import runtests


#Żeby drzewo spełniało warunki zadania, należy posortować krawędzie wg wag a następnie zbudować drzewo z krawędzi które
# tworzą spójny podciąg. Znajduje wszystkie takie drzewa a następnie wybieram to z najmniejszą sumą wag.
# Złożoność O(VE log E)

def convert(G):
    result = []
    for v in range(0, len(G)):
        for tup in G[v]:
            if v < tup[0]:
                result.append((v, tup[0], tup[1]))

    return result


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


def beautree(G):
    n = len(G)
    edge_list = convert(G)
    result = [float('inf')]
    vertices = UnionFind(n)
    edge_list.sort(key=lambda x: x[2])

    for i in range(0, len(edge_list)):
        curr_weight = 0
        possible = True
        for j in range(i, len(edge_list)):
            if not vertices.union(edge_list[j][0], edge_list[j][1]):
                possible = False
                break
            else:
                curr_weight += edge_list[j][2]

        if possible and result < curr_weight:
            result = curr_weight

        vertices = UnionFind(n)

    if result != [float('inf')]:
        return result
    else:
        return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(beautree, all_tests=True)

G = [[(1, 3), (2, 1), (4, 2)],
     [(0, 3), (2, 5)],
     [(1, 5), (0, 1), (3, 6)],
     [(2, 6), (4, 4)],
     [(3, 4), (0, 2)]]

# print(beautree(G))
