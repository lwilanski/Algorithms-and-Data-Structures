from collections import deque


# Zwykły bfs tylko, jak wejdzie inną drogą do wierzchołka który jest już visited, to zwraca True.
# Przykładowo BFS dla drzew, zawsze znajdzie tylko jedną ścieżkę do każdego wierzchołka.

def bfs_cycles(G, s):
    visited = [False] * len(G)
    parents = [None] * len(G)
    queue = deque([s])
    visited[s] = True

    while queue:
        vertex = queue.popleft()

        for neighbor in G[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parents[neighbor] = vertex
                queue.append(neighbor)

            elif parents[vertex] != neighbor:
                return True

    return False


G = [[1, 9, 11], [0, 2, 11], [1, 3, 6], [2, 4, 5], [3, 5, 10], [3, 4], [2, 5, 7], [6, 8, 11], [7, 9, 10], [0, 8, 10],
     [4, 8, 9], [0, 1, 7]]

print(bfs_cycles(G, 7))
