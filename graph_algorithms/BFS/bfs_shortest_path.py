from collections import deque


# W BFS-ie każde pierwsze odwiedzenie jakiegokolwiek wierzchołka, jest jednocześnie najkrótszą ścieżką
# od wierzchołka startowego.

def bfs_shortest_path(G, s, t):
    visited = [False] * len(G)
    visited[s] = True
    queue = deque([(s, [s])])

    while queue:
        vertex, path = queue.popleft()

        for neighbor in G[vertex]:
            if neighbor == t:
                return path + [neighbor]
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, path + [neighbor]))

    return None
