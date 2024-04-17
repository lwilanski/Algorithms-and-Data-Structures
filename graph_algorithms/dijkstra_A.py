import heapq


# Algorytm Dijkstry jest wykorzystywany do znalezienia najkrótszych ścieżek od danego
# wierzchołka startowego do wszystkich innych wierzchołków w grafie ważonym z nieujemnymi wagami krawędzi.

# Algorytm działa na zasadzie "relaksacji" krawędzi, co oznacza, że stara
# się poprawić aktualnie znaną najkrótszą ścieżkę do każdego wierzchołka.

# Algorytm działa w następujący sposób:

# Inicjalizuje listę odwiedzonych wierzchołków, listę czasów (odległości od wierzchołka startowego do pozostałych)
# oraz listę poprzedników (dla rekonstrukcji ścieżki).

# Ustala wierzchołek startowy oraz jego czas na 0, a dla reszty
# wierzchołków - na nieskończoność (w Pythonie float('inf')).

# Dodaje wierzchołek startowy do kolejki priorytetowej, gdzie
# priorytet to aktualnie znany czas dojścia do danego wierzchołka.

# W pętli, dopóki kolejka nie jest pusta, wybiera wierzchołek o najmniejszym znanym czasie dojścia,
# który nie został jeszcze odwiedzony.

# Oznacza ten wierzchołek jako odwiedzony.

# Dla każdego nieodwiedzonego sąsiada aktualnego wierzchołka, sprawdza czy poprzez ten wierzchołek można
# dotrzeć do sąsiada szybciej niż dotychczas ("relaksuje" krawędź).

# Jeśli tak, aktualizuje czas dojścia do sąsiada oraz jego poprzednika.

# Dodaje sąsiada do kolejki priorytetowej z nowym czasem jako priorytetem.

# Zwraca listę czasów (najkrótszych ścieżek) i poprzedników.

# Explained version:

def dijkstra_e(G, s):
    # Inicjalizacja list visited, times i parents
    visited = [False] * len(G)
    times = [float('inf')] * len(G)
    times[s] = 0  # Czas dla wierzchołka startowego to 0
    parents = [None] * len(G)
    queue = [(0, s)]  # Dodajemy wierzchołek startowy do kolejki

    while queue:
        # Wyjmujemy wierzchołek o najmniejszym czasie
        vertex = heapq.heappop(queue)[1]

        # Jeśli już go odwiedziliśmy, pomijamy go
        if visited[vertex]:
            continue

        # Oznaczamy wierzchołek jako odwiedzony
        visited[vertex] = True

        # Przechodzimy przez sąsiadów wierzchołka
        for neighbor, weight in G[vertex]:
            if not visited[neighbor]:  # Dla nieodwiedzonego sąsiada
                # Jeśli możemy poprawić czas do sąsiada, robimy to
                if times[neighbor] > times[vertex] + weight:
                    times[neighbor] = times[vertex] + weight
                    parents[neighbor] = vertex

                # Dodajemy sąsiada do kolejki z nowym czasem
                heapq.heappush(queue, (times[neighbor], neighbor))

    # Zwracamy listę czasów i poprzedników
    return times, parents


# Copy-paste version:
def dijkstra(G, s):
    visited = [False] * len(G)
    times = [float('inf')] * len(G)
    times[s] = 0
    parents = [None] * len(G)
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
                    parents[neighbor] = vertex

                heapq.heappush(queue, (times[neighbor], neighbor))

    return times, parents


def main():
    # G = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2], [5], [4], [7, 9], [6, 8], [7], [6, 10], [9, 11], [10]]
    # G = [[1], [2], [0, 3], [4], [5, 8], [6, 10], [3], [8], [10], [8], [7, 9]]
    # G = [[(1, 2), (2, 14), (3, 15), (4, 12)], [(0, 2), (2, 3), (6, 13)], [(0, 14), (1, 3), (6, 15), (7, 2)], [(0, 15), (4, 14), (7, 13), (8, 11)], [(0, 12), (3, 14)], [(6, 16), (9, 15)], [(1, 13), (2, 15), (5, 16), (7, 3), (9, 4)], [(2, 2), (3, 13), (6, 3), (8, 12), (9, 11)], [(3, 11), (7, 12), (9, 11)], [(5, 15), (6, 4), (7, 11), (8, 11)]]
    # G = [[(1, 2), (2, 99)], [(0, 2), (2, 2), (3, 99)], [(0, 99), (1, 2), (3, 2)], [(2, 2), (1, 99)]]
    # G = [[(1, 2), (2, 1)], [(0, 2), (2, 5)], [(0, 1), (1, 5)]]
    G = [[(1, 0.2), (3, 3.1), (4, 1.7)], [(0, 0.2), (2, 4.2), (4, 1.1)], [(1, 4.2), (3, 0.1), (4, 8.4)],
         [(0, 3.1), (2, 0.1), (4, 0.3)], [(0, 1.7), (1, 1.1), (2, 8.4), (3, 0.3)]]

    print(dijkstra(G, 0))


if __name__ == "__main__":
    main()
