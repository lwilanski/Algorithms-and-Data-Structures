from zad9testy import runtests
import heapq


def merge(O, C, L):
    new_list = []
    new_list.append((0, 0, 0))
    for i in range(0, len(O)):
        new_list.append((O[i], C[i], i + 1))
    new_list.append((L, 0, len(new_list) + 1))
    new_list.sort()
    return new_list

def build_graph(O, C, T, mega_vertex):
    G = []
    n = len(O)
    for v in range(0, n):
        neighbors = []
        if v == mega_vertex:
            for i in range(0, n):
                if O[v] < O[i] <= O[v] + 2 * T:
                    neighbors.append((i, C[i]))

        else:
            for i in range(0, n):
                if O[v] < O[i] <= O[v] + T:
                    neighbors.append((i, C[i]))

        G.append(neighbors)

    return G


def dijkstra_shortest_path(G, s, t):
    visited = [False] * len(G)
    distances = [float('inf')] * len(G)
    distances[s] = 0
    queue = [(0, s)]

    while queue:
        _, vertex = heapq.heappop(queue)

        if vertex == t:
            break

        if visited[vertex]:
            continue

        visited[vertex] = True

        for neighbor, weight in G[vertex]:
            new_distance = distances[vertex] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))

    return distances[t]


def min_cost(O, C, T, L):
    O.insert(0, 0)
    O.append(L)
    C.insert(0, 0)
    C.append(0)
    x = len(O) - 1
    current_min = float('inf')

    for ver in range(0, x):
        graph = build_graph(O, C, T, ver)
        res = dijkstra_shortest_path(graph, 0, x)
        if res < current_min:
            current_min = res

    return current_min


o = [17, 20, 11, 5, 12]
c = [9, 7, 7, 7, 3]
t = 7
l = 25

# print(build_graph(o, c, t, l))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(min_cost, all_tests=True)
