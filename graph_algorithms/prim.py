import heapq


# Algorytm Prima służy do znajdywania minimalnego drzewa rozpinającego w grafie ważonym.

# Dopóki drzewo nie pokrywa całego grafu, znajdujemy krawędź o najniższym koszcie
# spośród wszystkich krawędzi prowadzących od wybranych już wierzchołków do
# wierzchołków jeszcze niewybranych. Znalezioną krawędź dodajemy do drzewa rozpinającego.

# Twój kod zaczyna od inicjalizacji listy visited do przechowywania informacji o odwiedzonych wierzchołkach
# i kolejki priorytetowej queue, która jest używana do przechowywania wierzchołków do przetworzenia.

# Pętla while wykonuje się dopóki nie zostanie przetworzone n-1 krawędzi (gdzie n to liczba wierzchołków w grafie).
# W każdej iteracji pętli, z kolejki priorytetowej queue wybierany
# jest wierzchołek o najmniejszym koszcie (najmniejszej wadze).

# Jeśli wierzchołek już został odwiedzony, to pętla while wraca do początku, pomijając resztę kodu.

# Jeśli wierzchołek nie był jeszcze odwiedzony, to jest dodawany do drzewa
# rozpinającego (msp), a zmienna counter jest inkrementowana.

# Po oznaczeniu wierzchołka jako odwiedzonego, wszystkie sąsiednie wierzchołki,
# które nie były jeszcze odwiedzone, są dodawane do kolejki priorytetowej.

# Po zakończeniu pętli while, zwracane jest minimalne drzewo rozpinające.


def prims(G, s):
    # Tworzymy listę odwiedzonych wierzchołków
    visited = [False] * len(G)
    # Tworzymy kolejkę priorytetową z początkowym wierzchołkiem
    queue = [(0, None, s)]
    # Inicjalizujemy licznik odwiedzonych wierzchołków
    counter = 0
    # Inicjalizujemy listę krawędzi minimalnego drzewa rozpinającego
    msp = []

    # Dopóki nie odwiedzimy wszystkich wierzchołków
    while counter < len(G) - 1:
        # Wybieramy wierzchołek o najmniejszym koszcie z kolejki
        vertex = heapq.heappop(queue)

        # Jeśli wierzchołek został już odwiedzony, kontynuujemy pętlę
        if visited[vertex[2]]:
            continue

        # Dodajemy wierzchołek do minimalnego drzewa rozpinającego
        if vertex[1] is not None:
            msp.append((vertex[1], vertex[2]))
            counter += 1

        # Oznaczamy wierzchołek jako odwiedzony
        visited[vertex[2]] = True

        # Dodajemy nieodwiedzonych sąsiadów do kolejki priorytetowej
        for neighbor, weight in G[vertex[2]]:
            if not visited[neighbor]:
                heapq.heappush(queue, (weight, vertex[2], neighbor))

    # Zwracamy minimalne drzewo rozpinające
    return msp



def main():
    G = [[(1, 5), (3, 9), (6, 3)],
         [(0, 5), (2, 9), (4, 8), (5, 6), (7, 7)],
         [(1, 9), (3, 9), (4, 4), (6, 5), (7, 3)],
         [(0, 9), (2, 9), (6, 8)],
         [(1, 8), (2, 4), (5, 2), (6, 1)],
         [(1, 6), (4, 2), (6, 6)],
         [(0, 3), (2, 5), (3, 8), (4, 1), (5, 6), (7, 9)],
         [(1, 7), (2, 3), (6, 9)]]

    print(prims(G, 0))


if __name__ == "__main__":
    main()
