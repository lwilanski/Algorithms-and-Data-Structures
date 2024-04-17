from zad4testy import runtests
from collections import deque


def bfs(G, s, t):
    visited = [False] * len(G)
    parent = [None] * len(G)
    queue = deque([s])
    visited[s] = True

    while len(queue) > 0:
        tmp = queue.popleft()
        if tmp == t:
            break

        for neighbor in G[tmp]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = tmp
                queue.append(neighbor)

    result = []
    if not visited[t]:
        return None

    current = t
    while current is not None:
        result.append(current)
        current = parent[current]

    result.reverse()
    return result


def longer(G, s, t):
    path = bfs(G, s, t)

    if not path:
        return None

    for i in range(0, len(path) - 1):
        u = path[i]
        v = path[i + 1]

        G[u].remove(v)
        G[v].remove(u)

        new_path = bfs(G, s, t)

        G[u].append(v)
        G[v].append(u)

        if not new_path or len(new_path) > len(path):
            return (u, v)

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
