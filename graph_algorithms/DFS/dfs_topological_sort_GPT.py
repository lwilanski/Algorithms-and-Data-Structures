
# Sortowanie topologiczne wykonujemy tylko dla skierowanych grafów acyklicznych i
# polega ono na ustawieniu wierzchołków tak że krawędzie idą tylko z lewej na prawo.
# Można tego użyć np do ustalenia kolejności wykonywania jakiś działań.

# Algorytm sam w sobie polega na odpaleniu dfs-a i dodawaniu wierzchołków do wyniku podczas back-trackingu.

def dfs(G, vertex, visited, result):
    visited[vertex] = True

    for neighbor in G[vertex]:
        if not visited[neighbor]:
            dfs(G, neighbor, visited, result)

    result.append(vertex)


def topological_sort(G):
    visited = [False] * len(G)
    result = []

    for vertex in range(len(G)):
        if not visited[vertex]:
            dfs(G, vertex, visited, result)

    return result[::-1]
