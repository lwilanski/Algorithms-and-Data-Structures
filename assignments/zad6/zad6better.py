# Łukasz Wilański
from zad6testy import runtests


# Algorytm szuka jak liczne jest najliczniejsze skojarzenie w grafie dwudzielnym, na zasadzie znajdywania ścieżek powiększających
# (augmenting paths) korzystając z DFS-a. Funkcja binworker wywołuje dla każdego wierzchołka dfs żeby zbudować największe skojarzenie
# i na końcu zwraca jego liczność.

def dfs(G, vertex, match, visited):
    visited[vertex] = True
    print("Current vertex within DFS:", vertex)
    print("Matchings:", match)
    print("Visited:", visited)

    for neighbor in G[vertex]:
        print("Current neighbor:", neighbor, "and it's match", match[neighbor], "\n")
        if match[neighbor] == -1 or (not visited[match[neighbor]] and dfs(G, match[neighbor], match, visited)):
            match[neighbor] = vertex
            return True
    return False


def binworker(M):
    n = len(M)
    match = [-1] * n
    for v in range(n):
        print("Binworker vertex", v, "START", "\n")
        dfs(M, v, match, [False] * n)
        print("Matchings after vertex", v, ":", match)
        print("Binworker vertex", v, "END", "\n")

    return n - match.count(-1)


# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests(binworker, all_tests=True)

# G = [[0, 1, 3], [2, 4], [0, 2], [3], [2, 3]]
# print("BINWORKER RESULT", binworker(G))

G = [ [0, 1], [0, 3], [1, 2], [2, 3] ]

match = [1, 0, 2, -1]

dfs(G, 2, match, [False] * len(G))
print(match)
dfs(G, 3, match, [False] * len(G))
print(match)
