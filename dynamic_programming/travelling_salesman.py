import math as m


# Mamy n miast, pomiędzy dowolnymi dwoma miastami jest jakaś odległość.

# Zadanie polega na znalezieniu najkrótszej ścieżki która odwiedza
# wszystkie miasta i kończy w mieście w którym zaczeliśmy.

# Problem o którym mowa jest problemem NP - zupełnym co oznacza że nie ma rozwiązania o czasie
# wielomianowym, co nie zmienia faktu że są lepsze i gorsze algorytmy rozwiązujące ten problem.
# Będziemy reprezentować miasta jako punkty na płaszczyźnie kartezjańskiej, gdzie odległość
# pomiędzy dwoma punktami (x1, y1) i (x2, y2) wynosi sqrt((x2 - x1)^2 + (y2 - y1)^2)
# Punkty zapiszemy jako krotki w liście.

# Algorytm 1: Brute - force
# Brute force w tym przypadku polega na przetestowaniu wszystkich możliwych kolejności miast.
# Jako że zaczynamy w mieście 0 to możliwości będzie (n-1)!, ale że musimy przejrzeć każdą z możliwości
# w czasie liniowym to złożonością takiego rozwiązania będzie O(n!) (nie będe go implementował bo nie ma po co)

# Algorytm 2: Algorytm dynamiczny w przypadku ogólnym
# Implementujemy funkcję rekurencyjną f(A, s, t), która jest równa najkrótszej trasie
# startującej w s i zakończonej w t, odwiedzającą wszystkie wierzchołki z A.
# f(A, s, t) = min z wszystkich f(A \ {t}, s, r) gdzie r to element A \ {t}
# Ten algorytm ma złożoność wykładniczą O(2^n * n^2)

def f(A, s, t, counter=0):
    if counter == len(A) - 1:
        return m.sqrt(((s[0] - A[t][0]) ** 2) + ((s[1] - A[t][1]) ** 2))

    result = float('inf')
    subset = A.copy()
    subset[t] = None
    for i, r in enumerate(subset):
        if r is not None:
            p = f(subset, s, i, counter + 1) + m.sqrt(((A[t][0] - r[0]) ** 2) + ((A[t][1] - r[1]) ** 2))
            if p < result:
                result = p

    return result


a = [(0, 6), (2, 3), (5, 4), (7, 5), (8, 2), (6, 1), (1, 0)]
print(f(a, a[0], 0))


# Algorytm 3: Bitonic TSP
# Algorytm działa przy punktach posortowanych według jednej z osi (w tym przypadku osi x), i polega
# na rozpoczęciu z wierzchołka maksymalnie na lewo i stworzenia dwóch ścieżek. Jedną ścieżką idziemy w prawo z
# wierzchołka startowego do wierzchołka maksymalnie na prawo, a drugą ścieżką wracamy do wierzchołka starowego.

# Będziemy obliczać funkcję rekurencyjną f(i, j) i zakładając że i < j, jest to minimalny koszt dwóch ścieżek
# jednej zakończonej w i drugiej w j, które rozpoczynają w wierzchołki startowym i odwiedzają
# wszystkie wierzchołki z jakiegoś zbioru. Złożoność tego algorytmu to O(n^2)

# f(i, j) = f(i, j - 1) + d(j - 1, j) gdy i < j - 1
# f(j - 1, j) = minimum ze wszystkich f(i, j - 1) + d(i, j) gdzie i < j - 1
# F to tablica do zapamiętywania wartości funkcji a D to tablica z odległościami

def tsp_f(i, j, F, D):
    if F[i][j] != float('inf'):
        return F[i][j]

    if i == j - 1:
        best = float('inf')

        for k in range(j - 1):
            best = min(best, tsp_f(k, j - 1, F, D) + D[k][j])

        F[j - 1][j] = best

    else:
        F[i][j] = tsp_f(i, j - 1, F, D) + D[j - 1][j]

    return F[i][j]
