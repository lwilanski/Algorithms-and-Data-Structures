# Łukasz Wilański
from zad5testy import runtests
# Program dzieli się na 3 funkcje: build_adjacency_list, find_shortest_time, spacetravel.
# Pierwsza tworzy listę sąsiedztwa, dodając połączenia o czasie zerowym między planetami w pobliżu osobliwości.
# Druga implementuje algorytm Dijkstry w celu znalezienia najkrótszego czasu podróży.
# Trzecia i docelowa funkcja "spacetravel" korzysta z poprzednich funkcji i zwraca odpowiedni wynik.
import heapq


def build_adjacency_list(n, edges, singularities):
    adjacency_list = [list() for _ in range(n)]

    for u, v, t in edges:
        adjacency_list[u].append((v, t))
        adjacency_list[v].append((u, t))

    for i in range(len(singularities)):
        for j in range(i + 1, len(singularities)):
            adjacency_list[singularities[i]].append((singularities[j], 0))
            adjacency_list[singularities[j]].append((singularities[i], 0))

    return adjacency_list


def find_shortest_time(n, adjacency_list, a, b):
    visited = [False] * n
    distances = [float('inf')] * n
    distances[a] = 0
    priority_queue = [(0, a)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if visited[current_node]:
            continue

        visited[current_node] = True

        for neighbor, weight in adjacency_list[current_node]:
            new_distance = current_distance + weight

            if not visited[neighbor] and new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances[b]


def spacetravel(n, E, S, a, b):
    adjacency_list = build_adjacency_list(n, E, S)
    shortest_time = find_shortest_time(n, adjacency_list, a, b)
    return None if shortest_time == float('inf') else shortest_time


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
