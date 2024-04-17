# Algorytm Bellmana-Forda służy do znajdywania najkrótszych ścieżek w grafie
# pomiędzy wierzchołkiem startowym a wszystkimi innymi wierzchołkami.

# Różni się od Dijkstry tym że dopuszcza krawędzie o ujemnych wagach.
# Nie dopuszcza za to cykli o ujemnej sumie.

# Algorytm Bellmana-Forda zakłada że najkrótsza ścieżka pomiędzy dowolnymi dwoma wierzchołkami
# jest maksymalnie długości |V| - 1, ponieważ jeżeli byłaby dłuższa to znaczy że
# powtórzyliśmy w niej jakiś wierzchołek, a to znaczy że przeszliśmy przez cykl.
# Jako że nie ma cykli o ujemnej sumie, to ten cykl na pewno wydłużył najkrótszą ścieżkę.

# Algorytm wykonuje następujące kroki:

# Inicjalizacja: Wszystkie wierzchołki, z wyjątkiem źródła, są ustawiane
# na nieskończoną odległość, a odległość źródła wynosi 0.

# Relaxacja: Algorytm przechodzi przez wszystkie krawędzie grafu i próbuje zaktualizować
# odległość do wierzchołka docelowego, jeżeli przejście przez wierzchołek źródłowy jest krótsze.

# Wykrywanie cykli o ujemnej wadze: Algorytm przechodzi przez wszystkie krawędzie grafu i sprawdza,
# czy istnieje jakiekolwiek ulepszenie ścieżki. Jeżeli tak, to oznacza to, że istnieje cykl o ujemnej wadze.

# Explained version:

def bellman_ford_e(G, s):
    n = len(G)
    # Inicjalizacja odległości
    distances = [float('inf')] * n
    distances[s] = 0
    predecessors = [None] * n

    # Relaxacja krawędzi
    for _ in range(n - 1):  # Wykonujemy n - 1 iteracji
        for u in range(n):  # Dla każdego wierzchołka w grafie
            for v, weight in G[u]:  # Dla każdego sąsiada wierzchołka
                # Jeżeli odległość przez 'u' jest krótsza, to zaktualizuj odległość i poprzednika
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u

    # Wykrywanie cykli o ujemnej wadze
    for u in range(n):  # Dla każdego wierzchołka w grafie
        for v, weight in G[u]:  # Dla każdego sąsiada wierzchołka
            # Jeżeli można zaktualizować odległość, to graf zawiera cykl o ujemnej wadze
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative weight cycle")

    return distances, predecessors  # Zwracamy odległości i poprzedników


def bellman_ford(G, s):
    n = len(G)
    distances = [float('inf')] * n
    distances[s] = 0
    predecessors = [None] * n

    for _ in range(n - 1):
        for u in range(n):
            for v, weight in G[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u

    for u in range(n):
        for v, weight in G[u]:
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative weight cycle")

    return distances, predecessors
