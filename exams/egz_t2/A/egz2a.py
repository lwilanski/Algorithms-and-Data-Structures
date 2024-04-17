from egz2atesty import runtests


# Algorytm porównuje każdy punkt z każdym i siłę i-tego punktu zapisuje do tablicy strength[i].
# Jako wynik zwraca max(strength).
# Złożoność tego algorytmu to n^2.
def dominance(P):
    n = len(P)
    strength = [0 for _ in range(n)]

    for i in range(0, n):
        for j in range(i + 1, n):
            if P[i][0] > P[j][0] and P[i][1] > P[j][1]:
                strength[i] += 1

            elif P[i][0] < P[j][0] and P[i][1] < P[j][1]:
                strength[j] += 1

    return max(strength)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(dominance, all_tests=True)
