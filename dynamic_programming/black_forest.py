# Black forest to las rosnący na osi liczbowej gdzieś w południowej Anglii.
# Las składa się z n drzew rosnących na pozycjach 0, ... , n - 1.
# Dla każdego i = {0, ... , n - 1} znany jest zyck c(i), jaki można osiągnąć ścinając drzewo z pozycji i
# Twój stary chce uzyskać maksymalny zysk ze ścinanych drzew, ale prawo zabrania ścinania dwóch drzew pod rząd.
# Zadanie polega na wyliczeniu maksymalnego zysku jaki można osiągnać z wycinki.
# Mamy daną tablicę długości n z zyskami, dla poszczególnych drzew.

example = [1, 7, 8, 2, 6, 12, 1, 10, 2, 6, 10]
example1 = [11, 1, 10, 10, 10, 80, 70]


# Algorytm dynamiczny oblicza wartości funkcji f(i), która oznacza maksymalny
# osiągalny zysk na kawałku lasu kończącym się na i (z i-tym drzewem włącznie).

# f(i) = max(f(i - 1), f(i - 2) + C[i]) albo ścinamy i-te drzewo albo nie

def black_forest(C):
    n = len(C)
    f = [-1 for _ in range(n)]
    f[0] = C[0]
    f[1] = max(C[0], C[1])

    for i in range(2, n):
        f[i] = max(f[i - 1], f[i - 2] + C[i])

    return f[n - 1]


print(black_forest(example1))
