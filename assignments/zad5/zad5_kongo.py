from zad5testy import runtests
from collections import deque


def convert(n, E, S):
    G = [[] for _ in range(n)]

    for v1, v2, weight in E:
        G[v1].append((v2, weight))
        G[v2].append((v1, weight))

    for i in range(0, len(S)):
        for j in range(i + 1, len(S)):
            G[S[i]].append((S[j], 0))
            G[S[j]].append((S[i], 0))

    return G


def bfs_shortest_path(G, s, t):
    visited = [False] * len(G)
    queue = deque([((s, 0), 0)])

    while queue:
        vertex, l = queue.popleft()

        if vertex[1] == 0:
            visited[vertex[0]] = True
            if vertex[0] == t:
                return l
            for neighbor in G[vertex[0]]:
                if not visited[neighbor[0]]:
                    queue.append((neighbor, l))
        else:
            queue.append(((vertex[0], vertex[1] - 1), l + 1))

    return None


def spacetravel(n, E, S, a, b):
    G = convert(n, E, S)

    return bfs_shortest_path(G, a, b)


runtests(spacetravel, all_tests=False)

# E = [(0, 1, 5), (1, 2, 21), (1, 3, 1), (2, 4, 7), (3, 4, 13), (3, 5, 16), (4, 6, 4), (5, 6, 1)]
# S = [0, 2, 3]
# n = 7
# print(convert(n, E, S))
