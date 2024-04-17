from zad5testy import runtests
import heapq


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


def dijkstra_shortest_path(G, s, t):
    visited = [False] * len(G)
    times = [None] * len(G)
    times[s] = 0
    queue = [(0, s)]

    while queue:
        distance, vertex = heapq.heappop(queue)

        if visited[vertex]:
            continue

        if vertex == t:
            return times[t]

        visited[vertex] = True

        for neighbor, weight in G[vertex]:
            if not visited[neighbor] and (times[neighbor] is None or times[neighbor] > distance + weight):
                times[neighbor] = distance + weight

            heapq.heappush(queue, (times[neighbor], neighbor))


def spacetravel(n, E, S, a, b):
    G = convert(n, E, S)

    return dijkstra_shortest_path(G, a, b)


runtests(spacetravel, all_tests=True)

# E = [(0, 1, 5), (1, 2, 21), (1, 3, 1), (2, 4, 7), (3, 4, 13), (3, 5, 16), (4, 6, 4), (5, 6, 1)]
# S = [0, 2, 3]
# n = 7
# print(convert(n, E, S))
