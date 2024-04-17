# Łukasz Wilański
from zad3testy import runtests


# Algorytm robi kopię wejściowej tablicy, obraca w niej wszystkie stringi funkcją [::-1]
# następnie dodaje kopię do wejściowej tablicy i sortuje nowo powstałą tablicę quicksortem.
# Na końcu znajduje najdłuższy podciąg takich samych stringów i zwraca jego długość
# (funkcja jest uzupełniona o sytuację w której najmocniejszy string to palindrom)
# Złożoność algorytmu to O(nlog(n)+n)

def partition(A, l, r):
    pivot = A[r]
    i = l - 1
    for j in range(l, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, l, r):
    while l < r:
        pivot = partition(A, l, r)
        quick_sort(A, l, pivot - 1)
        l = pivot + 1


def strong_string(T):
    B = T.copy()
    for i in range(0, len(B)):
        B[i] = B[i][::-1]
    T = T + B
    quick_sort(T, 0, len(T) - 1)
    mlicz = 1
    licz = 1
    for j in range(0, len(T) - 1):
        if T[j] == T[j + 1]:
            licz += 1
        else:
            if T[j] == T[j][::-1]:
                licz = licz // 2
            if licz > mlicz:
                mlicz = licz
            licz = 1

    return mlicz


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests(strong_string, all_tests=True)
