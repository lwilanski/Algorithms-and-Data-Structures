# Łukasz Wilański
from kol1testy import runtests

# Algorytm dla każdego składnika sumy tworzy podzbiór z którego w którym będzie znajdywał k-ty największy element.
# Aby znaleźć ten element korzysta z funkcji partition i wykonuje ją dopóki szukany element będzie równy pivotovi
# Złożoność czasowa O(np) złożoność pamięciowa O(1)

def partition(A, l, r):
    pivot = A[r]
    i = l - 1
    for j in range(l, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def ksum(T, k, p):
    wyn = 0
    for i in range(0, len(T) - p + 1):
        arr = []
        for j in range(i, i + p):
            arr.append(T[j])

        s = 0
        e = len(arr) - 1
        while True:
            v = partition(arr, s, e)
            if v > len(arr) - k:
                e = v - 1
            elif v < len(arr) - k:
                s = v + 1
            if v==len(arr)-k:
                break
        wyn += arr[v]
    return wyn


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=True)


