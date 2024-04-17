
# Zadanie polega na znalezieniu najdłuższego, niekoniecznie spójnego, rosnącego podciągu w tablicy.
# W tym wypadku elementami tablicy są liczby, ale mogą być inne obiekty z relacją porządku liniowego.

# Funkcja rekurencyjna którą zaimplementuję to f(i) co oznacza długość najdłuższego podciągu kończącego się na A[i].
# Funkcję obliczamy jako max(f(k) + 1) gdzie k = {0, 1, ... , i - 1} a warunkiem brzegowym jest A[0] = 1.
# Jak żadna liczba od A[0] do A[i - 1] to f(i) = 1.

# W tej implementacji, tablica z wartościami funkcji f jest na wejście zapełniana jedynkami, więc najwyżej
# wartość funkcji nie ulegnie zmianie jeżeli podciągu nie da się przedłużyć.

# Funkcja lis(A) oblicza wartości funkcji f dla każdego elementu tablicy A jednocześnie tworząc tablicę parents.
# Funkcja sequence(A, parents, ind) odtwarza rozwiązanie korzystając z tablicy parents.

def lis(A):
    n = len(A)
    f = [1] * n
    parents = [None] * n

    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j] and f[j] + 1 > f[i]:
                parents[i] = j
                f[i] = f[j] + 1

    return f, f.index(max(f)), max(f), parents


def sequence(A, parents, ind):
    seq = []
    start = ind

    while start is not None:
        seq.append(A[start])
        start = parents[start]

    return seq[::-1]


A = [2, 1, 4, 3, 1, 5, 2, 7, 8, 3]
result = lis(A)

print(sequence(A, result[3], result[1]))
