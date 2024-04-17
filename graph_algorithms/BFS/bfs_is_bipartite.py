from collections import deque


# Każdy graf dwudzielny można pokolorować tak żeby każde dwa wierzchołki połączone krawędzią miały inny kolor.
# Zaczyna od jakiegoś wierzchołka i naprzemiennie koloruje wierzchołki do których trafia kolorem 0 albo 1.
# Jeżeli dojdzie do sprzeczności do graf nie jest dwudzielny

def bfs_is_bipartite(G, s):
    colors = [None] * len(G)
    visited = [False] * len(G)
    queue = deque([s])
    colors[s] = False

    while queue:
        vertex = queue.popleft()
        visited[vertex] = True
        for neighbor in G[vertex]:
            if not visited[neighbor]:
                if colors[neighbor] is None or colors[neighbor] is not colors[vertex]:
                    colors[neighbor] = not colors[vertex]
                else:
                    return False
                queue.append(neighbor)

    return colors


# G = [[1, 3], [0, 2], [1, 3], [0, 2]]
# G = [[1, 2, 5], [0, 2], [1, 0, 3], [2, 4, 5], [3, 5], [0, 3, 4]]
# G = [[2], [2, 4], [0, 1, 3, 4], [2, 5], [1, 2], [3]]
# G = [[1, 4, 8], [0, 2, 3], [1, 5, 8], [1, 7], [0, 6, 8], [2, 6], [4, 5, 7], [3, 6], [0, 2, 4]]
# G = [[4, 1], [0, 2], [1, 3, 5, 4], [2, 4], [2, 3, 5, 0], [2, 4]]
# G = [[1, 4], [0, 2], [1, 3, 4, 5], [2, 4], [0, 2, 3, 5], [2, 4]]
G = [[1, 3], [0, 2], [1, 3], [0, 2, 4], [3, 5, 7], [4, 6], [5, 7], [4, 6]]

print(bfs_is_bipartite(G, 0))
