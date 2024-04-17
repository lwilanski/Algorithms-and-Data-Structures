from collections import deque
from zad4testy import runtests


def bfs_shortest_path(G, s, t):
    visited = [False] * len(G)
    visited[s] = True
    paths = []
    # Zmienna wave mówi nam jak daleko od źródłowego wierzchołka jesteśmy, final_wave będzie więc
    # długością najkrótszej ścieżki z s do t
    final_wave = float('inf')
    queue = deque([(s, [s], 0)])

    while queue:
        vertex, path, wave = queue.popleft()
        # Odwiedzianie wierzchołka dopiero przy wyciąganiu go z kolejki pozwala na dotarcie
        # do tego samego wierzchołka z wielu różnych wierzchołków co jest kluczowe do znalezienia
        # wszystkich ścieżek z s do t (ponieważ musimy wrzucić t do kolejki tyle razy ile jest ścieżek)
        visited[vertex] = True

        if wave > final_wave:
            # Jeżeli final_wave != inf oraz jest większe od poprzednio ustawionej wartości
            # to znaczy że już poszliśmy dalej niż wierzchołek t więc zwracamy paths
            return paths

        for neighbor in G[vertex]:
            if not visited[neighbor]:
                if neighbor != t:
                    queue.append((neighbor, path + [neighbor], wave + 1))
                else:
                    # Znaleźliśmy pierwszą najkrótszą ścieżkę z s do t, ustawiamy final_wave
                    final_wave = wave
                    paths.append(path + [neighbor])

    # Jeżeli okazałoby się że wierzchołek t jest ostatnim i najdalszym wierzchołkiem w grafie
    # i w kolejce nic już nie zostało to też zwracamy paths. Jeżeli ścieżka z s do t nie istnieje
    # to BFS zwróci pustą listę.
    return paths


def longer(G, s, t):
    # Ta funkcja sprawdza warunek z kolumnami i zwraca wynik.
    mat = bfs_shortest_path(G, s, t)

    if not mat:
        return None

    if len(mat) == 1:
        res = (mat[0][0], mat[0][1])
        return res

    elif len(mat[0]) == 1:
        return None

    for i in range(0, len(mat[0]) - 1):
        first = mat[0][i]
        second = mat[0][i + 1]
        found = True
        for j in range(1, len(mat)):
            if mat[j][i] != first or mat[j][i + 1] != second:
                found = False
                break

        if found:
            res = (first, second)
            return res

    return None


runtests(longer, all_tests=True)

G1 = [[1, 13],
     [0, 2],
     [1, 3, 4],
     [2, 5],
     [2, 6],
     [3, 7],
     [4, 7],
     [5, 6, 8],
     [7, 9],
     [8, 10],
     [9, 11],
     [10, 12],
     [11, 13],
     [0, 12]]

G2 = [[1, 2], [0, 2], [0, 1]]

G3 = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7], [10, 11], [9, 12], [9, 12], [10, 11]]

# print(longer(G3, 0, 12))
