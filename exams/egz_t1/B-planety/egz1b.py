from egz1btesty import runtests


# Funkcja rekurencyjna jaką zaimplementuje to f(i, b) (podana jako podpowiedź)

# f(i, b) = min po wszystkich k = {0, i - 1} z dwóch wartości:
# f(k, 0) + T[k][1]
# f(k, b + (D[i] - D[k])) + C[k] * k
# Warunkiem brzegowym jest f(0, b) = 0
# Rozwiązaniem będzie f(n - 1, 0)

# Poprawnym rozwiązaniem będzie również, rekurencyjne sprawdzenie wszyskich możliwości
# oraz przechowywanie minmimum w podproblemie
def planets(D, C, T, E):
    # tu prosze wpisac wlasna implementacje
    return -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets, all_tests=False)
