import random


def partition(A, l, r):
    e = random.randint(l, r)
    A[r], A[e] = A[e], A[r]
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


t = [1, 4, 2, 8, 4]
quick_sort(t, 0, len(t) - 1)
print(t)
