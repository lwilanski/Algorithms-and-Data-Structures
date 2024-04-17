# Algorytm Floyda-Warshalla stosuje się do znalezienia najkrótszych ścieżek w
# grafie ważonym pomiędzy wszystkimi parami wierzchołków
# Dopuszczamy krawędzie o ujemnych wagach, ale nie dopuszczamy cykli o ujemnej sumie.

# Najpierw tworzymy dwuwymiarową kwadratową tablicę, o wymiarach n x n , gdzie n to rząd grafu.
# Do tej macierzy będziemy wpisywać wyniki.
# M[i][j] to najkrótsza trasa z wierzchołka i do j.
# Pola M[i][i] ustawiamy na 0.
# Jak pomiędzy krawędziami i oraz j jest krawędź, to M[i][j] = waga tej krawędzi
# Teraz w potrójnej pętli przechodzimy przez nasz graf, starając się ulepszyć aktualne dystanse

# Explained version with path reconstruct.

# Tworzymy macierz wag i macierz poprzedników
def matrix(G):
    n = len(G)
    # Macierz wag. Początkowo wszystkie odległości są ustawione na "inf", z wyjątkiem diagonalnych (0).
    M = [[float('inf') for _ in range(n)] for _ in range(n)]
    # Macierz poprzedników. Początkowo wszyscy poprzednicy są ustawieni na None.
    parents = [[None for _ in range(n)] for _ in range(n)]

    # Inicjalizujemy macierz wag i poprzedników
    for v in range(0, n):
        M[v][v] = 0
        for u, weight in G[v]:
            M[v][u] = weight
            parents[v][u] = v  # Zapisujemy poprzednika

    return M, parents


# Implementacja algorytmu Floyda-Warshalla
def floyd_warshall(G):
    n = len(G)
    M, parents = matrix(G)  # Inicjalizujemy macierze

    # Aktualizujemy macierz wag i poprzedników
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                # Jeżeli znaleźliśmy krótszą ścieżkę przez wierzchołek 'k'
                if M[i][j] > M[i][k] + M[k][j]:
                    M[i][j] = M[i][k] + M[k][j]  # Aktualizujemy wagę
                    parents[i][j] = parents[k][j]  # Aktualizujemy poprzednika

    return M, parents


# Odtwarza najkrótszą ścieżkę od 'i' do 'j'
def reconstruct_path(i, j, parents):
    # Jeżeli nie istnieje ścieżka, zwracamy None
    if parents[i][j] is None:
        return None

    # Inicjalizujemy ścieżkę z końca
    path = [j]
    # Idziemy wstecz przez poprzedników aż dojedziemy do 'i'
    while i != j:
        j = parents[i][j]
        path.append(j)  # Dodajemy poprzednika do ścieżki

    # Odwracamy ścieżkę, żeby była w poprawnej kolejności
    return path[::-1]


# Simplified version

def matrix_s(G):
    n = len(G)
    M = [[float('inf') for _ in range(n)] for _ in range(n)]

    for v in range(0, n):
        M[v][v] = 0
        for u, weight in G[v]:
            M[v][u] = weight

    return M


def floyd_warshall_s(G):
    n = len(G)

    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if G[i][j] > G[i][k] + G[k][j]:
                    G[i][j] = G[i][k] + G[k][j]


def main():
    G = [[(2, -2)], [(0, 4), (2, 3)], [(3, 2)], [(1, -1)]]
    G = matrix(G)
    print(G)
    floyd_warshall(G)
    print(G)


if __name__ == "__main__":
    main()
