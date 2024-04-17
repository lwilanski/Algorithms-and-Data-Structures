import heapq


# Ta wersja algorytmu Dijkstry działa podobnie jak poprzednia, ale z kilkoma kluczowymi różnicami.
# Zamiast szukać najkrótszych ścieżek do wszystkich wierzchołków, algorytm zatrzymuje się,
# gdy znajdzie najkrótszą ścieżkę do określonego wierzchołka końcowego 't'.

# Dodatkowo, ten algorytm zawiera krok rekonstrukcji najkrótszej
# ścieżki od wierzchołka startowego do końcowego na końcu procedury.

# Explained version:

def dijkstra_shortest_path_e(G, s, t):
    # Inicjalizacja list visited, distances i parents
    visited = [False] * len(G)
    distances = [float('inf')] * len(G)
    distances[s] = 0  # Odległość dla wierzchołka startowego to 0
    parents = [None] * len(G)
    queue = [(0, s)]  # Dodajemy wierzchołek startowy do kolejki

    while queue:
        # Wyjmujemy wierzchołek o najmniejszej odległości
        _, vertex = heapq.heappop(queue)

        # Jeśli jest to wierzchołek końcowy, przerywamy algorytm
        if vertex == t:
            break

        # Jeśli wierzchołek już był odwiedzony, pomijamy go
        if visited[vertex]:
            continue

        # Oznaczamy wierzchołek jako odwiedzony
        visited[vertex] = True

        # Przechodzimy przez sąsiadów wierzchołka
        for neighbor, weight in G[vertex]:
            new_distance = distances[vertex] + weight  # Nowa potencjalna odległość do sąsiada
            # Jeśli możemy skrócić odległość do sąsiada, robimy to
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parents[neighbor] = vertex  # Aktualizujemy poprzednika sąsiada
                # Dodajemy sąsiada do kolejki z nową odległością
                heapq.heappush(queue, (new_distance, neighbor))

    # Rekonstrukcja najkrótszej ścieżki
    path = []
    current_vertex = t
    while current_vertex is not None:
        path.append(current_vertex)  # Dodajemy wierzchołek do ścieżki
        current_vertex = parents[current_vertex]  # Przechodzimy do poprzednika
    path.reverse()  # Odwracamy ścieżkę, żeby była w poprawnej kolejności

    # Zwracamy ścieżkę jeśli istnieje, w przeciwnym wypadku None
    return path if parents[t] is not None else None


# Copy-paste version

def dijkstra_shortest_path(G, s, t):
    visited = [False] * len(G)
    distances = [float('inf')] * len(G)
    distances[s] = 0
    parents = [None] * len(G)
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
                parents[neighbor] = vertex
                heapq.heappush(queue, (new_distance, neighbor))

    path = []
    current_vertex = t
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = parents[current_vertex]
    path.reverse()

    return path if parents[t] is not None else None
