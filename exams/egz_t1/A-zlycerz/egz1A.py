import heapq

from egz1Atesty import runtests


# Łukasz Wilański
# Rozwiązanie polega na sprawdza dla każdego zamku, co by było jakbyśmy go obrabowali.
# Czyli szukamy najkrótszych ścieżek z s do pozostałch wierzchołków po zwykłych wagach i dostajemy tablicę normal_times
# Następnie szukamy najkrótszych ścieżek z t do pozostałych wierzchołków i dostajemy tablicę taxed_times
# Teraz musimy przejść po obu tablicach naraz i znaleźć najlepszą ścieżkę z s do i, oraz z i do t.
# Wykonujemy 2 razy Dijkstre i przechodzimy raz przez tablicę długości |V|, więc
# Złożoność tego algorytmu to O(V((V+E)*logV))

def gold(G, V, s, t, r):
    result = float('inf')
    normal_times = dijkstra_before(G, s)
    taxed_times = dijkstra_after(G, t, r)
    n = len(normal_times)
    for i in range(0, n):
        if normal_times[i] is None or taxed_times[i] is None:
            continue

        elif normal_times[i] + taxed_times[i] - V[i] < result:
            result = normal_times[i] + taxed_times[i] - V[i]

    return result


def dijkstra_before(G, s):
    visited = [False] * len(G)
    times = [float('inf')] * len(G)
    times[s] = 0
    queue = [(0, s)]

    while queue:
        vertex = heapq.heappop(queue)[1]

        if visited[vertex]:
            continue

        visited[vertex] = True

        for neighbor, weight in G[vertex]:
            if not visited[neighbor]:
                if times[neighbor] > times[vertex] + weight:
                    times[neighbor] = times[vertex] + weight

                heapq.heappush(queue, (times[neighbor], neighbor))

    return times


def dijkstra_after(G, s, r):
    visited = [False] * len(G)
    times = [float('inf')] * len(G)
    times[s] = 0
    queue = [(0, s)]

    while queue:
        vertex = heapq.heappop(queue)[1]

        if visited[vertex]:
            continue

        visited[vertex] = True

        for neighbor, weight in G[vertex]:
            if not visited[neighbor]:
                if times[neighbor] > times[vertex] + (2 * weight) + r:
                    times[neighbor] = times[vertex] + (2 * weight) + r

                heapq.heappush(queue, (times[neighbor], neighbor))

    return times


G = [[(1, 9), (2, 2)],
     [(0, 9), (3, 2), (4, 6)],
     [(0, 2), (3, 7), (5, 1)],
     [(1, 2), (2, 7), (4, 2), (5, 3)],
     [(1, 6), (3, 2), (6, 1)],
     [(2, 1), (3, 3), (6, 8)],
     [(4, 1), (5, 8)]]

V = [25, 30, 20, 15, 5, 10, 0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(gold, all_tests=True)
# print(gold(G, V, 0, 6, 7))

# print(gold(G, V, 0, 6, 7))
